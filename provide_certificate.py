import subprocess
from pathlib import Path

# Produire un certificat pour la paire de clé RSA publique/privée
cmd = [
    "openssl", "req",                                       # Commande OpenSSL pour créer une requête de certificat
    "-new",                                                 # Demande la création d’une nouvelle CSR
    "-key", "./Keys/PrivateKeys/sk_atrium.pem",             # Clé privée dont on veut donner un certificat
    "-batch",                                               # Eviter les questions interactives
    "-subj", "/CN=AdrienPanguel",                           # Définir directement le sujet du certificat
    "-out", "./Certificates/certificate_atrium.csr.pem"     # Chemin du fichier de sortie
]

# Lancer la commande OpenSSL
result = subprocess.run(cmd, capture_output=True, text=True)

# Tester si le processus OpenSSL s’est terminé avec une erreur
if result.returncode != 0:
    print("Erreur lors de la génération de la CSR :")
    print(result.stderr)
    raise SystemExit(1)

print("CSR générée : ./Certificates/certificate_atrium.csr.pem")