from PrimaryFunctions.decrypt import decrypt

CHALLENGE = "U2FsdGVkX1+nH9rYtEFp/PADwdT/aLalA/NT7FkPp2Rs7orZEpe9WpbDEfapMOiG\n"
TARGET = "trees lever trims loxes filly"

with open("./Texts/list_keys.txt", "r", encoding="utf-8", errors="ignore") as f:
    # Parcours du fichier ligne à ligne
    for i, line in enumerate(f):
        if i % 2000 == 0:
            print(f"Testé {i} mots")

        # Récupération de chaque ligne
        word = line.strip()
        if not word:
            continue

        # Déchifrage du Ciphertext avec chaque clé de la liste de clés possibles
        out = decrypt(CHALLENGE, word)

        # Comparaison du Plaintext obtenu au Plaintext original
        if out is not None and out.strip() == TARGET:
            print("FOUND PASSWORD:", word)
            break