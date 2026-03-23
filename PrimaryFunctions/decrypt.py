import subprocess

class OpensslError(Exception):
    pass

def decrypt(ciphertext, passphrase, cipher = "aes-128-cbc", decode_utf8 = True, strict = False):

    # Commande OpenSSL
    cmd = [
        "openssl", "enc",                # Commande OpenSSL pour le chiffrement/déchiffrement symétrique
        "-d", f"-{cipher}",              # Mode de déchiffrement (déchiffrage) et choix du type de chiffrement (aes-128-cbc)
        "-base64",                       # L’entrée est fournie en type base64
        "-pbkdf2",                       # Utiliser la fonction de dérivation de clé PBKDF2 pour dériver la clé à partir de la passphrase
        "-pass", f"pass:{passphrase}",   # Transmet la passphrase à OpenSSL
        "-A"                             # Traiter le base64 comme une seule ligne
    ]

    # Conversion du ciphertext de chaîne str en octets avec l'encodage UTF-8
    if isinstance(ciphertext, str):
        ciphertext = ciphertext.encode("utf-8")

    # Lancer la commande OpenSSL
    result = subprocess.run(
        cmd,
        input = ciphertext,
        stdout = subprocess.PIPE,     # Capture la sortie standard dans result.stdout
        stderr = subprocess.PIPE      # Capture la sortie d’erreur dans result.stderr
    )

    # Tester si le processus OpenSSL s’est terminé avec une erreur
    if result.returncode != 0:
        # En mode strict, on lève une exception ; sinon on renvoie None
        if strict:
            # Récupèrer le message d’erreur produit par OpenSSL
            err = result.stderr.decode("utf-8", errors="replace").strip()
            raise OpensslError(err or "OpenSSL failed.")
        return None

    # Stocker la sortie standard qui contient le plaintext sous forme d’octets
    plaintext_bytes = result.stdout

    # Vérifier si l’utilisateur veut récupérer les octets bruts ou une chaîne str
    if not decode_utf8:
        return plaintext_bytes

    # Décoder les octets du plaintext d'octets à une chaîne str avec l'encodage UTF-8
    try:
        return plaintext_bytes.decode("utf-8")
    except UnicodeDecodeError:
        # Vraie erreur ou juste un "None"
        if strict:
            raise OpensslError("Decryption produced non-UTF8 plaintext.")
        return None