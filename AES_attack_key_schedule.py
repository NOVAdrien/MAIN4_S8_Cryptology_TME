#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64
import re
from z3 import *
# from z3 import Solver, BitVec, BitVecVal, BitVecSort, Extract, Select, Store, Array, ULE, sat
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# ============================================================
# Données du challenge
# ============================================================

IV_HEX = "35c6590aa778bece7400176aac9b83cf"

CIPHERTEXT_B64 = """
YrU2vtrkR16VIZF3KwNHlLJbPBbRS9M/tOoYjN/HM3VZ85yV/NK8Q36Bt1WmbP85
mcNAL+IHk45KGfJci962kFnm42r4kzi+ZTU0JjDKjLEyIFoKnsrx5KhAs918f95C
uHW1GCO1XrMvd4Wxy8zLLuW/zsBR4OsuXYizBnBiA3OhivL79MpaOjJonvxMdnIa
CIR0i5Hm5XP1eCt9p+M74kT75nm7XRhzsHl7RUR6meYx1OWciD9N9PBXzde5l5WF
DydbCAKbxL3Q5zzBhY62EEC0pAldbEMABmDAvD3iVy03SOZwC4Rl5wzth8v+7c8c
L56nxuioC/GKIgb4JlhzHcHc1US/0BbTzoiRuuqdAjduq3CO+SaN1etBZY5ClM+9
8oFywsWzx4FwVwT3kX1O15+tB5DxThSq+hf0cJ8JkJaUpIanx0Mmv7LK46t3pLCM
rADeDI6zYqP1E6uRX4t+yzpxH3CCKEMN3ryzb31DeyjifwH3tr/oByaz2qzTLVIB
OLSD1dqdaTi+KSL1rExdvaSo3pfqmxbg/oODfVRmWJOJmSVCgnIpJPoC06lmsnCe
Q+1ce/ea/AxQhAZGATuK6TiNQNk90sPVwNUMJX9MzMUJYp/ujoLxfVPRG+2JitTk
p7fKHVZpthfVDHbuiCpyeZtqYBGT8o49BN58VV6RDiyUzWU0QKybbLm0iu2AUFdn
5C/YZcFUhKtxWFs+srbNjKG58S8UvfQy/lDMdwECnNrqqZQk7gHtfn7DkFkFVU7L
NlwrIZJZES/xaHV8eyGcJRxrEFvPMgVfBMSlPXmJBEFaivo5voKzkbHOPJILEVeE
G1lO1FdH1VAvVibHVMGeHqUdgzcnDbXY+J5ma7F8m2l/mQFr3MiaUNRM5R54bPcK
1ogofoyifuJQ7TiFR/j+hP+RbmgcffJHO0EnT4URyMxN3UW5GYg60rs8wIsGJ98l
BxGC62D0GDhWFpDT/VSpMwg19nUI38NvVAr4kz8meuNAme2bbjYoQCgG94w/cAED
MAkjHTzO66Ex4/hIOVPJ9mfv/moo7lsoDtXYcrZfzUmpJq7GfQnWV8+haKojmsj7
fMCgxG2edUnhpMeKbVEVAroMF+qFaWGCnBt+0ACY7SmOk5OiO6fv6/Iikuk1VwCm
zr5/l5m1g5WAueW7aN4JYUUkuvATvyzkI1JbGhsm0hzYhaWwA6szbN8PVcx2NWHX
VVR9ejxTyojb78I1VQ11rnG/wI5Vz901G5YsUYAavqUlz5EzUIhZDh71S40/83FB
JF8vPmsnpjFyuLltY++UhChNpbd8OxBTGRF9ij9f2Tk3+EAIQRPeV3AlwcopqTly
e/fBak3K6X3ZVvkCl/NUD4p2B7XQHle94huHHz2EvfIj934IcIENCf8kzClBcVuc
oDBLJcbykMxYbLS2lV/Rj5sZ4+jY1MS94s6R/sgoLI4=
""".strip()

# 11 round keys AES-128 (16 octets chacune)
ROUND_KEYS_MASKED = [
    "88?e2e3??2bb?7??8eb55f?6d1??ea?7",
    "0bf?7?02?94265f?77f73aa?a6e6d0?f",
    "?7?90?267ecb6?d?093c?b?0afda8b?f",
    "?4b4?6?f?a7fb?87a343ecf70c?96788",
    "???112a?984e?5263??d49?137??2?59",
    "000?d93b984e?c?d??4335cc94??1b??",
    "?e?ff319b6e1?f0?1?a2bac88175a15d",
    "f39db??545?c30?150de8ad?d1a?2b84",
    "116ce02b??10?0??04ce?ae3?56?716?",
    "47?f652813d??51217?1eff1c27?9e96",
    "e??4f??df01b4?1fe?0a?f?e??7e3178",
]

