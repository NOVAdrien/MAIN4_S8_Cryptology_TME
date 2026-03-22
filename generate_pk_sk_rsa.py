import subprocess

# Générer la clé privée RSA 2048 bits
cmd = [
    "openssl", "genpkey",                   # Commande OpenSSL pour générer une clé privée
    "-algorithm", "RSA",                    # La clé privée générée est de type RSA
    "-pkeyopt", "rsa_keygen_bits:2048",     # La clé RSA générée est de taille 2048 bits
    "-out", "./Keys/PrivateKeys/my_sk.pem"  # Fichier de sortie contenant la clé privée RSA générée
]

# Lancer la commande OpenSSL
result = subprocess.run(cmd, capture_output=True, text=True)

# Tester si le processus OpenSSL s’est terminé avec une erreur
if result.returncode != 0:
    print("Erreur lors de la génération de la clé privée :")
    print(result.stderr)
    raise SystemExit(1)

# Extraire la clé publique depuis la clé privée
cmd = [
    "openssl", "pkey",                          # Commande OpenSSL pour lire la clé privée et en sortir la partie publique
    "-in", "./Keys/PrivateKeys/my_sk.pem",      # Chemin vers la clé privée
    "-pubout",                                  # N’écrire que la clé publique mais pas la clé privée
    "-out", "./Keys/PublicKeys/my_pk.pem"       # Fichier de sortie contenant la clé publique RSA extraite de la clé privée
]

# Lancer la commande OpenSSL
result = subprocess.run(cmd, capture_output=True, text=True)

# Tester si le processus OpenSSL s’est terminé avec une erreur
if result.returncode != 0:
    print("Erreur lors de la génération de la clé publique :")
    print(result.stderr)
    raise SystemExit(1)

print("Clé privée générée : ./Keys/PrivateKeys/my_sk.pem")
print("Clé publique générée : ./Keys/PublicKeys/my_pk.pem")