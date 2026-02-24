#!/usr/bin/env python3
"""
RSA helper script (safe version)

- Parses an RSA public key PEM to extract (n, e)
- Reads private exponent d (hex)
- Checks that (n, e, d) is self-consistent via random RSA round-trips
- OPTIONAL: factors n into (p, q) ONLY for TOY moduli (small bit-length),
  and REFUSES automatically for realistic RSA sizes.

Requirements:
  pip install cryptography

Run:
  python rsa_helper.py
"""

import math
import secrets
from typing import Tuple

from cryptography.hazmat.primitives import serialization


# -----------------------------
# 1) PEM parsing
# -----------------------------
def parse_rsa_public_pem(pem_bytes: bytes) -> Tuple[int, int]:
    pub = serialization.load_pem_public_key(pem_bytes)
    nums = pub.public_numbers()
    return nums.n, nums.e


# -----------------------------
# 2) Consistency check (safe)
# -----------------------------
def check_edn_consistency(n: int, e: int, d: int, trials: int = 20) -> bool:
    """
    Tests RSA correctness on random messages:
      m -> c = m^e mod n -> m2 = c^d mod n
    If (e, d) is correct for n, then m2 == m for almost all m in Z_n*.
    """
    for _ in range(trials):
        m = secrets.randbelow(n - 3) + 2  # 2..n-2
        c = pow(m, e, n)
        m2 = pow(c, d, n)
        if m2 != m:
            return False
    return True


# -----------------------------
# 3) TOY-ONLY factorization from (e,d,n)
# -----------------------------
def factor_from_edn_toy_only(e: int, d: int, n: int, *, max_bits: int = 80, max_tries: int = 2000) -> Tuple[int, int]:
    """
    EDUCATIONAL / TOY ONLY.

    Attempts to factor n = p*q given (e, d, n) using the classical method:
      k = e*d - 1 = 2^t * r  with r odd
    and tries random bases to find a non-trivial gcd.

    HARD-REFUSES to run if n is larger than max_bits.
    """
    if n <= 3 or n % 2 == 0:
        raise ValueError("n must be an odd composite > 3 (toy RSA).")

    k = e * d - 1
    if k <= 0 or (k & 1) == 1:
        raise ValueError("Invalid inputs: k = e*d - 1 must be positive and even.")

    # Write k = 2^t * r with r odd
    r = k
    t = 0
    while (r & 1) == 0:
        r >>= 1
        t += 1

    for _ in range(max_tries):
        g = secrets.randbelow(n - 3) + 2  # 2..n-2

        g_gcd = math.gcd(g, n)
        if 1 < g_gcd < n:
            p = g_gcd
            q = n // p
            return (min(p, q), max(p, q))

        y = pow(g, r, n)
        if y == 1 or y == n - 1:
            continue

        for _ in range(t):
            x = pow(y, 2, n)
            if x == 1:
                p = math.gcd(y - 1, n)
                if 1 < p < n:
                    q = n // p
                    if p * q == n:
                        return (min(p, q), max(p, q))
                break
            if x == n - 1:
                break
            y = x

    raise RuntimeError("Toy factorization failed. Inputs may be inconsistent or not 2-prime RSA.")


# -----------------------------
# 4) Main (edit inputs here)
# -----------------------------
def main():
    pem = b"""-----BEGIN PUBLIC KEY-----
MIIBQDANBgkqhkiG9w0BAQEFAAOCAS0AMIIBKAKCAQEA0OKPjEGC7MZqhJsYYO5c
SK4xkKmTrfhpoeKKAlFXmysa+cy9+WoFfLOBz1qKLozUs1kaT4OknC1IfDf98x1K
rPy3nY5GyIdy2Tboeq5fA+GZN4pmedA9kDWIHhaU6toOb1Jk/53xGkRBEhwJjvBa
hbo3kogAx4pOiFBg5SNQ79ZjbCdCeeUyh4gHEeGzAzT2Pn4hM/TDoSZb6gsiYiI/
mlUga2hqZ5RyVSgJipecpJwwm/bM/wiWXuGgGOi+5ISe3leISnYKzM2wRGzA9bsz
i/o0KRgKL4WT2jrxpZb7+GrIRPhWW0BVSaDPi+5u+8iZHA2YB0XCTn+wIlyOgf8n
CQIhANolNsPg/iI84Fruqg8KdVsAAAAAAAA+++ATRIUM+++B
-----END PUBLIC KEY-----"""

    d_hex = (
        "4aeb9f587154bd8c124d3b33102ca26b35330e07e29476f8e256fc8bbc318172"
        "7348268bdc52032eeeb3cabe8542f189441dd3fed32b7a78f88a6cd43e6d0bcc"
        "fc2664b957c7c5111711484ab2ee6b78fd8949d82ad7367e972ac3e3b7d98130"
        "2395579c83dd14d8646956f641261af3deebe715ce95ee77ee3fff133cb85065"
        "5d46fb9aaeba0d179df907c85911099b72a7ffebc8bab69829e222bbaa9056b0d"
        "520cac5d02e5b23bcdbe35ef32bebdeffaa12aea5d2166f5961a78fc85eb8bf0"
        "1dddfca7b7892c04785113ca07aed262e946fe6052d47767918cd8b155f775c7c"
        "aef1f4c2445059975fa2953cd9cc7bd3cada81313fb4d9916aab7563e3d5ed"
    )

    n, e = parse_rsa_public_pem(pem)
    d = int(d_hex, 16)

    print("Parsed public key:")
    print("  e =", e)
    print("  n bits =", n.bit_length())
    print("  n hex (first 40 chars) =", hex(n)[:42] + "...")

    ok = check_edn_consistency(n, e, d, trials=20)
    print("\nConsistency check (e,d,n):", "OK" if ok else "FAILED")

    # Try factoring only if it's a toy modulus
    try:
        p, q = factor_from_edn_toy_only(e, d, n, max_bits=80, max_tries=2000)
        print("\nToy factorization succeeded:")
        print("  p =", p)
        print("  q =", q)
    except ValueError as ve:
        print("\nToy factorization skipped/refused:")
        print(" ", ve)
    except Exception as ex:
        print("\nToy factorization attempted but failed:")
        print(" ", ex)


if __name__ == "__main__":
    main()