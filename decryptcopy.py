# PrimaryFunctions/decrypt.py
import subprocess


class OpensslError(Exception):
    pass


def decrypt(ciphertext, passphrase, cipher="aes-128-cbc", decode_utf8=True, strict=False):
    """
    Déchiffre un ciphertext OpenSSL enc (base64 + pbkdf2).
    - ciphertext: str (base64, avec ou sans \\n) ou bytes
    - passphrase: str
    - cipher: ex "aes-128-cbc"
    - decode_utf8: si True, renvoie str sinon bytes
    - strict:
        False -> renvoie None si échec (pratique pour brute-force)
        True  -> lève OpensslError si échec (pratique pour usage "normal")
    """
    args = [
        "openssl", "enc",
        "-d", f"-{cipher}",
        "-base64",
        "-pbkdf2",
        "-pass", f"pass:{passphrase}",
        "-A"
    ]

    if isinstance(ciphertext, str):
        data = ciphertext.encode("utf-8")
    else:
        data = ciphertext

    result = subprocess.run(
        args,
        input=data,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    # échec OpenSSL (mauvais mdp, mauvais format, etc.)
    if result.returncode != 0:
        if strict:
            err = result.stderr.decode("utf-8", errors="replace").strip()
            raise OpensslError(err or "OpenSSL failed.")
        return None

    plaintext_bytes = result.stdout

    if not decode_utf8:
        return plaintext_bytes

    # succès OpenSSL mais bytes non UTF-8 (arrive souvent en brute-force CBC)
    try:
        return plaintext_bytes.decode("utf-8")
    except UnicodeDecodeError:
        if strict:
            raise OpensslError("Decryption produced non-UTF8 plaintext.")
        return None
    




    
CHALLENGE = "U2FsdGVkX1+nH9rYtEFp/PADwdT/aLalA/NT7FkPp2Rs7orZEpe9WpbDEfapMOiG\n"
TARGET = "trees lever trims loxes filly"

with open("ListKeys.txt", "r", encoding="utf-8", errors="ignore") as f:
    for i, line in enumerate(f):
        if i % 2000 == 0:
            print(f"Testé {i} mots")

        word = line.strip()
        if not word:
            continue

        out = decrypt(CHALLENGE, word)  # strict=False par défaut => None si échec
        if out is not None and out.strip() == TARGET:
            print("FOUND PASSWORD:", word)
            break