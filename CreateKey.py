from Crypto.PublicKey import RSA

TARGET = "+++ATRIUM+++"

tries = 0
while True:
    tries += 1

    # 1024 bits suffit souvent pour le jeu (sinon passe à 2048)
    key = RSA.generate(1024)

    pub_pem = key.publickey().export_key(format="PEM").decode()
    # pub_pem contient les lignes BEGIN/END + le base64 : on cherche dedans
    if TARGET in pub_pem:
        priv_pem = key.export_key(format="PEM").decode()

        print(f"[OK] Trouvé en {tries} essais\n")

        print("===== PUBLIC KEY (à mettre sur la carte) =====")
        print(pub_pem)

        print("===== PRIVATE KEY (à garder pour signer) =====")
        print(priv_pem)
        break

    # petit feedback
    if tries % 200 == 0:
        print(f"... {tries} essais")
