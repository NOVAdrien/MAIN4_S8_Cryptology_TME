from encrypt import encrypt
from decrypt import decrypt

import base64

# message = "A Plaintext"
# password = "my_secret_passphrase"

# # Chiffrement
# ciphertext = encrypt(message, password)
# print("Ciphertext (base64):")
# print(ciphertext)

# # Déchiffrement
# plaintext = decrypt(ciphertext, password)
# print("Decrypted plaintext:")
# print(plaintext)

ciphertext = "U2FsdGVkX1/oM6I8s/PNGYMdvL4xyivWpGpDOv+m8u/hi0N9Qr5fdYR1PsnX7jQG"

# ciphertext = "U2FsdGVkX19CUhVx+CxBSwEapLRuc1aMycULnTDLyCZ6hgHpE8zZZ2mvJcrpm3El+VS0uvClnJ6OVtsV1pWyXg=="

password = "ISECR0XX"

print(repr(ciphertext))
print(len(ciphertext))

# base64.b64decode(ciphertext)  # si ça plante, c’est que le base64 n’est pas valide

plaintext = decrypt(ciphertext, password)
print("Decrypted plaintext:")
print(plaintext)

# # Chiffrement
# ciphertext = encrypt(plaintext, password)
# print("Ciphertext (base64):")
# print(ciphertext)
