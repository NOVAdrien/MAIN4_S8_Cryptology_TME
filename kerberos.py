import requests
import json

URL = "http://m1.tme-crypto.fr:8888/"
WORLD_ID = "d87d48ebc0f1f3268b4d753285c51d77" # Ton monde
ITEM_ID = "808a353cf73cc1221a5660a9e7babfad" # L'ID du tableau

data = {
    "jsonrpc": "2.0",
    "method": "item.location",
    "params": {"world_id": WORLD_ID, "item": ITEM_ID},
    "id": 737
}

response = requests.post(URL, headers={'Content-Type': 'application/json'}, data=json.dumps(data))
print("--- RÉPONSE DU SERVEUR ---")
print(response.text)