import subprocess
from pathlib import Path

# Signer le fichier pk_friend1.pem avec la clé privée my_sk.pem
cmd = [
    "openssl", "dgst",                        # Outil OpenSSL pour calculer un condensat
    "-sha256",                                # Algorithme de hachage utilisé
    "-sign", "./Keys/PrivateKeys/my_sk.pem",  # Clé privée utilisée pour signer
    "./Keys/PublicKeys/pk_friend1.pem"        # Clé publique à signer
]

# Lancer la commande OpenSSL
result = subprocess.run(cmd, capture_output=True)

# Tester si le processus OpenSSL s’est terminé avec une erreur
if result.returncode != 0:
    print("Erreur lors de la signature :")
    print(result.stderr.decode(errors="ignore"))
    raise SystemExit(1)

with open("./Binary/sign_friend1.bin", "wb") as f:
    f.write(result.stdout)

# Convertir la signature binaire en hexadécimal
cmd = [
    "xxd",
    "-p",
    "./Binary/sign_friend1.bin"
]

# Lancer la commande OpenSSL
result = subprocess.run(cmd, capture_output=True, text=True)

# Tester si le processus OpenSSL s’est terminé avec une erreur
if result.returncode != 0:
    print("Erreur lors de la conversion en hexadécimal :")
    print(result.stderr)
    raise SystemExit(1)

# Retirer les retours à la ligne de la sortie
hex_content = result.stdout.replace("\n", "")

# # Écrire le résultat dans le fichier .hex
with open("./Hexa/sign_friend1.hex", "w", encoding="utf-8") as f:
    f.write(hex_content)

# Afficher la sortie
print(hex_content)