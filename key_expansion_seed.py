#!/usr/bin/env python3
import base64
import hashlib
import subprocess
import sys
import os

# --- Configuration ---
IV_HEX_TARGET = "96c2089c5c89644420794597e1eba19b"

# Chemin vers le fichier contenant le bloc Base64
CIPHER_FILE_PATH = "./Texts/ciphertext_key_expansion_seed.txt" 

def key_expansion(seed: bytes) -> bytes:
    state = seed
    out = b""
    for _ in range(8):
        state = hashlib.sha256(state).digest()
        out += state[:4]
    return out  # 32 bytes

def openssl_decrypt_aes128cbc(cipher_bytes: bytes, key_hex: str, iv_hex: str) -> bytes | None:
    cmd = [
        "openssl", "enc", "-d", "-aes-128-cbc",
        "-K", key_hex,
        "-iv", iv_hex,
    ]
    p = subprocess.run(cmd, input=cipher_bytes, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if p.returncode != 0:
        return None
    return p.stdout

def looks_plausible(pt: bytes) -> bool:
    try:
        s = pt.decode("utf-8")
    except UnicodeDecodeError:
        return False
    # Heuristiques de succès
    keywords = ["FLAG", "flag", "digicode", "Uglix", "UGLIX", "{", "}"]
    if any(x in s for x in keywords):
        return True
    printable_ratio = sum(32 <= c < 127 or c in (10, 13, 9) for c in pt) / max(1, len(pt))
    return printable_ratio > 0.90

def main():
    # 1) Récupération du ciphertext depuis le fichier
    if not os.path.exists(CIPHER_FILE_PATH):
        print(f"[!] Erreur : Le fichier {CIPHER_FILE_PATH} est introuvable.", file=sys.stderr)
        sys.exit(1)

    with open(CIPHER_FILE_PATH, "r") as f:
        raw_content = f.read()

    # Nettoyage : on enlève les espaces et retours à la ligne pour le Base64
    clean_b64 = "".join(raw_content.split())
    
    try:
        cipher_bytes = base64.b64decode(clean_b64)
    except Exception as e:
        print(f"[!] Erreur lors du décodage Base64 : {e}", file=sys.stderr)
        sys.exit(1)

    iv_target = bytes.fromhex(IV_HEX_TARGET)

    # 2) Recherche de la Seed
    hit = None
    for endianness in ["big", "little"]:
        for x in range(65536):
            seed = x.to_bytes(2, endianness)
            km = key_expansion(seed)
            K = km[:16]
            IV = km[16:32]
            if IV == iv_target:
                hit = (x, K.hex(), IV.hex(), endianness)
                break
        if hit: break

    if not hit:
        print("[!] Aucun match IV trouvé.", file=sys.stderr)
        sys.exit(1)

    seed_int, key_hex, iv_hex, endi = hit
    print(f"[+] Seed trouvée: {seed_int} (0x{seed_int:04x}) en {endi}-endian")
    print(f"[+] K  = {key_hex}")
    print(f"[+] IV = {iv_hex}")

    # 3) Déchiffrement
    pt = openssl_decrypt_aes128cbc(cipher_bytes, key_hex, iv_hex)
    if pt is None:
        print("[!] Déchiffrement OpenSSL échoué.", file=sys.stderr)
        sys.exit(2)

    # Sauvegarde du résultat
    output_path = "./Texts/key_expansion_seedTEST.txt"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "wb") as f:
        f.write(pt)

    if looks_plausible(pt):
        print("[+] Plaintext plausible :\n")
        print(pt.decode("utf-8", errors="replace"))
    else:
        print(f"[*] Plaintext écrit dans {output_path} (binaire ou non UTF-8).")

if __name__ == "__main__":
    main()