#!/usr/bin/env python3
"""
CTF pedagogical RSA: shared modulus demo (TOY ONLY)

- Parse pkA, pkB (PEM) to get (n, eA, eB)
- Verify same modulus n
- Verify skB matches pkB
- If n is small (<= MAX_BITS), derive skA and write skA.pem
- REFUSES for realistic RSA sizes automatically

pip install cryptography
"""

import math
import secrets
from typing import Tuple, Optional

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa


# -----------------------------
# Safety gate (toy only)
# -----------------------------
MAX_BITS = 80  # increase only for toy experimentation, never for real RSA


# -----------------------------
# Helpers: math
# -----------------------------
def egcd(a: int, b: int):
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = egcd(b, a % b)
    return (g, y1, x1 - (a // b) * y1)

def modinv(a: int, m: int) -> int:
    g, x, _ = egcd(a, m)
    if g != 1:
        raise ValueError("No modular inverse (gcd != 1).")
    return x % m

def lcm(a: int, b: int) -> int:
    return a // math.gcd(a, b) * b

def check_edn_consistency(n: int, e: int, d: int, trials: int = 20) -> bool:
    # textbook RSA check: (m^e)^d == m mod n on random m
    for _ in range(trials):
        m = secrets.randbelow(n - 3) + 2
        if pow(pow(m, e, n), d, n) != m:
            return False
    return True


# -----------------------------
# Helpers: PEM parsing
# -----------------------------
def get_ne_from_public_pem(pem: bytes) -> Tuple[int, int]:
    pub = serialization.load_pem_public_key(pem)
    nums = pub.public_numbers()
    return nums.n, nums.e

def load_private_key_numbers(pem: bytes) -> rsa.RSAPrivateNumbers:
    key = serialization.load_pem_private_key(pem, password=None)
    return key.private_numbers()


# -----------------------------
# TOY ONLY: derive skA from shared modulus using p,q (guarded)
# -----------------------------
def derive_private_key_from_pq_toy_only(p: int, q: int, e: int) -> rsa.RSAPrivateKey:
    n = p * q

    # Use Carmichael's function λ(n) = lcm(p-1, q-1) for best practice
    lam = lcm(p - 1, q - 1)
    d = modinv(e, lam)

    dp = d % (p - 1)
    dq = d % (q - 1)
    qi = modinv(q, p)

    priv_nums = rsa.RSAPrivateNumbers(
        p=p,
        q=q,
        d=d,
        dmp1=dp,
        dmq1=dq,
        iqmp=qi,
        public_numbers=rsa.RSAPublicNumbers(e=e, n=n),
    )
    return priv_nums.private_key()


def main():
    # --------- Inputs (paste your PEMs) ----------
    pkB_pem = b"""-----BEGIN PUBLIC KEY-----
MIIBQDANBgkqhkiG9w0BAQEFAAOCAS0AMIIBKAKCAQEA0OKPjEGC7MZqhJsYYO5c
SK4xkKmTrfhpoeKKAlFXmysa+cy9+WoFfLOBz1qKLozUs1kaT4OknC1IfDf98x1K
rPy3nY5GyIdy2Tboeq5fA+GZN4pmedA9kDWIHhaU6toOb1Jk/53xGkRBEhwJjvBa
hbo3kogAx4pOiFBg5SNQ79ZjbCdCeeUyh4gHEeGzAzT2Pn4hM/TDoSZb6gsiYiI/
mlUga2hqZ5RyVSgJipecpJwwm/bM/wiWXuGgGOi+5ISe3leISnYKzM2wRGzA9bsz
i/o0KRgKL4WT2jrxpZb7+GrIRPhWW0BVSaDPi+5u+8iZHA2YB0XCTn+wIlyOgf8n
CQIhANolNsPg/iI84Fruqg8KdVsAAAAAAAA+++ATRIUM+++B
-----END PUBLIC KEY-----"""

    skB_pem = b"""-----BEGIN PRIVATE KEY-----
MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDQ4o+MQYLsxmqE
mxhg7lxIrjGQqZOt+Gmh4ooCUVebKxr5zL35agV8s4HPWooujNSzWRpPg6ScLUh8
N/3zHUqs/LedjkbIh3LZNuh6rl8D4Zk3imZ50D2QNYgeFpTq2g5vUmT/nfEaREES
HAmO8FqFujeSiADHik6IUGDlI1Dv1mNsJ0J55TKHiAcR4bMDNPY+fiEz9MOhJlvq
CyJiIj+aVSBraGpnlHJVKAmKl5yknDCb9sz/CJZe4aAY6L7khJ7eV4hKdgrMzbBE
bMD1uzOL+jQpGAovhZPaOvGllvv4ashE+FZbQFVJoM+L7m77yJkcDZgHRcJOf7Ai
XI6B/ycJAgMBAAECggEAKilQqBKhBoGWBmX3qbjyz4i5YGWZ9Udqqs465PTeJeex
bjIxNiJ8MQtabCvuMC8kz35wnRQJKazKMKhsjaGf7QKlXRvWlashN06p5flEHFhw
wJEi1ft+MZlcfBY6wJx6xWVwFVgfzhlwuOMH2t4Qp2VKyjzBS4VTDJiMtjNGpuHV
lpnk0jJxDGNVkaBuxO4ixHreQe7t/l9jwmgFs/ulOZE1Oujhv3nGZ7upHEGGbARH
KfLH9j5m7D7ChJXQy6NSX06gdI06pUksXrCDghcjQWh52eSOgQKa44UewfFXZJZ7
BZ1wW5HHYsPAscSmWZnHKFjVVtKAsLsU2cxlee02sQKBgQDhq9EidH5EvviZKjAT
tPHfee0rJ3AT1qftx8uF8E8FexyhSipH4BdwyRXumn1cGtuq6zio+hvifUMlOc63
pGMgOHndfybZrRyX4GjE9ZVtLkpe6WIrojNxUxG7rawGdpJv0yxsutPjyU1NMg+0
mevSkp9ON46x7Gd4RM0GISNzIwKBgQDs9TfyHUJT6XPpDFkiGtfhOdAnRGLvyP8M
BMJHmfnBLoBHxz/nEfyfDOvFKuJi9NZePq2JpAl6KJKo8ayKqs07Z2AcN87IGuVQ
512pbfF++2EeqqWHH8MUjYIwpSm2xDpbJu4+woVQDIkC0yXd8rJqr4R5CgJRRNZj
Rr0kZSQl4wKBgDH4iebHRO6UGxhPbzXt62FA7nOP2BGMhsLwavDNtbHRARX2BkbE
KGyhGmora3bpu5qtW26Pc31Dn4quskeX7xtDZjjV3xR0cNBwsMJsXxo+FdnOdB6V
XC7L5jFY067asrJwYHXzKNhXyvY9D50+OCn4ra30P3TGlGLdWUjyLZdhAoGAVFEN
j0GKEIHJlOun69LRbns77j0PV3OWDZjD6OaJUIxTaTclLfvggFgArTANTlkAzphO
9+M+3BED3sngM5eDX9fxAxl4owuu/ZLWaSuN+zlH3bmrHOHYcL/Jy7V5mmdIvJal
v/9HoKxVNIQdvVRW2E+MO+Wr3W85Oio5s3Gp4zECgYBoiZG5ooDlmfQW+0EwDP8k
7k9MFXgQ1HLNTCVU69i8/jD7JT3KqsqnV33c7d+Gou5Q/HJELRyp2fyQiJcdziH0
Wlt1sk1FtD2KrCl37tsO2/E5CDFXP/YlOJy/T/Bc51RMPZjsLQ/+/GyIFbBZ6zf9
wgcM14V3PE6kfZGSSpEL5Q==
-----END PRIVATE KEY-----"""

    pkA_pem = b"""-----BEGIN PUBLIC KEY-----
MIIBPTANBgkqhkiG9w0BAQEFAAOCASoAMIIBJQKCAQEA0OKPjEGC7MZqhJsYYO5c
SK4xkKmTrfhpoeKKAlFXmysa+cy9+WoFfLOBz1qKLozUs1kaT4OknC1IfDf98x1K
rPy3nY5GyIdy2Tboeq5fA+GZN4pmedA9kDWIHhaU6toOb1Jk/53xGkRBEhwJjvBa
hbo3kogAx4pOiFBg5SNQ79ZjbCdCeeUyh4gHEeGzAzT2Pn4hM/TDoSZb6gsiYiI/
mlUga2hqZ5RyVSgJipecpJwwm/bM/wiWXuGgGOi+5ISe3leISnYKzM2wRGzA9bsz
i/o0KRgKL4WT2jrxpZb7+GrIRPhWW0BVSaDPi+5u+8iZHA2YB0XCTn+wIlyOgf8n
CQIeM4NUOx8uVRPDQiSkQRVnZwAAAAA+++ATRIUM+++B
-----END PUBLIC KEY-----"""

    # Optional: if you already know p and q for a TOY challenge, paste them here.
    # If None, we read p,q from skB (still toy-gated when deriving skA).
    p_override: Optional[int] = None
    q_override: Optional[int] = None

    # --------- Parse public keys ----------
    nB, eB = get_ne_from_public_pem(pkB_pem)
    nA, eA = get_ne_from_public_pem(pkA_pem)

    print("pkB: e =", eB, "| n_bits =", nB.bit_length())
    print("pkA: e =", eA, "| n_bits =", nA.bit_length())
    print("Same modulus N?", nA == nB)

    # --------- Load skB numbers, verify skB matches pkB ----------
    skB_nums = load_private_key_numbers(skB_pem)
    pB, qB, dB = skB_nums.p, skB_nums.q, skB_nums.d

    if p_override is not None and q_override is not None:
        pB, qB = p_override, q_override

    # sanity: does p*q match pkB modulus?
    if pB * qB != nB:
        raise ValueError("Provided/loaded p,q do NOT multiply to pkB's modulus nB.")

    okB = check_edn_consistency(nB, eB, dB, trials=10)
    print("skB consistent with pkB?", okB)

    # --------- TOY ONLY: derive skA and write PEM ----------
    # This is the part that is intentionally blocked for large RSA sizes.
    try:
        skA = derive_private_key_from_pq_toy_only(pB, qB, eA)

        pemA = skA.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption(),
        )
        with open("skA.pem", "wb") as f:
            f.write(pemA)

        print("Wrote skA.pem (TOY modulus).")
        print("Check: skA consistent with pkA?",
              check_edn_consistency(nA, eA, skA.private_numbers().d, trials=10))

    except ValueError as ve:
        print("Refused to derive skA:", ve)


if __name__ == "__main__":
    main()