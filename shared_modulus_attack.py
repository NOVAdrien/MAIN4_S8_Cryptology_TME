#!/usr/bin/env python3
import math
import secrets
import os
from typing import Tuple
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

# --- Configuration des chemins ---
pubA_path = "./Keys/PublicKeys/pk_atriumA.pem"
pubB_path = "./Keys/PublicKeys/pk_atriumB.pem"
privA_out = "./Keys/PrivateKeys/sk_atriumA.pem"
privB_out = "./Keys/PrivateKeys/sk_atriumB.pem"

d_hex_B = (
    "4aeb9f587154bd8c124d3b33102ca26b35330e07e29476f8e256fc8bbc318172"
    "7348268bdc52032eeeb3cabe8542f189441dd3fed32b7a78f88a6cd43e6d0bcc"
    "fc2664b957c7c5111711484ab2ee6b78fd8949d82ad7367e972ac3e3b7d98130"
    "2395579c83dd14d8646956f641261af3deebe715ce95ee77ee3fff133cb85065"
    "5d46fb9aaeba0d179df907c85911099b72a7ffebc8bab69829e222bbaa9056b0d"
    "520cac5d02e5b23bcdbe35ef32bebdeffaa12aea5d2166f5961a78fc85eb8bf0"
    "1dddfca7b7892c04785113ca07aed262e946fe6052d47767918cd8b155f775c7c"
    "aef1f4c2445059975fa2953cd9cc7bd3cada81313fb4d9916aab7563e3d5ed"
)

# -----------------------------
# Fonctions Mathématiques
# -----------------------------
def egcd(a, b):
    if b == 0: return (a, 1, 0)
    g, x1, y1 = egcd(b, a % b)
    return (g, y1, x1 - (a // b) * y1)

def modinv(a, m):
    g, x, _ = egcd(a, m)
    if g != 1: raise ValueError("Pas d'inverse modulaire")
    return x % m

def factor_n_from_ed(e, d, n):
    """Retrouve p et q à partir de (e, d, n)"""
    k = e * d - 1
    r = k
    t = 0
    while r % 2 == 0:
        r //= 2
        t += 1
    
    while True:
        g = secrets.randbelow(n - 1) | 1
        x = pow(g, r, n)
        if x == 1 or x == n - 1: continue
        for _ in range(t - 1):
            y = pow(x, 2, n)
            if y == n - 1: break
            if y == 1:
                p = math.gcd(x - 1, n)
                return p, n // p
            x = y
        else: continue
        break

# -----------------------------
# Exportation PEM
# -----------------------------
def save_priv_key(p, q, e, path):
    n = p * q
    phi = (p - 1) * (q - 1)
    d = modinv(e, phi)
    
    # Paramètres pour la structure de clé privée
    dp = d % (p - 1)
    dq = d % (q - 1)
    qi = modinv(q, p)
    
    priv_nums = rsa.RSAPrivateNumbers(
        p=p, q=q, d=d, dmp1=dp, dmq1=dq, iqmp=qi,
        public_numbers=rsa.RSAPublicNumbers(e=e, n=n)
    )
    
    pem = priv_nums.private_key().private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        f.write(pem)

# -----------------------------
# Exécution principale
# -----------------------------
def main():
    # 1. Chargement des clés publiques
    with open(pubA_path, "rb") as f:
        pubA = serialization.load_pem_public_key(f.read())
    with open(pubB_path, "rb") as f:
        pubB = serialization.load_pem_public_key(f.read())

    nA, eA = pubA.public_numbers().n, pubA.public_numbers().e
    nB, eB = pubB.public_numbers().n, pubB.public_numbers().e
    dB = int(d_hex_B, 16)

    print(f"nA: {nA}")
    print(f"nB: {nB}")
    print(f"eA: {eA}")
    print(f"eB: {eB}")

    if nA != nB:
        print("\n[!] Erreur: Les modules nA et nB ne sont pas identiques.")
        return

    # 2. Factorisation de n via la clé B
    print("\n[*] Factorisation de n en cours...")
    p, q = factor_n_from_ed(eB, dB, nB)
    phi = (p - 1) * (q - 1)
    print(f"phi(n): {phi}")

    # 3. Génération des fichiers de clés privées
    save_priv_key(p, q, eA, privA_out)
    save_priv_key(p, q, eB, privB_out)

    print(f"\n[+] Succès !")
    print(f"Clé privée A écrite dans: {privA_out}")
    print(f"Clé privée B écrite dans: {privB_out}")

if __name__ == "__main__":
    main()