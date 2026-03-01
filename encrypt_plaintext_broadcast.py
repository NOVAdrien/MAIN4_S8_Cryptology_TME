from PrimaryFunctions.encrypt import encrypt

plaintext = "test"
password = "AdrienPanguel123"

plaintext = encrypt(plaintext, password)
print("\nEncrypted plaintext:")
print(plaintext)
