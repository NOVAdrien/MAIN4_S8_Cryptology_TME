from Crypto.PublicKey import RSA
import base64

# ══════════════════════════════════════════════
# DONNÉES
# ══════════════════════════════════════════════

PEM = """-----BEGIN PUBLIC KEY-----
MIIBITANBgkqhkiG9w0BAQEFAAOCAQ4AMIIBCQKCAQEAy7nQxx7TmJKuXFZwhY/g
j1bj2RjbUUOfjsInkLVeoGV3yb8qXJnoJkMegI/2WBMti6RdYtHYY5f98iNCXk6B
bKeOOlIZ3cIsnsik076uUYe2YHv3ukXl5rqHce5Cmfnw2ntT/iB1DbQ6nxKiNfTE
e7YCWlZA69fGb1ZAYau0Z6+vRNY3XhvbCnpO+59lX26iw34TPNS865ngRiLeycQG
COiagvsMjMIyU+2RG6YLvPCQJPfHKoXiI3LMu8+tUPmRiUNThfC5a/gyjZW0tnO2
1tiZKChG+tHOW/BGtLOZH4P9aNhCEkBUN6C5I9aTabImucUdHEycT7b5xz1PTX1J
NQICAQE=
-----END PUBLIC KEY-----"""

C = 0x5ee512e0a699a0334acb7a0fe9ac37b5fb5f0d409f76d4382374e9186c9a7ca9515c83a546e570ff3e4dada4392f0fe729e6b00977597f97ff0c4ed036a4f04f7e65fff2a0457b985d117c557fb9751071967b14b052d3b1ee9fcfa2fab0e20bdd838344c027d893c848344262c0feebfaf774db05c54618f5f777999ee5a58fb3a3448c806135bcc090bb7de259d783979fe7972c9fc5d03882c4fac2d437ca11f9d46eb4880b0cbb5a71b8de261a4975cb3e5d728b63229202b70c40c1518fdca441a332ba177a9deacc164921eaf9666c22feab4c50eac4cdd004bd24c71c644d4940d765acbd706b9056ece6602faac0435372c41e6ce26f014d0d6eb4c3

C1 = 0x5c07330e315d0abacaf6d77143c46a1c30c649c55aac3121c86f846df52412a6860c01adc6344d5b97bbce811021dca0cd7aba2eea646b6fe47f2d5588313b96c8f6633761a1db00d0381c64ae809734c7e4ab1c606cc3eca1aa8d9a180f7f2b3820fa3114252069c3d2e175c846b0d429adb6c4920b49ea8e28be19c90907f2593e05ed6b1e8b536494157350e3bdc6a7fcca17d905b500e088a60d2e1c2f011d80d197317fccb12ed060362341fbfda078cc5039a5960778507d2048eb33d36285d5ada9b6c74b47fa899bd7c0de1c04b91bc9ca510fa4857507f726cde62faa68f9071920c0e4ce1d007612b7e5a88219fcc5e1450c108598d22b03763549

# ══════════════════════════════════════════════
# EXTRACTION DE N ET E
# ══════════════════════════════════════════════

key = RSA.import_key(PEM)
n = key.n
e = key.e
print(f"n = {hex(n)[:20]}...")
print(f"e = {e}")

# ══════════════════════════════════════════════
# FRANKLIN-REITER ATTACK
# Polynômes : f1(x) = x^e - C, f2(x) = (x+1)^e - C'
# PGCD donne (x - M)
# ══════════════════════════════════════════════

def poly_gcd(a, b, n):
    """PGCD de deux polynômes sur Z/nZ"""
    while b:
        a, b = b, poly_mod(a, b, n)
    return a

def poly_mod(a, b, n):
    """Reste de la division de a par b sur Z/nZ"""
    if not b:
        return a
    # Division polynomiale sur Z/nZ
    a = list(a)
    b = list(b)
    
    db = len(b) - 1
    # Coefficient dominant de b
    inv_lead = pow(b[-1], -1, n)
    
    while len(a) - 1 >= db:
        coef = (a[-1] * inv_lead) % n
        deg_diff = len(a) - 1 - db
        for i in range(len(b)):
            a[deg_diff + i] = (a[deg_diff + i] - coef * b[i]) % n
        a.pop()
    
    # Enlever les zéros de tête
    while a and a[-1] == 0:
        a.pop()
    
    return a

def poly_pow_mod(base, exp, mod_poly, n):
    """Calcule base^exp mod mod_poly sur Z/nZ (exponentiation rapide)"""
    result = [1]  # polynôme constant 1
    base = [x % n for x in base]
    
    while exp > 0:
        if exp % 2 == 1:
            result = poly_mod(poly_mul(result, base, n), mod_poly, n)
        base = poly_mod(poly_mul(base, base, n), mod_poly, n)
        exp //= 2
    
    return result

def poly_mul(a, b, n):
    """Multiplication de deux polynômes sur Z/nZ"""
    if not a or not b:
        return []
    result = [0] * (len(a) + len(b) - 1)
    for i, ca in enumerate(a):
        for j, cb in enumerate(b):
            result[i + j] = (result[i + j] + ca * cb) % n
    return result

def poly_sub(a, b, n):
    """Soustraction de deux polynômes sur Z/nZ"""
    length = max(len(a), len(b))
    result = [0] * length
    for i in range(len(a)):
        result[i] = a[i] % n
    for i in range(len(b)):
        result[i] = (result[i] - b[i]) % n
    while result and result[-1] == 0:
        result.pop()
    return result

print("\n=== Franklin-Reiter Attack ===")
print("Calcul de x^e - C  et  (x+1)^e - C' ...")

# f1(x) = x^e - C  → représenté comme liste [coef_deg0, coef_deg1, ...]
# f1 = x^e - C → [-C, 0, 0, ..., 0, 1] avec 1 en position e
f1 = [(-C) % n] + [0] * (e - 1) + [1]

# f2(x) = (x+1)^e - C'
# On calcule (x+1)^e par binôme de Newton
print("Calcul du binôme de Newton pour (x+1)^e ...")
from math import comb
f2_coeffs = [comb(e, k) % n for k in range(e + 1)]  # coefficient de x^k dans (x+1)^e
f2_coeffs[0] = (f2_coeffs[0] - C1) % n  # soustraire C'
f2 = f2_coeffs

print("Calcul du PGCD des polynômes...")
g = poly_gcd(f1, f2, n)
print(f"PGCD degré : {len(g)-1}")
print(f"PGCD : {g}")

# Si degré 1 : g = [a, b] → b*x + a → x = -a/b mod n → M = -g[0] * inv(g[1]) mod n
if len(g) == 2:
    M = (-g[0] * pow(g[1], -1, n)) % n
    print(f"\n✅ M (int) = {M}")
    try:
        msg = M.to_bytes((M.bit_length() + 7) // 8, 'big').decode('ascii')
        print(f"✅ M (texte) = {msg}")
    except:
        msg_bytes = M.to_bytes((M.bit_length() + 7) // 8, 'big')
        print(f"✅ M (bytes) = {msg_bytes}")
else:
    print("❌ PGCD de degré inattendu, vérifier les données")