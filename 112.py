def multiply_poly(A, B, Q):
    """Multiplie deux polynômes A et B dans GF(2)[x] modulo Q"""
    res = 0
    while B > 0:
        if B & 1:
            res ^= A
        A <<= 1
        if A & (1 << 64): # Si le degré atteint 64, on réduit modulo Q
            A ^= Q
        B >>= 1
    return res

def power_poly(A, exp, Q):
    """Calcule A^exp modulo Q"""
    res = 1
    base = A
    while exp > 0:
        if exp & 1:
            res = multiply_poly(res, base, Q)
        base = multiply_poly(base, base, Q)
        exp >>= 1
    return res

def inverse_poly(A, Q):
    """Calcule l'inverse d'un polynôme A modulo Q(x) dans GF(2^64).
       Puisque GF(2^64) est un corps, A^(2^64 - 2) est l'inverse de A (Fermat)."""
    exp = (1 << 64) - 2
    return power_poly(A, exp, Q)

def solve_crc64():
    # Polynôme générateur Q(x) = x^64 + x^4 + x^3 + x + 1
    Q = 0x1000000000000001b
    
    # La cible (le hash)
    target_hash = 0x1a70e26a5e14b7eb
    
    # Le facteur par lequel P(x) est multiplié : x^64 modulo Q(x)
    # x^64 mod Q(x) = x^4 + x^3 + x + 1 (c'est-à-dire 0x1B)
    X_64 = 0x1b
    
    # On calcule l'inverse de (x^4 + x^3 + x + 1) modulo Q(x)
    inv_X_64 = inverse_poly(X_64, Q)
    
    # On calcule P(x) = S(x) * inverse(x^64) modulo Q(x)
    P = multiply_poly(target_hash, inv_X_64, Q)
    
    # Convertir le polynôme P en bytes pour avoir le mot de passe
    password_bytes = P.to_bytes(8, byteorder='big')
    
    print(f"[*] Hash cible : {hex(target_hash)}")
    print(f"[*] Inverse de X^64 trouvé.")
    print(f"[+] Mot de passe en Hex : {hex(P)}")
    
    # On essaye de l'afficher en ASCII si possible
    try:
        print(f"[+] Mot de passe ASCII (si lisible) : {password_bytes.decode('ascii')}")
    except:
        print("[!] Le mot de passe contient des caractères non imprimables. Utilisez la version Hex ou Bytes.")
        print(f"[+] Mot de passe Bytes : {password_bytes}")

if __name__ == "__main__":
    solve_crc64()