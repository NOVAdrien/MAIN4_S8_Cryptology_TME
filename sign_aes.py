#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import base64

MESSAGE = b"cycad adorn runts roper shuck"

# Mets ici le chemin vers ta clé privée RSA
PRIVATE_KEY_FILE = "private.pem"

def main():
    with open(PRIVATE_KEY_FILE, "rb") as f:
        key = RSA.import_key(f.read())

    h = SHA256.new(MESSAGE)
    signature = pkcs1_15.new(key).sign(h)

    print("Message :", MESSAGE.decode())
    print("Signature (hex)    :", signature.hex())
    print("Signature (base64) :", base64.b64encode(signature).decode())

if __name__ == "__main__":
    main()