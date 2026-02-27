from PrimaryFunctions.encrypt import encrypt

plaintext = "fader scrub chins divvy amass"
password = "Didi-03?/"

plaintext = encrypt(plaintext, password)
print("\nEncrypted plaintext:")
print(plaintext)
