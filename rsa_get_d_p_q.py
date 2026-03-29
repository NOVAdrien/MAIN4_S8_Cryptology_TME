import math
import sys

sys.setrecursionlimit(10000)

n = """
bd:25:d2:42:8f:50:64:ef:84:11:a2:8b:fb:c8:d3:5a
37:2e:e3:20:86:e3:69:83:ec:09:ac:35:c9:2b:fd:4e
48:9b:ef:b3:14:81:aa:67:32:b3:3c:a9:09:f9:81:9c
41:0f:18:57:c0:64:c0:c3:7b:bc:cb:9d:9d:38:46:a2
77:c5:84:35:db:15:ed:df:34:57:17:65:61:5e:df:2b
bc:f8:24:7f:60:aa:f0:4c:e4:2f:6e:70:89:dc:c7:1a
3a:64:51:df:6e:08:7d:7d:d1:77:2d:a6:31:05:51:88
70:4f:8e:d9:57:d6:b3:fc:16:c1:93:30:13:6a:22:91
10:86:f7:de:1d:ed:5d:4a:49:e8:73:f3:d1:0d:91:61
3a:e4:dd:af:66:17:9b:e0:19:3e:1e:9c:5c:22:74:89
6c:5a:46:57:26:fb:4b:a9:33:45:43:31:7a:e7:22:1b
07:e3:62:69:12:19:88:3c:dd:62:aa:7d:df:06:52:99
55:1e:09:b5:36:35:f9:14:3d:56:b7:9b:02:10:3a:17
2b:59:5c:2f:dc:5b:d1:93:d1:64:db:ae:d7:76:40:be
9f:44:8d:03:72:bd:c2:26:d6:33:b8:dd:2a:f3:8f:0d
eb:5c:6c:96:20:8f:25:a1:d9:f3:b6:d2:45:4f:d3:c1
"""
n = int(n.replace(":", "").replace("\n", "").replace(" ", ""), 16)

e = 65537

d_partial = """
1?:87:88:f?:90:6?:31:d2:1d:?d:45:4f:b9:52:62:?c
d5:?b:0b:30:56:5b:dd:?0:60:ed:c1:d?:9b:67:aa:4b
5c:de:25:88:40:00:57:53:?9:87:28:32:f3:57:34:8c
43:e?:0c:c0:3f:f?:6b:92:8a:73:4f:ab:bf:d3:ec:2e
5?:f?:c8:56:a3:e?:1?:6?:?2:14:bc:71:29:58:83:?2
0a:47:80:e9:f?:?6:b1:d4:d?:6a:b2:?9:a?:c9:6?:?5
0?:9?:c?:?c:0c:ae:f?:a0:37:04:fb:46:8b:40:5c:35
76:a?:44:?4:25:?8:c4:3a:?e:de:?8:b7:58:5d:26:52
a7:?3:6?:13:01:3d:80:bb:47:1?:61:f8:1f:b3:eb:1c
85:2?:55:18:ea:e0:26:16:74:bc:0e:9b:92:??:93:a1
a6:1f:94:?4:a5:e5:29:da:fe:a4:b?:?8:de:39:8f:fd
7c:ee:?a:07:68:7f:f9:??:2?:b0:b1:b7:8b:f7:71:97
3c:cc:c?:?d:9f:?6:16:0a:c1:4e:2f:?b:68:93:cb:8?
f0:6e:f6:5a:06:cd:c4:49:e?:ad:b6:ef:e3:f?:df:22
?7:e3:4e:c8:ec:a8:7?:0b:??:47:63:1?:c3:0a:cb:dd
?f:c?:00:90:?b:13:?9:3d:2a:?d:dd:3f:56:fb:43:1b
"""

p_partial = """
e?:02:28:a5:8?:4d:?3:93:8d:?d:e3:6f:ec:d2:d?:d9
18:9a:e1:45:fc:28:a5:89:8d:f2:?d:a3:?5:17:a4:94
ab:e5:?a:d3:53:38:19:45:62:05:?c:?2:89:f1:7e:ef
d0:d1:39:e3:01:2e:90:fd:1e:53:18:26:96:76:4?:18
cc:a8:00:19:64:d?:82:5b:9f:12:30:22:?2:30:3f:f0
e9:?1:09:?c:0f:64:??:b2:98:cd:23:f0:74:?9:dc:09
21:ea:4e:?b:?2:c3:7f:8?:d5:0f:1?:2c:43:a7:f7:3a
65:e6:0d:1e:24:e1:bd:?9:2f:8e:10:7?:8b:?7:4c:?3
"""

