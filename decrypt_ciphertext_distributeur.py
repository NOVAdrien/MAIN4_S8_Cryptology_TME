import binascii

# 1. Les données d'entrée en hexadécimal propre
# Les textes chiffrés (c)
c1_hex = "09dcdd93b468ca6617dcdbfb2d167673cff9c0be2042046c22e790cf1bbb3720868784d624592698080a0d7ff00c49b6377b8dbf48a9c2d6a71c8939086e8d4963480e031c0cfc164dfbe746bf265d86fcc1a2e3fe1eef0370d2e5f270a0741fba6ab98dd5a7023708672831e50f68398210807688478ca897855432d090bae43c146848af5c58f1c6e331f2f39f791bdc0c80deb175104b1826e6216b7f4b5362badf620ced2d8450a99a7a978924db24942a5168c786203d83b9128c716b5a2b98ef4c754688aacbd4cf621fcdf54e2521a40c74264201d198176e15ddcc15ce7956bf504205ed753b16f948020873c8a60d4d7be5a6ab9ea765c8441dbdc1"
c2_hex = "99a2bb1d4e1cad08900b41225471058ddbab94aec8bbd93d6870c185027f3b305e9e66cb25f6e51f73e525c3d43163115336bed8a1fa94db98643125959dc1850c81a60fdf6284c8ff4b89bbf0a3b9ad896142727165138f206875c90be9405b7d5b6a5c4df9b41d21221d060ee070eaf770c4c9f11240bdfd320f621fb43bad8a87df3cbcdbc6887de2adc43bf4dab77f6f745134e33cf62e7ecd0102b073956ed9a4b88bce3583e29976c97437f8449d1b693b2857ddde8ee77f2ca382164779a38fac889202c9d2b87fbb279ca95a435f0ef42d8c18d494e33b9afa16799f130d31d929124cde4d5384b4b227f147546483b3ae9cef044b51f331ed89b20e"
c3_hex = "2c59b0e207b3c8c223eb2753dd9cc7936d2c84d8dd472944dc46d35c96532fd5877bb4efa0060669d0a15d8ef1bb2dd823de007f26c45e6595c7048e85cef1c246bb593f8c4dfd286113f48b58a4592a6959ecef6dbf3581df3e8f9b677ba3ab3ea113f10f1cddd6ce44809e3b05e667a1b2b01f4a5389a018f9936433e04ea37bee6d16d079cd3d1bd01cfc07d65f5a2e3bd58faa1e78b380abea54196fbdf36d3b5f9f19ad4991022032d72f126e6391bd2411dc5366c0de9acb646bdcef1d2f63e72bd5953d77a3f5727907e63b51040ad9c32ee63cd029c8af9556c54a928c9e2448e365918d9ba39fa3e616b1ff4de25baa82a34ff6aff36a69fedb63de"

# Les modules (N) sans les deux-points
n1_hex = "bee9bd6750beb5a56d88685d199e193e3ec8e38e6af70021a47e091dbb5c41f7d832ca99708ef1a99813fbd3986c5666ddb63ef11631272a4851df3f99e701fc7e1de1a85c5b5c187850cae49144bde455a9100cad8bd137b5e0459cbd2a3b75b06cd243d8862dfca0098bbe411b1a63e74f913636027efb9138d4f011f597a5d3e2383a7a4bfb00df37941fe403e495c8084d37bc3155e7d9c007f07721e28f5cb557a1d2da8b80f5153f11f7e2d01f9d6cc9cd7126011972d3d714e3593161b196ccbbada38f5bbe9964b7080695951e941dc6712687c8a0c2982be3388d3f4696021948bd30c8bf4dfe87233d30b3379a2791a2198089292faf35f48e8c35"
n2_hex = "aff0cca51213ed42b68971b60d53588b131f921679017d9060591d17cb1a75fffb527b22f71b08a1f973e845781535ce6d3bc35b4225dfb607d4326f53092d44cb478a0521cb610d6e390a54156b4898ddd30452bb46f3cc718e4eb40085aab82d8940eb4fd9e4a3d005ca437214cf86c8b8b6221a079692b82ff7bfbc3f14b1dffac2b18bfa5decb89630b5416c1c1c0ad109908ba678cd1248f827e3140992f20df5642006df47a7f659e1cd42c73cb93607bb03eff97ff306662199befcdd559ee96c3a6fedad1e91bc36ccf5239e2a498f6180d49d4e478d002c52beae5356485e18666858174de2fb3794ecf5e0ce58af3dbeb480c156c1aae8056fbe27"
n3_hex = "b8b7f7dbd82d6a733a8faed66d8dd6c3098f4b78270fa37d28121791a3d7e871c80cd60ec9688ffa02ca8d544dd84bf8526eb24971d1eab0c8d2485e8cecb0916596b7c268a54632e589ef244f50a08d68a7d66eb3288899007469a57c60ed3529eafae7ceea65e26f3586e72a902052a48f737ee36acc0df3b4d0582a33e6de996f520b49d5a1ca468fea773f6c86b35b3a0c8f765325a78a17022352b7e30aef593021093d687d01c9ae24fce18b1dc3786a7bd4fe88dfc1767a3e1ef220bb7af47e91cfc1db73bf2ad7a58eff1c1f0c4d38733a781d9d138969bcc3d394b9893fd2eb0084d4dd11c474821e7bc7be4f2629d98dc92f2a379ce9cf08a5ba11"

# Conversion en entiers mathématiques
c1 = int(c1_hex, 16)
c2 = int(c2_hex, 16)
c3 = int(c3_hex, 16)
n1 = int(n1_hex, 16)
n2 = int(n2_hex, 16)
n3 = int(n3_hex, 16)

# 2. Théorème des Restes Chinois (CRT)
def crt(c_list, n_list):
    N_total = n_list[0] * n_list[1] * n_list[2]
    result = 0
    for i in range(3):
        Ni = N_total // n_list[i]
        # pow(base, -1, mod) calcule l'inverse modulaire
        inverse = pow(Ni, -1, n_list[i])
        result = (result + c_list[i] * Ni * inverse) % N_total
    return result

# 3. Calcul de la racine cubique entière par dichotomie
def integer_cbrt(n):
    low = 0
    high = n
    while low < high:
        mid = (low + high) // 2
        if mid**3 < n:
            low = mid + 1
        else:
            high = mid
    return low

# Application de l'attaque de Håstad
print("[*] Exécution du Théorème des Restes Chinois...")
m_cubed = crt([c1, c2, c3], [n1, n2, n3])

print("[*] Calcul de la racine cubique...")
m_int = integer_cbrt(m_cubed)

# 4. Conversion et extraction du message lisible
print(f"[*] Valeur brute de m (hex): {hex(m_int)}")

def get_printable_message(n):
    m_hex = hex(n)[2:]
    if len(m_hex) % 2 != 0:
        m_hex = '0' + m_hex
    
    data = binascii.unhexlify(m_hex)
    
    # On cherche la fin du padding RSA (00 02 ... 00 [MESSAGE])
    # Si c'est du padding PKCS#1 v1.5, le message commence après le premier octet nul 
    # trouvé après l'octet de type (02).
    if b'\x00' in data:
        parts = data.split(b'\x00')
        # On prend la dernière partie qui est généralement le message
        potential_msg = parts[-1]
        try:
            return potential_msg.decode('utf-8')
        except:
            return potential_msg # Retourne les bytes si le décodage échoue
    
    return data

resultat = get_printable_message(m_int)
print("\n[+] Résultat trouvé :")
print(resultat)