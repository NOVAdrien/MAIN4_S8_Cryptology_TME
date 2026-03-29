import requests
import json
import base64
import os
import email.utils
import calendar
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256
from Crypto.Util.Padding import pad, unpad

# ==========================================
# 🛑 VARIABLES À REMPLIR 🛑
# ==========================================
URL = "http://m1.tme-crypto.fr:8888/"
USERNAME = "AdrienPanguel"
PASSWORD = "Didi-03?/" # Ton mot de passe dans le jeu
WORLD_ID = "d87d48ebc0f1f3268b4d753285c51d77" # Ex: 1e4f8807b83cc7588d9993b3a345d8d9
TARGET_ROOM = "0ed0b788122bcacf824f1e4f3c422120" # Le bureau J04 de l'Atrium

headers = {'Content-Type': 'application/json'}

# --- SYNCHRONISATION TEMPORELLE ABSOLUE ---
def get_server_timestamp():
    resp = requests.get(URL)
    date_str = resp.headers.get('Date')
    if date_str:
        # Convertit la date HTTP du serveur en timestamp UNIX
        return int(calendar.timegm(email.utils.parsedate(date_str)))
    import time
    return int(time.time())

# --- CHIFFREMENT 100% COMPATIBLE OPENSSL LINUX ---
def openssl_encrypt(plain_text, password):
    salt = os.urandom(8)
    key_iv = PBKDF2(password.encode('utf-8'), salt, 32, count=10000, hmac_hash_module=SHA256)
    key, iv = key_iv[:16], key_iv[16:]
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # Bash 'echo' ajoute un \n qu'il faut reproduire pour la compatibilité
    padded_data = pad(plain_text.encode('utf-8') + b'\n', AES.block_size)
    ciphertext = cipher.encrypt(padded_data)
    
    b64 = base64.b64encode(b"Salted__" + salt + ciphertext).decode('utf-8')
    # On ajoute des sauts de ligne tous les 64 caractères comme le fait OpenSSL
    return '\n'.join(b64[i:i+64] for i in range(0, len(b64), 64)) + '\n'

def openssl_decrypt(b64_text, password):
    data = base64.b64decode(b64_text)
    salt, ciphertext = data[8:16], data[16:]
    key_iv = PBKDF2(password.encode('utf-8'), salt, 32, count=10000, hmac_hash_module=SHA256)
    key, iv = key_iv[:16], key_iv[16:]
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ciphertext), AES.block_size).decode('utf-8').strip()

# ==========================================
# EXÉCUTION DE L'ATTAQUE KERBEROS
# ==========================================
print("[*] 1. Demande du TGT (Authentication Service)...")
resp_as = requests.post(URL, headers=headers, json={
    "jsonrpc": "2.0", "method": "kerberos.authentication-service",
    "params": {"username": USERNAME}, "id": 1
}).json()

if "error" in resp_as:
    print("❌ Erreur AS :", resp_as["error"])
    exit()

tgt = resp_as['result']['ticket']
tgs_session_key = openssl_decrypt(resp_as['result']['key'], PASSWORD)
print(f"[+] Clé TGS déchiffrée : {tgs_session_key}")

print("\n[*] 2. Demande du Ticket de Méthode (Ticket-Granting Service)...")
# On utilise l'heure exacte du serveur pour tromper Kerberos
server_time = get_server_timestamp()
auth_plain = f'{{"username": "{USERNAME}", "timestamp": {server_time}}}'
auth_enc = openssl_encrypt(auth_plain, tgs_session_key)

resp_tgs = requests.post(URL, headers=headers, json={
    "jsonrpc": "2.0", "method": "kerberos.ticket-granting-service",
    "params": {"ticket": tgt, "authenticator": auth_enc, "method": "protagonist.move"},
    "id": 2
}).json()

if "error" in resp_tgs:
    print("❌ Erreur TGS :", resp_tgs["error"])
    exit()

method_ticket = resp_tgs['result']['ticket']
method_session_key = openssl_decrypt(resp_tgs['result']['key'], tgs_session_key)
print(f"[+] Clé de méthode obtenue : {method_session_key}")

print("\n[*] 3. Exécution de la téléportation (protagonist.move)...")
server_time = get_server_timestamp() # On resynchronise au cas où
auth_plain_2 = f'{{"username": "{USERNAME}", "timestamp": {server_time}}}'
auth_enc_2 = openssl_encrypt(auth_plain_2, method_session_key)

args_plain = f'{{"world_id": "{WORLD_ID}", "room": "{TARGET_ROOM}"}}'
args_enc = openssl_encrypt(args_plain, method_session_key)

resp_move = requests.post(URL, headers=headers, json={
    "jsonrpc": "2.0", "method": "protagonist.move",
    "params": {"ticket": method_ticket, "authenticator": auth_enc_2, "encrypted_args": args_enc},
    "id": 3
}).json()



if "error" in resp_move:
    print("❌ Erreur MOVE :", resp_move["error"])
else:
    resultat_chiffre = resp_move.get('result')
    if resultat_chiffre:
        resultat_clair = openssl_decrypt(resultat_chiffre, method_session_key)
        print("✅ RÉSULTAT DÉCHIFFRÉ :", resultat_clair)
    else:
        print("✅ RÉSULTAT : null (Téléportation réussie !)")