q_partial = """
d8:2?:24:2?:6?:b1:2f:24:11:9d:?0:c?:b7:4?:5f:0f
0b:da:d5:a2:94:a3:ba:ca:79:6?:?1:fc:b6:06:17:27
56:c1:26:64:9d:9f:a7:?9:d6:fe:cc:23:fe:9f:77:9?
c8:ff:f9:?9:a6:97:3b:10:12:2?:ed:8c:eb:28:1b:9f
aa:c7:80:1d:?a:fe:4d:?2:5?:43:cb:c6:bd:25:5?:5a
81:26:37:05:0?:2a:f7:1c:d9:3a:?d:13:17:2?:17:d0
61:0f:6d:a5:1?:?c:aa:?e:d6:11:21:2e:b3:f?:?3:0c
?4:4a:3a:72:cd:0c:cf:5?:65:65:6d:6a:f2:8?:79:7b
"""

def hex_to_bit_list(s: str) -> str:
    s = s.replace(":", "").replace(" ", "").replace("\n", "")
    out = []
    for ch in s:
        if ch == "?":
            out.extend(["x"] * 4)
        else:
            out.extend(list(bin(int(ch, 16))[2:].zfill(4)))
    return "".join(out)


def known_bits_from_partial(bitstr: str) -> dict[int, int]:
    bits = {}
    for i, bit in enumerate(reversed(bitstr)):  # LSB first
        if bit in "01":
            bits[i] = int(bit)
    return bits


def construct_number(known_bits: dict[int, int], guess_bits: dict[int, int], max_bits: int) -> int:
    x = 0
    for i in range(max_bits):
        if i in known_bits:
            x |= (known_bits[i] << i)
        elif i in guess_bits:
            x |= (guess_bits[i] << i)
    return x


def branch_and_prune(
    N: int,
    p_known: dict[int, int],
    q_known: dict[int, int],
    p_guess: dict[int, int],
    q_guess: dict[int, int],
    bit_pos: int,
    target_bits: int,
    solutions: list,
    limit: int = 2,
) -> None:
    if len(solutions) >= limit:
        return

    mod_value = 1 << bit_pos if bit_pos > 0 else 1
    p_cur = construct_number(p_known, p_guess, bit_pos)
    q_cur = construct_number(q_known, q_guess, bit_pos)

    if bit_pos > 0 and (p_cur * q_cur) % mod_value != N % mod_value:
        return

    if bit_pos == target_bits:
        p_full = construct_number(p_known, p_guess, target_bits)
        q_full = construct_number(q_known, q_guess, target_bits)
        if p_full * q_full == N:
            solutions.append((p_full, q_full))
        return

    p_known_here = bit_pos in p_known
    q_known_here = bit_pos in q_known

    if p_known_here and q_known_here:
        branch_and_prune(N, p_known, q_known, p_guess, q_guess, bit_pos + 1, target_bits, solutions, limit)

    elif p_known_here:
        for qb in (0, 1):
            q_guess[bit_pos] = qb
            branch_and_prune(N, p_known, q_known, p_guess, q_guess, bit_pos + 1, target_bits, solutions, limit)
            del q_guess[bit_pos]

    elif q_known_here:
        for pb in (0, 1):
            p_guess[bit_pos] = pb
            branch_and_prune(N, p_known, q_known, p_guess, q_guess, bit_pos + 1, target_bits, solutions, limit)
            del p_guess[bit_pos]

    else:
        for pb in (0, 1):
            p_guess[bit_pos] = pb
            for qb in (0, 1):
                q_guess[bit_pos] = qb
                branch_and_prune(N, p_known, q_known, p_guess, q_guess, bit_pos + 1, target_bits, solutions, limit)
                del q_guess[bit_pos]
            del p_guess[bit_pos]


p_bits = hex_to_bit_list(p_partial)
q_bits = hex_to_bit_list(q_partial)

p_known = known_bits_from_partial(p_bits)
q_known = known_bits_from_partial(q_bits)

# p et q sont des nombres premiers RSA impairs
p_known[0] = 1
q_known[0] = 1

target_bits = max(len(p_bits), len(q_bits))

solutions = []
branch_and_prune(n, p_known, q_known, {}, {}, 0, target_bits, solutions, limit=1)

if not solutions:
    print("Aucune solution trouvée.")
else:
    p, q = solutions[0]

    if p > q:
        p, q = q, p

    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)

    print("n =", hex(n))
    print("p =", hex(p))
    print("q =", hex(q))
    print("d =", hex(d))