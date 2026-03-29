import sys

def split_blocks(hex_str, block_size=16):
    bytes_data = bytes.fromhex(hex_str)
    return [bytes_data[i:i+block_size] for i in range(0, len(bytes_data), block_size)]

def xor_bytes(b1, b2):
    return bytes(x ^ y for x, y in zip(b1, b2))

def format_hex(b):
    return b.hex()

def main():
    # Le message complet chiffré du challenge
    challenge_hex = "cf98b5764036581776dd2829c452c634a3340e10efaf006db424f7d1bff5546f4f106abdc6f23b87aff4f4dd793c3b28349a38a18b3c9a30650e4baa6e8b92454ad87ed97c766c1dcd4314c0ce149f91"
    blocks = split_blocks(challenge_hex)
    
    print("[*] Challenge AES divisé en blocs :")
    for i, b in enumerate(blocks):
        print(f"Bloc {i}: {format_hex(b)}")
        
    num_blocks = len(blocks)
    plaintext_blocks = []

    # On déchiffre de la fin (Bloc 4) vers le début (Bloc 1)
    # L'IV est le Bloc 0, il sert juste de C_prev pour le Bloc 1
    for target_idx in range(2, 0, -1):
        target_block = blocks[target_idx]
        prev_block = blocks[target_idx - 1]
        
        print(f"\n==============================================")
        print(f"[*] DÉCHIFFREMENT DU BLOC {target_idx}")
        print(f"==============================================")
        
        # Ce tableau va contenir le résultat brut du déchiffrement D(k, Cn)
        decrypted_raw = bytearray(16)
        
        # On devine octet par octet en partant de la fin du bloc (index 15 vers 0)
        for byte_idx in range(15, -1, -1):
            padding_val = 16 - byte_idx
            
            # On prépare le faux bloc C_prev
            fake_prev = bytearray(16)
            
            # Les octets déjà découverts doivent être XORés avec le padding attendu
            for k in range(byte_idx + 1, 16):
                fake_prev[k] = decrypted_raw[k] ^ padding_val
            
            # Génération des 256 requêtes pour l'octet actuel
            print(f"\n[+] Génération des 256 payloads pour l'octet {byte_idx} (padding attendu: {padding_val:02x})")
            payloads = []
            for guess in range(256):
                fake_prev[byte_idx] = guess
                payload_hex = format_hex(fake_prev) + format_hex(target_block)
                payloads.append(payload_hex)
            
            # Écriture dans un fichier pour un copier-coller facile
            with open("current_batch.txt", "w") as f:
                f.write("\n".join(payloads) + "\n")
                
            print(f"[!] COPIEZ le contenu du fichier 'current_batch.txt' et collez-le dans le mode BATCH du jeu.")
            print(f"Ensuite, regardez la ligne qui contient 'Successful decryption'.")
            
            valid_guess = -1
            while valid_guess < 0 or valid_guess > 255:
                try:
                    user_input = input("[?] À quel INDEX (0-255) l'oracle a-t-il accepté le padding ? (ou 'q' pour quitter) : ")
                    if user_input.lower() == 'q':
                        sys.exit()
                    valid_guess = int(user_input)
                except ValueError:
                    print("Veuillez entrer un nombre entier.")
            
            # Calcul du D_k(C)
            decrypted_byte = valid_guess ^ padding_val
            decrypted_raw[byte_idx] = decrypted_byte
            print(f"[*] D_k(C) partiel : {format_hex(decrypted_raw)}")
            
        # Fin de la boucle de l'octet pour ce bloc
        # On a récupéré tout D_k(Cn), on calcule le clair en XORant avec le VRAI bloc précédent
        plain_block = xor_bytes(decrypted_raw, prev_block)
        print(f"\n[+] BLOC {target_idx} CLAIR (hex)   : {format_hex(plain_block)}")
        print(f"[+] BLOC {target_idx} CLAIR (ascii) : {plain_block}")
        
        plaintext_blocks.insert(0, plain_block) # On insère au début de la liste
        
    print("\n==============================================")
    print("[🏆] MESSAGE COMPLET DÉCHIFFRÉ :")
    full_plain = b"".join(plaintext_blocks)
    print(full_plain)
    
    # Pour nettoyer le padding PKCS#7 / RFC2040 final
    padding_len = full_plain[-1]
    if 0 < padding_len <= 16:
        clean_plain = full_plain[:-padding_len]
        print(f"[🏆] MESSAGE SANS PADDING :")
        print(clean_plain.decode('utf-8', errors='ignore'))
    else:
        print("[!] Erreur : Padding final invalide.")

if __name__ == "__main__":
    main()