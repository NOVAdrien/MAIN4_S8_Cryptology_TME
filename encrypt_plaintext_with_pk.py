import subprocess

# Écrire le message dans un fichier texte
with open("./Texts/msg_pki_tutorial.txt", "w", encoding="utf-8") as f:
    f.write("I got it!")

# Chiffrer ce message avec la clé publique
cmd = [
    "openssl", "pkeyutl",                               # Commande OpenSSL pour opérations sur clés publiques/privées
    "-encrypt",                                         # Je veux chiffrer
    "-pubin",                                           # La clé fournie est une clé publique
    "-inkey", "./Keys/PublicKeys/pk_pki_tutorial.pem",  # Chemin vers la clé publique
    "-in", "./Texts/msg_pki_tutorial.txt",              # Fichier contenant le message en clair
    "-out", "./Binary/msg_pki_tutorial.bin"             # Fichier de sortie contenant le ciphertext binaire
]

# Lancer la commande OpenSSL
result = subprocess.run(cmd, capture_output=True, text=True)

# Tester si le processus OpenSSL s’est terminé avec une erreur
if result.returncode != 0:
    print("Erreur OpenSSL :")
    print(result.stderr)
    raise SystemExit(1)

# Convertir en hexadécimal
cmd = [
    "xxd",
    "-p",
    "./Binary/msg_pki_tutorial.bin"
]

# Lancer la commande OpenSSL
result = subprocess.run(cmd, capture_output=True, text=True)

# Tester si le processus OpenSSL s’est terminé avec une erreur
if result.returncode != 0:
    print("Erreur xxd :")
    print(result.stderr)
    raise SystemExit(1)

# Retirer les retours à la ligne
hex_content = result.stdout.replace("\n", "")

# Sauvegarder la sortie dans un fichier .hex
with open("./Hexa/msg_pki_tutorial.hex", "w", encoding="utf-8") as f:
    f.write(hex_content)

# Afficher la sortie
print(hex_content)