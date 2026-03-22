import hashlib
import binascii
import subprocess

# Récupérer le modulus de la clé publique du directeur
cmd = [
    "openssl", "rsa",                               # Commande OpenSSL pour manipuler des clés RSA
    "-pubin",                                       # Indique à OpenSSL que le fichier donné en entrée est une clé publique
    "-in", "./Keys/PublicKeys/pk_director.pem",     # Chemin du fichier contenant la clé publique RSA du directeur
    "-noout",                                       # Demande à OpenSSL de ne pas réafficher la clé elle-même
    "-modulus"                                      # Demande à OpenSSL d’afficher seulement le modulus RSA, c’est-à-dire N
]

# Lancer la commande OpenSSL
result = subprocess.run(cmd, capture_output=True, text=True)

# Tester si le processus OpenSSL s’est terminé avec une erreur
if result.returncode != 0:
    print("Erreur lors de la lecture du modulus :")
    print(result.stderr)
    raise SystemExit(1)

# Transformer la sortie d’OpenSSL en une chaîne hexadécimale propre
N_hex = result.stdout.replace("Modulus=", "").strip().lower()

# --- DONNÉES DU DIRECTEUR ---
N = int(N_hex, 16)
e = 65537

# Création du bloc PKCS#1 v1.5 avec hash SHA-256
msg = b"I, the lab director, hereby grant AdrienPanguel permission to take the BiblioDrone-NG."
msg_hash = hashlib.sha256(msg).digest()

# Identifiant ASN.1 standard pour SHA-256
sha256_asn1_id = binascii.unhexlify("3031300d060960864801650304020105000420")
data = sha256_asn1_id + msg_hash

# Taille du modulus en octets
k = (N.bit_length() + 7) // 8

# Padding FF pour atteindre la taille du modulus
pad_len = k - 3 - len(data)
if pad_len < 8:
    print("Erreur : padding PKCS#1 v1.5 invalide.")
    raise SystemExit(1)

# Construction du bloc RSA complet en binaire
M_bytes = b"\x00\x01" + (b"\xff" * pad_len) + b"\x00" + data
M = int.from_bytes(M_bytes, "big")

# Aveuglement (Blinding) qui utilise x = 2 comme facteur
x = 2
M_blind = (M * pow(x, e, N)) % N

print("--- MODULUS DU DIRECTEUR ---")
print(N_hex)
print()

print("--- DATA À ENVOYER AU DIRECTEUR ---")
print(hex(M_blind)[2:])