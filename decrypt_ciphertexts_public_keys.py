#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import re
from typing import Tuple


# ============================
# DONNÉES
# ============================

YMOLINA_PEM = b"""-----BEGIN PUBLIC KEY-----
MIIBPTANBgkqhkiG9w0BAQEFAAOCASoAMIIBJQKCAQEArGseb911v/OWCUFFgM3G
1IJN9DaXLnbNt/wB/Y+OSIIdhuHc0fXMr8F9gZalkUc+KKyh9Ha+R6DD4OngiPik
rNMWIXGx92gHQZCH/+W2+hgAN8xwPYXaYsUK/FCQU//M5aTkVtLJQMO5355TubJ6
J+x51y0K54ezfuENoEcpK8C+rI8Qr0ju6F2Hs7gmV+XAVThz7Bg/ZlkrnDKDxDhA
l28x9EaWvbVmLK0ZAkWQBmWaOF3RIyIoFC6YWytOapNYXsIUae3EyFOeU2fSSjkG
Qv6AGwLdHqWDmaQt/uWpQMGYSkJi9ImEVsdNtE7OYwaTfXSdeSDlE6JOfrYLy14U
2wIeeAWSlTXUlpaMc8oziaLZzQAAAAA+++ATRIUM+++B
-----END PUBLIC KEY-----"""

JILLIAN_PEM = b"""-----BEGIN PUBLIC KEY-----
MIIBPTANBgkqhkiG9w0BAQEFAAOCASoAMIIBJQKCAQEArGseb911v/OWCUFFgM3G
1IJN9DaXLnbNt/wB/Y+OSIIdhuHc0fXMr8F9gZalkUc+KKyh9Ha+R6DD4OngiPik
rNMWIXGx92gHQZCH/+W2+hgAN8xwPYXaYsUK/FCQU//M5aTkVtLJQMO5355TubJ6
J+x51y0K54ezfuENoEcpK8C+rI8Qr0ju6F2Hs7gmV+XAVThz7Bg/ZlkrnDKDxDhA
l28x9EaWvbVmLK0ZAkWQBmWaOF3RIyIoFC6YWytOapNYXsIUae3EyFOeU2fSSjkG
Qv6AGwLdHqWDmaQt/uWpQMGYSkJi9ImEVsdNtE7OYwaTfXSdeSDlE6JOfrYLy14U
2wIeEHF4fObeyNHi52X48UNQQQAAAAA+++ATRIUM+++B
-----END PUBLIC KEY-----"""

C_YMOLINA_HEX = "73abb97126b99496e5146a51ef470c81a1ad2c72f6542c1081306c1bffc8a3fafdfbdec88eaaa9aa43d7a523d68d9e7b84ec317f46163e87ad263721c64b0f5cdeb7da2948a0de56a15200ea36a825b014c2723fe7f789be108294a1e3dd319b512dd284a21583336666eae21d5da7648c71e98dfc75dd3eefdbf790a7334cdbc741cc0d6a3128b23d6bb2981baff723cbb5f7d22816961cc13e4bec22ea22b018cedf8ae8ab3ba93a5a63f7c10ed3536e01b7e05405d3e35b9e5bb14deed8e65bc4919df7613324321dc2de11bd4663879c93f653d2f2db06bdbe512834a00bbae6aef0bff14790a4a56a955a2fcca1e5de36ec281012da04db89f82f2aa420"
C_JILLIAN_HEX = "3ecf827250c63d9086bc1b008c4b3a306b5ae0380168537841f878f947022b61b8252f91309558577466c0d81fc93b6d755eb2a0128ddd74dadf0df86e8b548687fc8f889103a79400cc982214329eaf0d2182dc05380f84dd2033979cbd1e195c04137bc76cabc82b1fd25303a0d1eca9ae1a3ace40cab284692fb4b91af78e79a88b28fa834a27d7a8abab524be72429cd8a46bf5b4e46e86cc78d16fd12c5ef027bed9e2719dec9bdfd43ab7315792d726e82c50981833cfa9741abf8611982a2f31ea0bd1043b1f5514c2f42dde4c2e8a996a6d2450d19c5c9672d7abbda5cf2515038ce46450deb9bf01f0914ffb918c4f93bb6347de4517c4d4f8aa5d9"

OUT_FILE = "./Texts/digicode.txt"

# ============================
# UTILS
# ============================

def hex_to_int(h: str) -> int:
    return int(h, 16)

def egcd(a: int, b: int) -> Tuple[int, int, int]:
    x0, y0 = 1, 0
    x1, y1 = 0, 1
    while b != 0:
        q = a // b
        a, b = b, a - q * b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def modinv(a: int, m: int) -> int:
    g, x, _ = egcd(a, m)
    if g != 1:
        raise ValueError("No modular inverse")
    return x % m

def load_pubkey_numbers(pem: bytes):
    try:
        from cryptography.hazmat.primitives import serialization
        pub = serialization.load_pem_public_key(pem)
        nums = pub.public_numbers()
        return int(nums.n), int(nums.e)
    except Exception:
        from Crypto.PublicKey import RSA
        key = RSA.import_key(pem)
        return int(key.n), int(key.e)

# ============================
# MAIN
# ============================

def main():

    n1, e1 = load_pubkey_numbers(YMOLINA_PEM)
    n2, e2 = load_pubkey_numbers(JILLIAN_PEM)

    c1 = hex_to_int(C_YMOLINA_HEX)
    c2 = hex_to_int(C_JILLIAN_HEX)

    # affichage terminal minimal
    print("n_bits =", n1.bit_length())
    print("e1 =", e1)
    print("e2 =", e2)

    if n1 != n2 or math.gcd(e1, e2) != 1:
        raise SystemExit("Not common modulus case.")

    # Common modulus attack
    g, a, b = egcd(e1, e2)

    def mod_pow_signed(base, exp, mod):
        if exp >= 0:
            return pow(base, exp, mod)
        inv = modinv(base % mod, mod)
        return pow(inv, -exp, mod)

    m = (mod_pow_signed(c1, a, n1) * mod_pow_signed(c2, b, n1)) % n1
    pt = m.to_bytes((m.bit_length() + 7) // 8, "big")

    text = pt.decode(errors="ignore")

    match = re.search(r"Nouveau digicode de la salle RC-25\s*:\s*([0-9a-fA-F]+)", text)
    if not match:
        raise SystemExit("Digicode not found.")

    code = match.group(1)

    print("DIGICODE =", code)

    # fichier ne contient QUE le digicode
    with open(OUT_FILE, "w") as f:
        f.write(code)


if __name__ == "__main__":
    main()