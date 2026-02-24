from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import math

# -----------------------------
# 1) Mets tes p et q ici
# -----------------------------
p = 158471677684273038093153148407962386946897322498319901708374187144876651813927183683552194590889424780826572914832512985150969008089255365634530873940748002908782603939614433042056329136752341273972201182106415015775394595517285664726268463186997232319706436196094918384907014719737044305373894618940197532451

q = 166397485532169568759599492214111269305439412936342049739557348862527244186639350322296635215381191518627671871443643898034442387540168439035865011312025782246857993679179638888518456434681274874494654837109311343925278300525009855843029611939612523628711266595053482174705835716489040177038054294267768350179

e = 65537

# -----------------------------
# 2) Calculs RSA
# -----------------------------
n = p * q
phi = (p - 1) * (q - 1)

# Inverse modulaire
def egcd(a, b):
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = egcd(b, a % b)
    return (g, y1, x1 - (a // b) * y1)

def modinv(a, m):
    g, x, _ = egcd(a, m)
    if g != 1:
        raise ValueError("e n'est pas inversible modulo phi(n)")
    return x % m

d = modinv(e, phi)

dp = d % (p - 1)
dq = d % (q - 1)
qi = modinv(q, p)

# -----------------------------
# 3) Construction clé privée
# -----------------------------
private_numbers = rsa.RSAPrivateNumbers(
    p=p,
    q=q,
    d=d,
    dmp1=dp,
    dmq1=dq,
    iqmp=qi,
    public_numbers=rsa.RSAPublicNumbers(e=e, n=n)
)

private_key = private_numbers.private_key(default_backend())

# -----------------------------
# 4) Export en PEM (PKCS#8)
# -----------------------------
pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

with open("private_keyB.pem", "wb") as f:
    f.write(pem)

print("Clé privée écrite dans private_keyB.pem")