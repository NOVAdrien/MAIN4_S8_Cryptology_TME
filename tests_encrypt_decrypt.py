from encrypt import encrypt
from PrimaryFunctions.decrypt import decrypt
# from decrypt2 import decrypt2

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
# # print(plaintext)

# # ciphertext = "U2FsdGVkX1/oM6I8s/PNGYMdvL4xyivWpGpDOv+m8u/hi0N9Qr5fdYR1PsnX7jQG"
# # ciphertext = "U2FsdGVkX1/1fiiNcyBYc7VR1+96SdtC2p0tzT+edb8ghJQ68RA2VRQkrH0H5e2j"
# ciphertext = "U2FsdGVkX1911nHcGWY/BLPkmg9hL/SRPt3iJDX6HyT4kJr6UDjCKBXf8LFhicoV"
# # ciphertext = "U2FsdGVkX19CUhVx+CxBSwEapLRuc1aMycULnTDLyCZ6hgHpE8zZZ2mvJcrpm3El+VS0uvClnJ6OVtsV1pWyXg=="

# password = "Didi-03!-?/"

# print(repr(ciphertext))
# print(len(ciphertext))

# # base64.b64decode(ciphertext)  # si ça plante, c’est que le base64 n’est pas valide

# plaintext = decrypt(ciphertext, password)
# print("Decrypted plaintext:")
# print(plaintext)

# # # Chiffrement
# # ciphertext = encrypt(plaintext, password)
# # print("Ciphertext (base64):")
# # print(ciphertext)

# m = "test"
# s = "AdrienPanguel123"
# print(encrypt(m,s))


# m = "mohammed_saad.el_abbadi"
# s = "AdrienPanguel123"
# print(encrypt(m,s))

# ciphertext = "0e93683e496faf151740c3edc44ce6e0ca4b5d23d8804b9a62113db3edc7000cbf8f88c14a2d8a7dc85151531396f90183e01818a1a52d2f91846b9e0b389b69166ec0d38d3b47197a4cf9c693a21921cdf41bdcdc01ce27874b61db8386188fd021a22208ad121d7daabb21325999e5fb58fc520804998ad0b3acd50714c204b13c7e67e79ea00748c1d0e912b14291b423d9eb1704efc83632749366179eedba01ac8e52aa9ed5ba57f5fe9e653ecd765b00b626869e84eac8851599032fa7bc884660af2e61e6bb24e63a45571f96a63119aecbc5e78c13879edcb3bb804c8cf1203cda6e92512cd1addd832dabedf4f80bcb0763080ecacb592ee26fb7d6"
# password = "MIIBPTANBgkqhkiG9w0BAQEFAAOCASoAMIIBJQKCAQEArGseb911v/OWCUFFgM3G1IJN9DaXLnbNt/wB/Y+OSIIdhuHc0fXMr8F9gZalkUc+KKyh9Ha+R6DD4OngiPikrNMWIXGx92gHQZCH/+W2+hgAN8xwPYXaYsUK/FCQU//M5aTkVtLJQMO5355TubJ6J+x51y0K54ezfuENoEcpK8C+rI8Qr0ju6F2Hs7gmV+XAVThz7Bg/ZlkrnDKDxDhAl28x9EaWvbVmLK0ZAkWQBmWaOF3RIyIoFC6YWytOapNYXsIUae3EyFOeU2fSSjkGQv6AGwLdHqWDmaQt/uWpQMGYSkJi9ImEVsdNtE7OYwaTfXSdeSDlE6JOfrYLy14U2wIeeAWSlTXUlpaMc8oziaLZzQAAAAA+++ATRIUM+++B"

# plaintext = decrypt(ciphertext, password)
# print("Decrypted plaintext:")
# print(plaintext)

ciphertext = "0e93683e496faf151740c3edc44ce6e0ca4b5d23d8804b9a62113db3edc7000cbf8f88c14a2d8a7dc85151531396f90183e01818a1a52d2f91846b9e0b389b69166ec0d38d3b47197a4cf9c693a21921cdf41bdcdc01ce27874b61db8386188fd021a22208ad121d7daabb21325999e5fb58fc520804998ad0b3acd50714c204b13c7e67e79ea00748c1d0e912b14291b423d9eb1704efc83632749366179eedba01ac8e52aa9ed5ba57f5fe9e653ecd765b00b626869e84eac8851599032fa7bc884660af2e61e6bb24e63a45571f96a63119aecbc5e78c13879edcb3bb804c8cf1203cda6e92512cd1addd832dabedf4f80bcb0763080ecacb592ee26fb7d6"
password = "MIIBPTANBgkqhkiG9w0BAQEFAAOCASoAMIIBJQKCAQEArGseb911v/OWCUFFgM3G1IJN9DaXLnbNt/wB/Y+OSIIdhuHc0fXMr8F9gZalkUc+KKyh9Ha+R6DD4OngiPikrNMWIXGx92gHQZCH/+W2+hgAN8xwPYXaYsUK/FCQU//M5aTkVtLJQMO5355TubJ6J+x51y0K54ezfuENoEcpK8C+rI8Qr0ju6F2Hs7gmV+XAVThz7Bg/ZlkrnDKDxDhAl28x9EaWvbVmLK0ZAkWQBmWaOF3RIyIoFC6YWytOapNYXsIUae3EyFOeU2fSSjkGQv6AGwLdHqWDmaQt/uWpQMGYSkJi9ImEVsdNtE7OYwaTfXSdeSDlE6JOfrYLy14U2wIeEHF4fObeyNHi52X48UNQQQAAAAA+++ATRIUM+++B"

plaintext = decrypt(ciphertext, password)
print("Decrypted plaintext:")
print(plaintext)


