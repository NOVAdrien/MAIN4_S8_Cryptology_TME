from decryptcopy import decrypt

ciphertext = "U2FsdGVkX1/oM6I8s/PNGYMdvL4xyivWpGpDOv+m8u/hi0N9Qr5fdYR1PsnX7jQG"
password = "ISECR0XX"

plaintext = decrypt(ciphertext, password, strict=True)  # strict=True => lève si mauvais

print("\nCiphertext:")
print(ciphertext)
print("\nDecrypted Plaintext:")
print(plaintext, "\n")