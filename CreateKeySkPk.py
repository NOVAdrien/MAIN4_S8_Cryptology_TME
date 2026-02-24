import base64
import subprocess
from pathlib import Path

TARGET = b"+++ATRIUM+++"

print("On commence par decoder +++ATRIUM+++ en base64...")
atrium_b64_dec = base64.b64decode(TARGET)

# Ajout d'un octet pour éviter un exposant pair (idée)
atrium_b64_dec += b"\x01"
print("Octets obtenus:", atrium_b64_dec)

print("On convertit en int...")
atrium_int = int.from_bytes(atrium_b64_dec, byteorder="big") + (256 * 10**100)
print("e =", atrium_int)

# Dossier de sortie (attention aux espaces)
out_dir = Path("Pieces") / "Niveau_SB" / "Atrium" / "Bureau SB"
out_dir.mkdir(parents=True, exist_ok=True)

sk_path = out_dir / "sk_atrium.pem"
pk_path = out_dir / "pk_atrium.pem"

print("Génération de la clé privée avec OpenSSL...")
cmd_keygen = [
    "openssl", "genpkey",
    "-algorithm", "RSA",
    "-out", str(sk_path),
    "-outform", "PEM",
    "-pkeyopt", f"rsa_keygen_pubexp:{atrium_int}",
    "-pkeyopt", "rsa_keygen_bits:2048",
    "-pkeyopt", "rsa_keygen_primes:2",
]

keygen_run = subprocess.run(cmd_keygen, capture_output=True, text=True)
print("returncode:", keygen_run.returncode)
print("STDERR:", keygen_run.stderr)
print("STDOUT:", keygen_run.stdout)

if keygen_run.returncode != 0:
    raise SystemExit("OpenSSL genpkey a échoué (voir STDERR ci-dessus).")

print("Extraction de la clé publique...")
cmd_pubout = [
    "openssl", "pkey",
    "-in", str(sk_path),
    "-pubout",
    "-out", str(pk_path),
]

pub_run = subprocess.run(cmd_pubout, capture_output=True, text=True)
print("returncode:", pub_run.returncode)
print("STDERR:", pub_run.stderr)
print("STDOUT:", pub_run.stdout)

if pub_run.returncode != 0:
    raise SystemExit("OpenSSL pkey -pubout a échoué (voir STDERR ci-dessus).")

print("OK. Clé privée :", sk_path)
print("OK. Clé publique:", pk_path)
