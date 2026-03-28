import json
from sympy import isprime, nextprime, factorint

def find_generator(p, factors_dict):
    """Trouve un générateur du groupe multiplicatif modulo p."""
    g = 2
    factors = list(factors_dict.keys())
    while True:
        is_gen = True
        for q in factors:
            if pow(g, (p - 1) // q, p) == 1:
                is_gen = False
                break
        if is_gen:
            return g
        g += 1

def generate_cert(p):
    """Génère récursivement le dictionnaire du certificat de Pratt pour p."""
    if p < 1024:
        return {"p": p}
    
    # On récupère le dictionnaire des facteurs et de leurs exposants
    factors_dict = factorint(p - 1)
    
    # Trouver le générateur pour ce p
    g = find_generator(p, factors_dict)
    
    # Construire la liste des sous-certificats EN PRENANT EN COMPTE LES EXPOSANTS
    pm1 = []
    for factor, count in factors_dict.items():
        # On génère le certificat du facteur une fois...
        sub_cert = generate_cert(factor)
        # ... et on l'ajoute 'count' fois à la liste pm1
        for _ in range(count):
            pm1.append(sub_cert)
            
    return {
        "p": p,
        "g": g,
        "pm1": pm1
    }

def main():
    a_hex = "2c840bc73912bf164f99439327a7968c800a281a33e88056ae061dad66a3c1ccb8d10328f0d4ff708de5e8d01ba6a019a50e06c933558dab2eb5f53f210344b1e2957e79a61dc2e269b46f9761732e9bf7f5db36ef2b4d3819790e5e6cabebf01d5fea37053481e44f8c0255caf65db23e2cb10cdd7024fea607853366e0e46a"
    a = int(a_hex, 16)
    b = a + 2**960

    print("[*] Construction de la base P...")
    P = 1
    base_primes = []
    pr = 2
    
    while P < 2**940:
        base_primes.append(pr)
        P *= pr
        pr = nextprime(pr)
        
    print(f"[+] Base P construite avec {len(base_primes)} petits nombres premiers.")
    
    q_start = a // P + 1
    if q_start % 2 == 0:
        q_start += 1

    print("[*] Recherche de q ...")
    q = q_start
    p_final = None
    q_final = None

    attempts = 0
    while True:
        p = P * q + 1
        if p >= b:
            print("[-] Dépassement de la borne b, il faut ajuster P.")
            break
        
        attempts += 1
        if isprime(q) and isprime(p):
            p_final = p
            q_final = q
            print(f"[+] Succès après {attempts} itérations !")
            break
        q += 2

    if p_final is None:
        return

    print("[*] Génération du certificat complet...")
    
    # Pour le grand p, la factorisation est 1 fois chaque élément de base_primes, et 1 fois q_final
    factors_of_p_minus_1 = {pr: 1 for pr in base_primes}
    factors_of_p_minus_1[q_final] = 1
    
    g_final = find_generator(p_final, factors_of_p_minus_1)
    
    pm1_list = []
    # On ajoute la base
    for pr in base_primes:
        pm1_list.append({"p": pr})
    # On ajoute le certificat complexe de q_final
    pm1_list.append(generate_cert(q_final))

    certificat = {
        "p": p_final,
        "g": g_final,
        "pm1": pm1_list
    }

    with open("./JavaScriptObjectNotation/certificat_pratt.json", "w") as f:
        json.dump(certificat, f)
        
    print("[+] Terminé ! Le certificat a été sauvegardé dans './JavaScriptObjectNotation/certificat_pratt.json'")

if __name__ == "__main__":
    main()