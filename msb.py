import requests
import json
from Crypto.PublicKey import RSA

# ══════════════════════════════════════════════
# DONNÉES
# ══════════════════════════════════════════════

PEM = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0u0LwPCWMF6QcfDCEmuP
Y3UnIbYQvdxy9Kw19KZYqsFfoSKFrH0zHkhFD1AEPBBGXFYwVoZMBr4m1zIoKd7v
UhHHSlj8QbApBWxnMdq5qtU1hZHU03d5Ei4Jya5iCyJxUmfpSNPtmfJyvYujpzAt
WulaJ6I+DtshhgDkDqY+GKyKuE2w0pcItwBZK06vYXN0CLoSl+1nOdhrHV7cH9qb
qTSgcoYKKOp7nmaqbJxovRB9N5y4M9VFr4f7WvDP5DcT/n6mnQzP4kNRrvklbCuv
ekBcapX0uhvMVhQms989dQXQRGk4Id5fyUd92X2toR6nIvYSfMWdGuDor8i4SdcF
8QIDAQAB
-----END PUBLIC KEY-----"""

C_hex = "373062d70886210c9c884d13d9b35eddc47843916a882fbe5e6f5f6814f99c8039f07902ed06c65f29fc3594bef09cba02e425f090c8cf783bed79abe9d1c12dde2e756c47e37844f04172852eace427d92ed90f0af38802253c7c953af718bc4383c6c051d7cb3afaa58eea2a737040b619cf80fd5d6adec401e134180e0d37bc5c7b9e2182f00da6b6870143b1ba797d73f0baf12b2ea9bb1913f0ea46320d1f68553fac53a6759b46345fecf4ca5a07a926af2869f0e94ed0f0cece8fceb574ed6cadfd6a5e036179ce37471a863be3a4a82655ffcba4971ef8c19f848a8d6e46597454792180094912f599501bf56a636ed243ac15c130b6f5438554dd87"

key = RSA.import_key(PEM)
n = key.n
e = key.e
C = int(C_hex, 16)

print(f"n bits: {n.bit_length()}")
print(f"e = {e}")

# ══════════════════════════════════════════════
# ORACLE
# ══════════════════════════════════════════════

url = "http://m1.tme-crypto.fr:8888/"
headers = {'Content-Type': 'application/json'}
WORLD_ID = "ac65d4bb4287c3e16ff27c769e3a4a40"

call_count = 0

def msb_oracle(ciphertext_int):
    global call_count
    call_count += 1
    ct_hex = hex(ciphertext_int)[2:].zfill(512)
    data = {
        "jsonrpc": "2.0",
        "method": "chip.whisperer-pro",
        "params": {"world_id": WORLD_ID, "ciphertext": ct_hex},
        "id": 1
    }
    r = requests.post(url, headers=headers, data=json.dumps(data))
    result = r.json()
    if "result" in result:
        val = result["result"]
        # Normaliser : accepter 0/1, "0"/"1", True/False
        if val in (1, "1", True):
            return 1
        else:
            return 0
    print(f"Erreur oracle: {result}")
    return None

# Test initial
print("\nTest oracle avec C original...")
test = msb_oracle(C)
print(f"Oracle(C) = {test}")

# ══════════════════════════════════════════════
# ATTAQUE MSB ORACLE
# ══════════════════════════════════════════════

print(f"\n=== Attaque MSB Oracle ===")
print(f"Bits à traiter: {n.bit_length()}")

lb = 0
ub = n
current_C = C
nbits = n.bit_length()

for i in range(nbits):
    # Multiplier m par 2 : chiffrer 2*m → C * 2^e mod n
    current_C = (current_C * pow(2, e, n)) % n

    mid = (lb + ub) // 2

    msb = msb_oracle(current_C)
    if msb is None:
        print("Erreur oracle, arrêt")
        break

    if msb == 1:
        lb = mid
    else:
        ub = mid

    if i % 200 == 0:
        print(f"  Bit {i+1}/{nbits} | appels={call_count} | range={ub-lb}")

    if lb >= ub - 1:
        break

m = ub
print(f"\n✅ M trouvé en {call_count} appels oracle")

# Retirer le padding PKCS#1 v1.5
m_bytes = m.to_bytes((m.bit_length() + 7) // 8, 'big')
print(f"M bytes (hex) = {m_bytes.hex()}")

# PKCS#1 v1.5 format: 0x00 0x02 <random> 0x00 <message>
try:
    # Chercher le 0x00 séparateur après le padding aléatoire
    idx = m_bytes.index(b'\x00', 2)
    plaintext = m_bytes[idx+1:]
    print(f"\n✅ Plaintext (hex) = {plaintext.hex()}")
    print(f"✅ Plaintext (texte) = {plaintext.decode('utf-8', errors='replace')}")
except Exception as ex:
    print(f"Pas de padding PKCS trouvé, message brut: {m_bytes}")
    print(f"Texte brut: {m_bytes.decode('latin-1', errors='replace')}")