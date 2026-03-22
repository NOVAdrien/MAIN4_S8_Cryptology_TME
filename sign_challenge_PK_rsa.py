import subprocess

# Écrire le challenge dans un fichier texte
with open("./Texts/sign_challenge_PK.txt", "w", encoding="utf-8") as f:
    f.write("fader scrub chins divvy amass")

# Signer le fichier avec la clé publique RSA
cmd = [
    "openssl", "dgst",                          # Commande OpenSSL pour calculer un condensat et signer
    "-sha256",                                  # Utiliser SHA-256 comme fonction de hachage
    "-sign", "./Keys/PrivateKeys/my_sk.pem",    # Clé privée utilisée pour signer
    "-out", "./Binary/sign_challenge_PK.bin",   # Fichier de sortie contenant la signature binaire
    "./Texts/sign_challenge_PK.txt"             # Fichier contenant le message à signer
]

# Lancer la commande OpenSSL
result = subprocess.run(cmd, capture_output=True, text=True)

# Tester si le processus OpenSSL s’est terminé avec une erreur
if result.returncode != 0:
    print("Erreur lors de la signature :")
    print(result.stderr)
    raise SystemExit(1)

# Convertir la signature binaire en hexadécimal
cmd = [
    "xxd",
    "-p",
    "./Binary/sign_challenge_PK.bin"
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

# Écrire le résultat dans le fichier .hex
with open("./Hexa/sign_challenge_PK.hex", "w", encoding="utf-8") as f:
    f.write(hex_content)

# Afficher la sortie
print(hex_content)