from Crypto.PublicKey import RSA
import random

TARGET = "+++ATRIUM+++"

BITS = 1024  # plus rapide que 2048
# Quelques exposants publics fréquents + d'autres impairs
E_CANDIDATES = [
    3, 5, 17, 257, 65537,
    7, 11, 13, 19, 23, 29, 31, 37, 41, 43, 47,
    73, 101, 127, 193, 337, 769, 1223, 4099, 8191
]

tries = 0
e_index = 0

while True:
    tries += 1

    # 1) on balaie une liste d'exposants, puis 2) on prend des impairs aléatoires
    if e_index < len(E_CANDIDATES):
        e = E_CANDIDATES[e_index]
        e_index += 1
    else:
        # e aléatoire impair (évite les valeurs trop petites / trop grandes)
        e = random.randrange(3, 1 << 16, 2)

    try:
        key = RSA.generate(BITS, e=e)
    except ValueError:
        # arrive si gcd(e, phi(n)) != 1, ou si e invalide => on retente
        continue

    pub_pem = key.publickey().export_key(format="PEM").decode()
    if TARGET in pub_pem:
        priv_pem = key.export_key(format="PEM").decode()

        print(f"[OK] Trouvé en {tries} essais (e={e}, bits={BITS})\n")
        print("===== PUBLIC KEY =====")
        print(pub_pem)
        print("===== PRIVATE KEY =====")
        print(priv_pem)
        break

    if tries % 200 == 0:
        print(f"... {tries} essais (dernier e={e})")
