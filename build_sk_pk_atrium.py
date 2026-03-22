import base64
import subprocess
from pathlib import Path

TARGET = b"+++ATRIUM+++"

sk_path = Path("./Keys/PrivateKeys/sk_atrium.pem")
pk_path = Path("./Keys/PublicKeys/pk_atrium.pem")

# Décoder la cible de Base64 vers des octets binaires
print("On commence par decoder +++ATRIUM+++ en base64...")
atrium_b64_dec = base64.b64decode(TARGET)

# Forcer un exposant impair en ajoutant l’octet b"\x01"
atrium_b64_dec += b"\x01"
print("Octets obtenus:", atrium_b64_dec)

# Convertir les octets en entier pour en faire l’exposant RSA et y ajouter un très grand nombre pour gonfler la valeur finale
print("On convertit en int...")
atrium_int = int.from_bytes(atrium_b64_dec, byteorder="big") + (256 * 10**100)
print("e =", atrium_int)

print("Génération de la clé privée avec OpenSSL...")
cmd_keygen = [
    "openssl", "genpkey",                           # Commande OpenSSL pour générer une clé privée
    "-algorithm", "RSA",                            # La clé privée générée est de type RSA
    "-out", str(sk_path),                           # Fichier de sortie de la clé privée
    "-outform", "PEM",                              # Format PEM:fichier texte encadré par des lignes "-----BEGIN ...-----".
    "-pkeyopt", f"rsa_keygen_pubexp:{atrium_int}",  # Définit l’exposant public RSA e à la valeur cible.
    "-pkeyopt", "rsa_keygen_bits:2048",             # La clé RSA générée est de taille 2048 bits
    "-pkeyopt", "rsa_keygen_primes:2",              # Demande une RSA classique à deux nombres premiers p et q.
]

# Lancer la commande OpenSSL
keygen_run = subprocess.run(cmd_keygen, capture_output=True, text=True)

print("returncode:", keygen_run.returncode)
print("STDERR:", keygen_run.stderr)
print("STDOUT:", keygen_run.stdout)

# Tester si le processus OpenSSL s’est terminé avec une erreur
if keygen_run.returncode != 0:
    raise SystemExit("OpenSSL genpkey a échoué (voir STDERR ci-dessus).")

print("Extraction de la clé publique...")
cmd_pubout = [
    "openssl", "pkey",      # Commande OpenSSL pour lire la clé privée et en sortir la partie publique
    "-in", str(sk_path),    # Chemin vers la clé privée
    "-pubout",              # N’écrire que la clé publique mais pas la clé privée
    "-out", str(pk_path),   # Fichier de sortie contenant la clé publique RSA extraite de la clé privée
]

# Lancer la commande OpenSSL
pub_run = subprocess.run(cmd_pubout, capture_output=True, text=True)

print("returncode:", pub_run.returncode)
print("STDERR:", pub_run.stderr)
print("STDOUT:", pub_run.stdout)

# Tester si le processus OpenSSL s’est terminé avec une erreur
if pub_run.returncode != 0:
    raise SystemExit("OpenSSL pkey -pubout a échoué (voir STDERR ci-dessus).")

print("OK. Clé privée :", sk_path)
print("OK. Clé publique:", pk_path)

print("\nVérification de la présence de la chaîne dans la clé publique...")

pem_text = pk_path.read_text()

# Extraire uniquement la partie Base64
lines = pem_text.splitlines()
b64_data = "".join(line for line in lines if "-----" not in line)

# Vérifier si la chaîne "+++Atrium+++" apparaît bien dans la clé publique
if TARGET.decode() in b64_data:
    print("La chaîne +++ATRIUM+++ est bien présente dans le Base64 du PEM.")
else:
    print("La chaîne n'apparaît PAS dans le Base64 du PEM.")