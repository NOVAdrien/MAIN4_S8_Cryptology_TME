from PrimaryFunctions.decrypt import decrypt

ciphertext = "U2FsdGVkX1/1fiiNcyBYc7VR1+96SdtC2p0tzT+edb8ghJQ68RA2VRQkrH0H5e2j"
password = "Didi-03?/"

plaintext = decrypt(ciphertext, password)
print("\nDecrypted plaintext:")
print(plaintext)
