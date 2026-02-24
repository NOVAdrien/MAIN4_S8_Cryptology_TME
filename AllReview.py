from PrimaryFunctions.decrypt import decrypt

ciphertext = "U2FsdGVkX1/oM6I8s/PNGYMdvL4xyivWpGpDOv+m8u/hi0N9Qr5fdYR1PsnX7jQG"
password = "ISECR0XX"

plaintext = decrypt(ciphertext, password)

print("Decrypted plaintext:")
print(plaintext)
