import base64
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

# --- CONFIGURATION ---
CLE_PRIV_SOURCE = "mykey.pem" # Ton ancienne clé privée (la 1ère que tu as postée)
TARGET = "+++ATRIUM+++"

def solve():
    # 1. Charger la clé originale
    with open(CLE_PRIV_SOURCE, "rb") as f:
        old_priv = serialization.load_pem_private_key(f.read(), password=None)
    
    pn = old_priv.private_numbers()
    n = pn.public_numbers.n
    target_bytes = base64.b64decode(TARGET)

    # 2. Trouver l'exposant e qui fait apparaître le texte dans le PEM
    found_e = None
    for p in range(100):
        for pad in [b'\x00', b'\x01']:
            e_test = int.from_bytes((pad * p) + target_bytes + b'\x01', 'big')
            if e_test % 2 == 0: e_test += 1
            
            # Test du rendu PEM
            pub = rsa.RSAPublicNumbers(e_test, n).public_key()
            pem = pub.public_bytes(serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo)
            if TARGET.encode() in pem:
                found_e = e_test
                break
        if found_e: break

    if not found_e:
        print("❌ Impossible de générer l'exposant.")
        return

    # 3. Recalculer la clé PRIVÉE cohérente (d = e^-1 mod phi)
    phi = (pn.p - 1) * (pn.q - 1)
    d = pow(found_e, -1, phi)
    
    new_priv = rsa.RSAPrivateNumbers(
        p=pn.p, q=pn.q, d=d, 
        dmp1=d % (pn.p - 1), dmq1=d % (pn.q - 1), iqmp=pow(pn.q, -1, pn.p),
        public_numbers=rsa.RSAPublicNumbers(found_e, n)
    ).private_key()

    # 4. SAUVEGARDER LES DEUX
    with open("atrium_final_pub.pem", "wb") as f:
        f.write(new_priv.public_key().public_bytes(serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo))
    
    with open("atrium_final_priv.pem", "wb") as f:
        f.write(new_priv.private_bytes(
            serialization.Encoding.PEM, 
            serialization.PrivateFormat.TraditionalOpenSSL, 
            serialization.NoEncryption()
        ))

    print("✅ Fichiers générés : atrium_final_pub.pem et atrium_final_priv.pem")
    print(f"Exposant e : {found_e}")

solve()