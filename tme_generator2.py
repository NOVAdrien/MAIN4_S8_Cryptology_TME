import gmpy2

# Données du challenge
a_hex = "c77d83a7fd9416dbb0ed531372bcae3ed82a4f2f488c540d27f4de7cd3f972428fd8e5aed2a6cfa2e182fd9514278f2a2adeb8d55e8cac0e22b9a41e0a02bd641868d6c98ff68cad9c2f65492d1856b789210530b0cdabb51b59ab3f434f477fd4f14c2df80b1864c28489cc2dd2fa4857e69a9bc7d5aea9d7bd8241d087ae6266a27d35d942d9886be92b6b45ec0cd31533e8141541cee16dc12c637851a4c7b1f4439cfff8b0094099beba35611c2390719902645ba39083dd1e7cddf45bba1df49b1082d857a65c36bc902572eef78faf8416c2f0aef63bc57098cb2af925d032e3d746b3929e99284913d5b2fcabc4dfbda88d66ff6c826eb373452e90de"
q_hex = "669819f383990b34742018a2ce8e8feefa462b86747b3b03967177397913469b8eb9606804195edbf7f2073308f5192d"

a = gmpy2.mpz(a_hex, 16)
b = a + gmpy2.mpz(2) ** 1950
q = gmpy2.mpz(q_hex, 16)


def find_p(a: gmpy2.mpz, b: gmpy2.mpz, q: gmpy2.mpz):
    """
    Cherche p = q * m + 1 avec p premier, a <= p < b.
    On prend m pair pour avoir p impair (plus naturel),
    donc m = 2*r avec r premier.
    """
    if not gmpy2.is_prime(q):
        raise ValueError("q n'est pas premier")

    r_min = (a - 1) // (2 * q)
    r_max = (b - 1) // (2 * q)

    r = gmpy2.next_prime(r_min)

    trials = 0
    while r < r_max:
        trials += 1
        if trials % 500 == 0:
            print(f"... {trials} tentatives")

        p = 2 * q * r + 1
        if a <= p < b and gmpy2.is_prime(p):
            return p, r

        r = gmpy2.next_prime(r)

    raise ValueError("Aucun p trouvé dans l'intervalle")


def find_primitive_root(p: gmpy2.mpz, prime_factors_phi):
    """
    Trouve un g d'ordre p-1 modulo p.
    Si phi = p-1 et F est l'ensemble des facteurs premiers de phi,
    g est primitif ssi pour tout f dans F :
        g^(phi/f) != 1 mod p
    """
    phi = p - 1
    g = gmpy2.mpz(2)

    while g < p:
        ok = True
        for f in prime_factors_phi:
            if gmpy2.powmod(g, phi // f, p) == 1:
                ok = False
                break
        if ok:
            return g
        g += 1

    raise ValueError("Aucune racine primitive trouvée")


def main():
    print("[*] Recherche de p...")
    p, r = find_p(a, b, q)

    phi = p - 1
    # Ici phi = 2 * q * r, avec 2, q, r premiers
    prime_factors_phi = [gmpy2.mpz(2), q, r]

    print("[*] Recherche de g...")
    g = find_primitive_root(p, prime_factors_phi)

    # Vérifications
    assert a <= p < b
    assert gmpy2.is_prime(p)
    assert phi % q == 0

    # Vérifie que g est bien d'ordre p-1
    for f in prime_factors_phi:
        assert gmpy2.powmod(g, phi // f, p) != 1
    assert gmpy2.powmod(g, phi, p) == 1

    # Format demandé pour (p-1)//q
    # (p-1)//q = 2 * r
    factors_p1_over_q = f"2, {r}"

    print("\n===== RÉSULTATS =====")
    print(f"p = {p}")
    print(f"g = {g}")
    print(f"(p-1)//q = 2 * {r}")
    print(f"Format à saisir pour (p-1)//q : {factors_p1_over_q}")


if __name__ == "__main__":
    main()