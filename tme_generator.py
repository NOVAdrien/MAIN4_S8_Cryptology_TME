import random
from sympy import isprime



def generate_p(a, b, q):
    
    # On recherche le premier nombre multiple de q dans l'intervalle [a, b) et le définir comme point de départ
    r = (a - 1) % q
    if r != 0:
        step = q - r
    else:
        step = 0
    start = a + step

    # Et on parcours les nombres dans l'intervalle [a, b) par pas de q à partir de ce point de départ jusqu'à trouver un nombre premier
    for p in range(start, b, q):
        if isprime(p):
            return p


def generate_g(p, q):
    
    while True:
        x = random.randint(2, p - 2)
        g = pow(x, (p - 1) // q, p)
        if g != 1:
            return g


if __name__ == "__main__":
    # Convertir les chaînes hexadécimales en entiers
    a_hex = "f5c9d3253a67e46073550a07ea6d36a1ad08de67e49fbdaec8b70437c10ddbfc2d5d24024c0f0bb5a5cb014fe7da4a9cf3b69b302afd19134180165571bbafd8c21c0493441b38a1afedabc26622738e8de9c64169af2ea96cf5fdf39751295e237704cae3a5c76f2ae7a2821acea059598456b645563867a4a0e25c2b6bb77bc49e9c13755d13d8598c697ef862b2542bbfa9a9545aff6d57d7542390bd3d517ca8e631db28e055a304a45049c50c92bc818bbb0c3f33f84c07340fa826619371dead9c06972b652c59233c8227d6630cb198f9b3cdbf903c0903ae59454c289d2f2444a298142334334410ef880d1cd0547f447bce510042b8d8199d3878b4"
    a = int(a_hex, 16)
    b =  a + 2**1950
    q = int("ddcf292ef95a5501e9ea8d1a03dbb9014bfe595627fe7f34f976a32c9701ba79", 16)

    # Générer p
    p = generate_p(a, b, q)
    assert a <= p < b, f"Erreur: p ({p}) n'est pas dans l'intervalle [a, b)"
    assert (p - 1) % q == 0, f"Erreur: p ({p}) - 1 n'est pas un multiple de q ({q})"

    # Générer g
    g = generate_g(p, q)
    assert pow(g, q, p) == 1, "Erreur: g**q == 1 mod p"

    print(f"p premier tel que (a <= p < b) et (p - 1) soit un multiple de q: \n{p}")
    print(f"g tel que g**q == 1 mod p: \n{g}")