import json
from hashlib import sha256
from lamport_core import LamportPrivateKey

def load_signatures_from_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    signatures = []
    for entry in data:
        msg = entry["message"]
        if isinstance(msg, str):
            message_bytes = msg.encode("utf-8")
        else:
            message_bytes = bytes(msg)
        signatures.append((message_bytes, entry["signature"]))
    return signatures

def recover_private_key(signatures_data):
    recovered_key = [None] * 512

    for message_bytes, signature_hex in signatures_data:
        signature_bytes = bytes.fromhex(signature_hex)
        signature_blocks = [
            signature_bytes[i:i+32]
            for i in range(0, len(signature_bytes), 32)
        ]

        if len(signature_blocks) != 256:
            raise ValueError("Signature invalide : 256 blocs attendus")

        h = int.from_bytes(sha256(message_bytes).digest(), byteorder="big")

        for i in range(256):
            bit = (h >> i) & 1
            key_index = 2 * i + bit
            recovered_key[key_index] = signature_blocks[i]

    recovered_count = sum(k is not None for k in recovered_key)
    print(f"Récupéré {recovered_count}/512 parties de la clé privée")

    return recovered_key

def build_private_key(recovered_key):
    if not all(part is not None for part in recovered_key):
        missing = [i for i, part in enumerate(recovered_key) if part is None]
        raise ValueError(f"Clé incomplète, morceaux manquants : {missing[:10]}{'...' if len(missing) > 10 else ''}")
    return LamportPrivateKey(b"".join(recovered_key))

def main():
    signatures = load_signatures_from_file("./JavaScriptObjectNotation/catalogue.json")
    recovered_key = recover_private_key(signatures)

    sk = build_private_key(recovered_key)
    print("Clé privée reconstruite.")

    challenge = input("Challenge à signer : ").encode("utf-8")
    forged_signature = sk.sign(challenge)

    print("\nSignature Lamport du challenge :")
    print(forged_signature)

if __name__ == "__main__":
    main()