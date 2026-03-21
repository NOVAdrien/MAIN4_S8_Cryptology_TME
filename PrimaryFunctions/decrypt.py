import subprocess

class OpensslError(Exception):
    pass

def decrypt(ciphertext, passphrase, cipher="aes-128-cbc", decode_utf8=True, strict=False):
    """
    Déchiffrer un ciphertext OpenSSL.
    - ciphertext: le texte chiffré à déchiffrer (type str ou bytes)
    - passphrase: la phrase de passe utilisée pour dériver la clé (type: str)
    - cipher: l’algorithme de chiffrement à utiliser (par défaut "aes-128-cbc")
    - decode_utf8: si le résultat doit être converti en chaîne UTF-8 (True) ou en bytes (False)
    - strict: si True, lève OpensslError en cas d’échec ; sinon renvoie None
    """
    args = [
        "openssl", "enc",                   # Sous-commande OpenSSL pour le chiffrement/déchiffrement symétrique
        "-d", f"-{cipher}",                 # Mode de déchiffrement et choix du chiffrement
        "-base64",                          # L’entrée est fournie en base64
        "-pbkdf2",                          # Utiliser PBKDF2 pour dériver la clé à partir de la passphrase
        "-pass", f"pass:{passphrase}",      # Transmet la passphrase à OpenSSL
        "-A"                                # Traiter le base64 comme une seule ligne, pour éviter des problèmes avec les retours à la ligne
    ]

    # Conversion du ciphertext de chaîne str en octets avec l'encodage UTF-8
    if isinstance(ciphertext, str):
        ciphertext = ciphertext.encode("utf-8")

    # Lancer la commande OpenSSL
    result = subprocess.run(
        args,
        input=ciphertext,
        stdout=subprocess.PIPE,     # Capture la sortie standard dans result.stdout
        stderr=subprocess.PIPE      # Capture la sortie d’erreur dans result.stderr
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

    # Décoder les octets du plaintext en chaîne str
    try:
        return plaintext_bytes.decode("utf-8")
    except UnicodeDecodeError:
        # Vraie erreur ou juste un "None"
        if strict:
            raise OpensslError("Decryption produced non-UTF8 plaintext.")
        return None