# ============================================================
# S-box AES
# ============================================================

SBOX = [
    0x63,0x7c,0x77,0x7b,0xf2,0x6b,0x6f,0xc5,0x30,0x01,0x67,0x2b,0xfe,0xd7,0xab,0x76,
    0xca,0x82,0xc9,0x7d,0xfa,0x59,0x47,0xf0,0xad,0xd4,0xa2,0xaf,0x9c,0xa4,0x72,0xc0,
    0xb7,0xfd,0x93,0x26,0x36,0x3f,0xf7,0xcc,0x34,0xa5,0xe5,0xf1,0x71,0xd8,0x31,0x15,
    0x04,0xc7,0x23,0xc3,0x18,0x96,0x05,0x9a,0x07,0x12,0x80,0xe2,0xeb,0x27,0xb2,0x75,
    0x09,0x83,0x2c,0x1a,0x1b,0x6e,0x5a,0xa0,0x52,0x3b,0xd6,0xb3,0x29,0xe3,0x2f,0x84,
    0x53,0xd1,0x00,0xed,0x20,0xfc,0xb1,0x5b,0x6a,0xcb,0xbe,0x39,0x4a,0x4c,0x58,0xcf,
    0xd0,0xef,0xaa,0xfb,0x43,0x4d,0x33,0x85,0x45,0xf9,0x02,0x7f,0x50,0x3c,0x9f,0xa8,
    0x51,0xa3,0x40,0x8f,0x92,0x9d,0x38,0xf5,0xbc,0xb6,0xda,0x21,0x10,0xff,0xf3,0xd2,
    0xcd,0x0c,0x13,0xec,0x5f,0x97,0x44,0x17,0xc4,0xa7,0x7e,0x3d,0x64,0x5d,0x19,0x73,
    0x60,0x81,0x4f,0xdc,0x22,0x2a,0x90,0x88,0x46,0xee,0xb8,0x14,0xde,0x5e,0x0b,0xdb,
    0xe0,0x32,0x3a,0x0a,0x49,0x06,0x24,0x5c,0xc2,0xd3,0xac,0x62,0x91,0x95,0xe4,0x79,
    0xe7,0xc8,0x37,0x6d,0x8d,0xd5,0x4e,0xa9,0x6c,0x56,0xf4,0xea,0x65,0x7a,0xae,0x08,
    0xba,0x78,0x25,0x2e,0x1c,0xa6,0xb4,0xc6,0xe8,0xdd,0x74,0x1f,0x4b,0xbd,0x8b,0x8a,
    0x70,0x3e,0xb5,0x66,0x48,0x03,0xf6,0x0e,0x61,0x35,0x57,0xb9,0x86,0xc1,0x1d,0x9e,
    0xe1,0xf8,0x98,0x11,0x69,0xd9,0x8e,0x94,0x9b,0x1e,0x87,0xe9,0xce,0x55,0x28,0xdf,
    0x8c,0xa1,0x89,0x0d,0xbf,0xe6,0x42,0x68,0x41,0x99,0x2d,0x0f,0xb0,0x54,0xbb,0x16,
]

RCON = [0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80,0x1B,0x36]

# ============================================================
# Outils Z3
# ============================================================

def build_sbox_array():
    arr = Array('sbox', BitVecSort(8), BitVecSort(8))
    for i, v in enumerate(SBOX):
        arr = Store(arr, BitVecVal(i, 8), BitVecVal(v, 8))
    return arr

SBOX_ARRAY = build_sbox_array()

def sbox(x):
    return Select(SBOX_ARRAY, x)

def rot_word(word_bytes):
    # [b0,b1,b2,b3] -> [b1,b2,b3,b0]
    return [word_bytes[1], word_bytes[2], word_bytes[3], word_bytes[0]]

def sub_word(word_bytes):
    return [sbox(b) for b in word_bytes]

def xor_words(a, b):
    return [a[i] ^ b[i] for i in range(4)]

def add_rcon(word_bytes, r):
    # AES: SubWord(RotWord(w[i-1])) xor [Rcon,00,00,00]
    return [word_bytes[0] ^ BitVecVal(RCON[r], 8), word_bytes[1], word_bytes[2], word_bytes[3]]

def parse_round_key_mask(mask):
    assert len(mask) == 32
    out = []
    for i in range(0, 32, 2):
        out.append(mask[i:i+2])
    return out

