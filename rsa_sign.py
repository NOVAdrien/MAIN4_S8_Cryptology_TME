# recover_armoire_rsa.py
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

n = int("bd25d2428f5064ef8411a28bfbc8d35a372ee32086e36983ec09ac35c92bfd4e489befb31481aa6732b33ca909f9819c410f1857c064c0c37bbccb9d9d3846a277c58435db15eddf34571765615edf2bbcf8247f60aaf04ce42f6e7089dcc71a3a6451df6e087d7dd1772da631055188704f8ed957d6b3fc16c19330136a22911086f7de1ded5d4a49e873f3d10d91613ae4ddaf66179be0193e1e9c5c2274896c5a465726fb4ba9334543317ae7221b07e362691219883cdd62aa7ddf065299551e09b53635f9143d56b79b02103a172b595c2fdc5bd193d164dbaed77640be9f448d0372bdc226d633b8dd2af38f0deb5c6c96208f25a1d9f3b6d2454fd3c1", 16)

e = 65537

p = int("d829242261b12f24119df0c7b7485f0f0bdad5a294a3baca796181fcb606172756c126649d9fa769d6fecc23fe9f7794c8fff989a6973b10122eed8ceb281b9faac7801d5afe4d425a43cbc6bd255f5a812637050d2af71cd93a0d13172217d0610f6da5145caa2ed611212eb3f6730cf44a3a72cd0ccf5b65656d6af285797b", 16)

q = int("e00228a5864d73938d7de36fecd2dfd9189ae145fc28a5898df24da34517a494abe54ad3533819456205dc4289f17eefd0d139e3012e90fd1e53182696764918cca8001964d0825b9f123022c2303ff0e901099c0f6455b298cd23f07429dc0921ea4e8bf2c37f86d50f132c43a7f73a65e60d1e24e1bd492f8e107a8b974cf3", 16)

d = int("7e1a7214d8116449df461695b736cbd9f0c27cc099cd91f256f297f27ffda8f2812c1d61ca412c8782e0c6877853f55a647198ec2023cbf44851b57a8e700f7f8fd48a7191700c57ec404823da07f347e8c39329ad1c29fb498269e1f3b7d2b224cdef5bc3b33b5f1fc09219a3c304f9aecf0bd0d1641e38ea3f024f6212379a53f1419e1c34de049c84b1d6362d14591060e87c5585c3dc7db13619c2e0f0085af97f1440f6ef57fbc508ae5764a5c8b3f7c1859da9d7e3fd21041cbaab6887aba40a9cda79aac5e34e8dd429f118f4d108042166b406ac195c8c458a1105951608b73222773e43ecd1255ddcb55e40585713136263c5bbcd3df9b5ba94c9c5", 16)

dmp1 = d % (p - 1)
dmq1 = d % (q - 1)
iqmp = pow(q, -1, p)

private_key = rsa.RSAPrivateNumbers(
    p=p,
    q=q,
    d=d,
    dmp1=dmp1,
    dmq1=dmq1,
    iqmp=iqmp,
    public_numbers=rsa.RSAPublicNumbers(e=e, n=n),
).private_key()

pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption(),
)

with open("./Keys/rsa_sign.pem", "wb") as f:
    f.write(pem)

challenge = b"incur dated campo darer blats"
sig = private_key.sign(challenge, padding.PKCS1v15(), hashes.SHA256())

print("PEM écrit dans ./Keys/rsa_sign.pem")
print("Signature hex :")
print(sig.hex())