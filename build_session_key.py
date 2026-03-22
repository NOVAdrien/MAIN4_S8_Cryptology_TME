import subprocess
from pathlib import Path

# Texte à chiffrer
plaintext = "AdrienPanguel123"

# Chiffrer ce Plaintext avec la clé publique pour obtenir la session-key
cmd = [
    "openssl", "pkeyutl",                               # Commande OpenSSL pour chiffrer
    "-encrypt",                                         # Choix de chiffrer
    "-pubin",                                           # Dire que la clé fournie est la clé publique
    "-inkey", "./Keys/PublicKeys/pk_broadcast.pem"      # Clé publique utilisée pour chiffrer
]

# Lancer la commande OpenSSL
result = subprocess.run(cmd, input=plaintext, capture_output=True, text=True)

# Tester si le processus OpenSSL s’est terminé avec une erreur
if result.returncode != 0:
    print("Erreur lors du chiffrement :")
    print(result.stderr)
    raise SystemExit(1)

cipher_bin = result.stdout.encode("latin1")

# Convertir le binaire en hexadécimal avec xxd -p
cmd = [
    "xxd",
    "-p"
]

# Lancer la commande OpenSSL
result = subprocess.run(cmd, input=cipher_bin, capture_output=True)

# Tester si le processus OpenSSL s’est terminé avec une erreur
if result.returncode != 0:
    print("Erreur lors de la conversion en hexadécimal :")
    print(result.stderr.decode(errors="ignore"))
    raise SystemExit(1)

# Supprimer les retours à la ligne dans la sortie
hex_content = result.stdout.decode().replace("\n", "").replace(" ", "")

# Écrire la sortie dans un fichier .pem
with open("./Keys/session_key.pem", "w", encoding="utf-8") as f:
    f.write(hex_content)

# Afficher la sortie
print(hex_content)