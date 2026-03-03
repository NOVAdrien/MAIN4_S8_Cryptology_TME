import hashlib
import binascii

# --- DONNÉES DU DIRECTEUR ---
N_hex = "bed6cdc8f142d61854b6bddc6f9eb36bbbf4e5dab77207240078293c384eb53d4e3a0b2f250d6dd1192448973b250d563517218c90a12c0447f5b31df37410d8a2e21573c0f05a8aa9924114708053b08878d3b53ccd35ba3516c02c3692d048ad46e98b7fbe13a99b4670fcc96dd51e7a04a3da93493ab5b5b0ff7ae77708d74f8c964112523fed59c1bdc949bfea248ff0a39285302b0292a6b8de23f98a920135cf1b5660e16eb4fddbb24b4312ef5c59f4a02a67dff2b28a6d1b0c3e3942c1736faa43a94f0995e04bda6c873a1cbaf6685424196abc6185d3e40fc1cc276fae72de0465d9748e6eb7e165b62800a53f2c67e4693cc92b37a9ee4bc449e9"
N = int(N_hex, 16)
e = 65537

# 1. Création du bloc PKCS#1 v1.5 avec Hash SHA-256
msg = b"I, the lab director, hereby grant AdrienPanguel permission to take the BiblioDrone-NG."
msg_hash = hashlib.sha256(msg).digest()
# Identifiant ASN.1 standard pour SHA-256
sha256_asn1_id = binascii.unhexlify("3031300d060960864801650304020105000420")
data = sha256_asn1_id + msg_hash

# Padding FF pour atteindre 256 octets
pad_len = 256 - 3 - len(data)
M_bytes = b"\x00\x01" + (b"\xff" * pad_len) + b"\x00" + data
M = int(binascii.hexlify(M_bytes), 16)

# 2. Aveuglement (Blinding)
# On utilise x = 2 comme facteur
x = 2
M_blind = (M * pow(x, e, N)) % N

print(f"--- DATA À ENVOYER AU DIRECTEUR ---")
print(hex(M_blind)[2:])