def apply_mask_constraints(solver, byte_var, mask2):
    hi, lo = mask2[0], mask2[1]
    if hi != '?':
        solver.add(Extract(7, 4, byte_var) == BitVecVal(int(hi, 16), 4))
    if lo != '?':
        solver.add(Extract(3, 0, byte_var) == BitVecVal(int(lo, 16), 4))

# ============================================================
# Reconstruction de la clé AES à partir des round keys
# ============================================================

def reconstruct_aes_keys():
    solver = Solver()

    # 44 words de 4 bytes pour AES-128
    W = [[BitVec(f"w_{i}_{j}", 8) for j in range(4)] for i in range(44)]

    # Contraintes de domaine
    for i in range(44):
        for j in range(4):
            solver.add(ULE(W[i][j], BitVecVal(0xff, 8)))

    # Contraintes des round keys observées
    for r, mask in enumerate(ROUND_KEYS_MASKED):
        mask_bytes = parse_round_key_mask(mask)
        for j in range(16):
            w_idx = 4 * r + (j // 4)
            b_idx = j % 4
            apply_mask_constraints(solver, W[w_idx][b_idx], mask_bytes[j])

    # Key schedule AES-128
    for i in range(4, 44):
        if i % 4 == 0:
            temp = rot_word(W[i - 1])
            temp = sub_word(temp)
            temp = add_rcon(temp, (i // 4) - 1)
            for j in range(4):
                solver.add(W[i][j] == W[i - 4][j] ^ temp[j])
        else:
            for j in range(4):
                solver.add(W[i][j] == W[i - 4][j] ^ W[i - 1][j])

    # Petite heuristique utile : la solution correcte donne souvent du texte lisible après déchiffrement
    # mais on commence par résoudre purement le key schedule.
    if solver.check() != sat:
        raise RuntimeError("Aucune clé AES cohérente trouvée avec les round keys fournies.")

    model = solver.model()

    # Reconstitue les 16 premiers octets = clé maître AES-128
    key = bytes(model.eval(W[i][j]).as_long() for i in range(4) for j in range(4))

    # Reconstitue aussi les 11 round keys complètes
    full_round_keys = []
    for r in range(11):
        rk = bytes(model.eval(W[4*r + k][j]).as_long() for k in range(4) for j in range(4))
        full_round_keys.append(rk)

    return key, full_round_keys

# ============================================================
# Déchiffrement
# ============================================================

def decrypt_with_key(key):
    iv = bytes.fromhex(IV_HEX)
    ct = base64.b64decode("".join(CIPHERTEXT_B64.split()))
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = cipher.decrypt(ct)

    # tente PKCS#7
    try:
        pt_unpadded = unpad(pt, 16)
    except ValueError:
        pt_unpadded = pt

    return pt, pt_unpadded

def printable_score(data):
    if not data:
        return 0.0
    ok = sum(1 for b in data if b in (9, 10, 13) or 32 <= b <= 126)
    return ok / len(data)

def find_flags(text):
    patterns = [
        r'flag\{[^}]+\}',
        r'FLAG\{[^}]+\}',
        r'UGLIX\{[^}]+\}',
        r'\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b',
    ]
    hits = []
    for p in patterns:
        hits.extend(re.findall(p, text, flags=re.I))
    return sorted(set(hits))

# ============================================================
# Main
# ============================================================

def main():
    print("[*] Reconstruction de la clé AES-128 depuis les round keys corrompues...")
    key, round_keys = reconstruct_aes_keys()

    print("[+] Clé AES-128 retrouvée :", key.hex())
    print()

    print("[+] Round keys complètes :")
    for i, rk in enumerate(round_keys):
        print(f"K[{i:2d}] = {rk.hex()}")
    print()

    print("[*] Déchiffrement AES-128-CBC...")
    pt_raw, pt = decrypt_with_key(key)

    print("[+] Score imprimable (raw)      :", f"{printable_score(pt_raw):.3f}")
    print("[+] Score imprimable (unpadded) :", f"{printable_score(pt):.3f}")
    print()

    try:
        text = pt.decode("utf-8")
        print("[+] Plaintext UTF-8 :")
        print(text)
    except UnicodeDecodeError:
        text = pt.decode("utf-8", errors="replace")
        print("[+] Plaintext (UTF-8 avec remplacements) :")
        print(text)

    print()
    hits = find_flags(text)
    if hits:
        print("[+] Candidats flag trouvés :")
        for h in hits:
            print("   ", h)
    else:
        print("[-] Aucun flag direct détecté dans le plaintext.")
        print("[*] Sauvegarde du plaintext dans plaintext.bin / plaintext.txt")

        with open("plaintext.bin", "wb") as f:
            f.write(pt)
        with open("plaintext.txt", "w", encoding="utf-8", errors="replace") as f:
            f.write(text)

if __name__ == "__main__":
    main()