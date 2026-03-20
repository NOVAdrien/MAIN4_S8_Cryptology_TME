from PrimaryFunctions.encrypt import encrypt

# plaintext = "fader scrub chins divvy amass"
plaintext = "trips joist larva wrath excel"
password = "Didi-03?/"

plaintext = encrypt(plaintext, password)
print("\nEncrypted plaintext:")
print(plaintext)
