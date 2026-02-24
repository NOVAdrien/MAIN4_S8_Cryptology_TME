from PrimaryFunctions.decrypt import decrypt

CHALLENGE = "U2FsdGVkX1+nH9rYtEFp/PADwdT/aLalA/NT7FkPp2Rs7orZEpe9WpbDEfapMOiG\n"
TARGET = "trees lever trims loxes filly"

with open("ListKeys.txt", "r", encoding="utf-8", errors="ignore") as f:
    for i, line in enumerate(f):
        if i % 2000 == 0:
            print(f"Testé {i} mots")

        word = line.strip()
        if not word:
            continue

        out = decrypt(CHALLENGE, word)  # strict=False par défaut => None si échec
        if out is not None and out.strip() == TARGET:
            print("FOUND PASSWORD:", word)
            break