Ce projet consiste à utiliser les ChipWhisperer (des cartes électroniques
conçues pour mettre facilement en oeuvre des attaques par canaux auxiliaires).
Le projet est en deux parties.  Vous devez restituer le matériel à la fin du
semestre (sinon vous aurez zéro).  Vous devrez présenter les résultats obtenus
lors d'une petite soutenance à la fin du semestre.  La deuxième partie est
réservée aux étudiants qui ont déjà fait la première.

Première partie : AES
---------------------
Un message a été chiffré avec l'AES-128 en mode CBC, avec une clef et un IV
aléatoires.  Le bourrage standard a été utilisé (comme dans OpenSSL).  Utilisez
la ChipWhisperer-lite qui a été mise à vitre disposition et mettez en oeuvre
une attaque de votre choix pour récuperer le texte clair.

Voici le chiffré :
AES-CIPHERTEXT = 639c33e00dc8147b69a6ae73c0f29382cb2ca5d1140ac74d385f4f3dd252b31c827e2d565944e8ed89bd3a7670e63f039d2a80d7e7a81d4f8a1f0dbaa1c4fe5d695f32082018415370497c675e178148

Deuxième partie : RSA
---------------------
Un message a été chiffré avec le système RSA PKCS #1 v1.5 (c'est ce que fait
OpenSSL quand on demande un chiffrement RSA).  Demandez une ChipWhisperer-pro
aux ingénieurs support de l'équipe pédagogique puis mettez en oeuvre une
attaque de votre choix pour récuperer le texte clair.

Voici la clef publique :
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0u0LwPCWMF6QcfDCEmuP
Y3UnIbYQvdxy9Kw19KZYqsFfoSKFrH0zHkhFD1AEPBBGXFYwVoZMBr4m1zIoKd7v
UhHHSlj8QbApBWxnMdq5qtU1hZHU03d5Ei4Jya5iCyJxUmfpSNPtmfJyvYujpzAt
WulaJ6I+DtshhgDkDqY+GKyKuE2w0pcItwBZK06vYXN0CLoSl+1nOdhrHV7cH9qb
qTSgcoYKKOp7nmaqbJxovRB9N5y4M9VFr4f7WvDP5DcT/n6mnQzP4kNRrvklbCuv
ekBcapX0uhvMVhQms989dQXQRGk4Id5fyUd92X2toR6nIvYSfMWdGuDor8i4SdcF
8QIDAQAB
-----END PUBLIC KEY-----

Voici le chiffré :
RSA-CIPHERTEXT = 122653e90f7b10b6b9f0f81c5952f9a24235a01b9c69bb01ef8605a02586fcc1dba735a15f7a5ad0417c678c6f9f802f181b53feaed8f2bd54f9bf9c6f1af1b3b63784e8d1d792349233eef3e7e4a8a65a85c2e3d5dc54885a720e06f4b46b52470a5222ed5b0e41a208683075534615ab9c367a79594bb5819c388aba1e1f19982fdbf009231cbc2b9f8b8510321c6558cae4e251f8f0114a8043bfa7ef5b2a039446bd582ca5eda65153d2642bff3dfc378eefd38dc52cf0a9c5f1b03bed07b1fe2dc02f6dcd352865306aac503d2317161671df547abc42240831270389b7b510de2bd0b439e66b7ccc7eb73e6d1764364beafb9ceb38033c76a1dcda42f4
