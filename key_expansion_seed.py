#!/usr/bin/env python3
import base64
import hashlib
import subprocess
import sys

IV_HEX_TARGET = "96c2089c5c89644420794597e1eba19b"

CIPHERTEXT_B64 = r"""
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
""".strip()

def key_expansion(seed: bytes) -> bytes:
    state = seed
    out = b""
    for _ in range(8):
        state = hashlib.sha256(state).digest()
        out += state[:4]
    return out  # 32 bytes

def openssl_decrypt_aes128cbc(cipher_bytes: bytes, key_hex: str, iv_hex: str) -> bytes | None:
    # On suppose : AES-128-CBC + IV explicite + base64 (pas pbkdf2, pas "Salted__")
    # Ici on passe des bytes *déjà décodés base64* à OpenSSL (donc pas -base64).
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
    # Heuristiques simples : imprimable / UTF-8 / présence de mots
    try:
        s = pt.decode("utf-8")
    except UnicodeDecodeError:
        return False
    if any(x in s for x in ["FLAG", "flag", "digicode", "Uglix", "UGLIX", "{", "}"]):
        return True
    # sinon, au moins éviter du binaire total
    printable_ratio = sum(32 <= c < 127 or c in (10, 13, 9) for c in pt) / max(1, len(pt))
    return printable_ratio > 0.90

def main():
    # base64 -> bytes
    cipher_bytes = base64.b64decode("".join(CIPHERTEXT_B64.split()))
    iv_target = bytes.fromhex(IV_HEX_TARGET)

    hit = None
    for x in range(65536):
        seed = x.to_bytes(2, "big")  # ou "little" si nécessaire (voir note plus bas)
        km = key_expansion(seed)
        K = km[:16]
        IV = km[16:32]
        if IV == iv_target:
            hit = (x, K.hex(), IV.hex())
            break

    if not hit:
        print("[!] Aucun match IV trouvé en big-endian. Tentative little-endian…", file=sys.stderr)
        for x in range(65536):
            seed = x.to_bytes(2, "little")
            km = key_expansion(seed)
            K = km[:16]
            IV = km[16:32]
            if IV == iv_target:
                hit = (x, K.hex(), IV.hex())
                break

    if not hit:
        print("[!] Toujours aucun match: IV cible peut-être faux / spec différente.", file=sys.stderr)
        sys.exit(1)

    seed_int, key_hex, iv_hex = hit
    print(f"[+] Seed trouvée: {seed_int} (0x{seed_int:04x})")
    print(f"[+] K  = {key_hex}")
    print(f"[+] IV = {iv_hex}")

    pt = openssl_decrypt_aes128cbc(cipher_bytes, key_hex, iv_hex)
    if pt is None:
        print("[!] Déchiffrement OpenSSL a échoué. Peut-être padding/format différent.", file=sys.stderr)
        sys.exit(2)

    # Sauvegarde + affichage
    with open("./Texts/key_expansion_seed.txt", "wb") as f:
        f.write(pt)

    if looks_plausible(pt):
        print("[+] Plaintext plausible (UTF-8) :\n")
        print(pt.decode("utf-8", errors="replace"))
    else:
        print("[*] Plaintext écrit dans plaintext.bin (pas clairement UTF-8).")

if __name__ == "__main__":
    main()