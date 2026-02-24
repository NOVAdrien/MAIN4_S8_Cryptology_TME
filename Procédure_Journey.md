# Procédure Journey

## A chaque connexion

### Se connecter au jeu
telnet m1.tme-crypto.fr 1337

### Récupérer la progression du jeu
[Aller dans la SALLE DES SAUVEGARDES au nord+est à partir de la position initiale.]
>>> terminal
[Entrer id = "AdrienPanguel" et mdp = "Didi!-03?/".]

### Plan du NIVEAU SS
                                                       YZY -- datacenter
                                                        |
                          local de service 3           XYX
                                  |                     |
            XYY ---------------- XXY ----------------- ZYX
             |     +------------------+                 |
             |     |      Salle       |                 |
            ZXY ---|       des        |---- trappe --- XXZ
             |     |   Sauvegardes    |       |         |
             |     +------------------+    poubelle     |
            ZZX ---------------- ZYZ ----------------- XZZ
             |
            YYZ
             |
            YZZ  ----------------- YXZ --------------- XYZ
             |                      |                   |
             |              local de service 5          |
     ??? .. ZXZ                                        XZX
             |                                          |
 réserve -- XZY                                        XXX -- local électrique

[press any key]

## Historique de l'aventure

### FLAG 1: S'enregistrer sur le registre des participants porur sauvegarder sa progression

[Prendre le plan interactif au nord+est.]
>>> prendre plan
OK

[Consulter le plan avec la comande suivante.]:
>>> utiliser plan

[Aller au Datacenter/SalleDesServeurs au nord-est et lire l'inscription]:
>>> lire inscription

POST-IT PASSWORD: ISECR0XX

[Noter ce password quelque part (c'est bien un "zéro").]

>>> inspecter clavier

U2FsdGVkX1/oM6I8s/PNGYMdvL4xyivWpGpDOv+m8u/hi0N9Qr5fdYR1PsnX7jQG

[Ce Ciphertext change à chaque nouvelle connexion.]
[Noter ce Ciphertext quelque part.]

[Aller à la réserve au sud-ouest.]
Ici se trouve un guide OpenSSL (tome I) : chaînes de caractères.
Ici se trouve un guide OpenSSL (tome II) : chiffrement symétrique.
Ici se trouve un guide OpenSSL (tome III) : génération d'une paire de clef.
Ici se trouve un guide OpenSSL (tome IV) : chiffrement à clef publique.
Ici se trouve un guide OpenSSL (tome V) : signature.
Ici se trouve un guide OpenSSL (tome VI) : script d'exemple.

[Lire tous les livres et copier leur contenu dans le dossier ./Livres/ .]
[A chaque nouvelle connexion, les tomes reviennent dans cette salle.]

[Lancer le code decrypt_ciphertext_post_it.py pour décrypter le ciphertext trouvé précédemment sur le post-it avec la commande suivante.]:

python3 decrypt_ciphertext_post_it.py 

[Retour de la commande]:

Ciphertext:
U2FsdGVkX1/oM6I8s/PNGYMdvL4xyivWpGpDOv+m8u/hi0N9Qr5fdYR1PsnX7jQG

Decrypted Plaintext:
breve falls ovate disks bwana

[Le Plaintext "breve falls ovate disks bwana" est le clair du Ciphertext "U2FsdGVkX1/oM6I8s/PNGYMdvL4xyivWpGpDOv+m8u/hi0N9Qr5fdYR1PsnX7jQG".]

[Entrer ce Plaintext dans le terminal de la salle des serveurs en tant que "machine password".]
>>> terminal
                                                                UGLIX v4.0 beta
                                                                SYSTEM STARTING... 
                    ERROR
                    - Corrupted system data structure
                    - Backup user directory unreachable
                                                                RECOVERY... 
                    FAILURE
                    - Recovery data not found
                                                                COLD START... 
                    Enter machine password:     *****************************        [Entrer ici le Plaintext.]

                    - Creating new administrator user account
                    Choose username:            AdrienPanguel                    
                    Choose password:            *********                        [Choisir son password.]
                    Confirm password:           *********                        
                                                                System setup... 
                    SUCCESS
                    - Created account ``AdrienPanguel'' (with full admin privileges)

                                                                    Press any key                     

                                                                   UGLIX v4.0 beta                                                                   
                                                              (main security terminal)
                    Active user: AdrienPanguel
                                                               System services status
                                                               ----------------------      
                    - power controller                          OFFLINE
                    - physical access controller                OFFLINE
                    - elevator controller                       OFFLINE
                    - terminals                                 OFFLINE
                    - censory engine                            OFFLINE
                    - security engine                           OFFLINE
                                                                        Menu
                                                                        ----             
                    1. bring everything ONLINE
                    2. procrastinate

[TAPPER "1" dans le terminal ouvert.]

>>> terminal
[security engine] register:52:1|b644c1e209b41a83e9ed72be2f7878f8eb9c34fde9a06f0e9701f5448840e16a      [PREMIER FLAG !!!]

### FLAG 2&3: Créer ma clé privée et ma clé publique

>>> conseil
Vous ne trouvez pas qu'il fait sombre ?  Essayez de remettre le courant.
Vous devrez aller au sud-est.

[Aller au local de service 5.]
[Ouvrir le terminal.]
>>> terminal
                                               UGLIX v4.0 beta
                                                                 (Service terminal)
                    Active user: AdrienPanguel
                                                                      Main menu
                                                                      ---------
                    1. Manage ID card
                    2. Public Key Infrastructure
                    3. Locksmith Tools
                    4. Exit

[Entrer "2. Public Key Infrastructure"]:
                                                                   UGLIX v4.0 beta            
                                                                 (Service terminal)             

                    Active user: AdrienPanguel
                    public-key uploaded: NO

                                                                      PKI menu
                                                                      --------
                    0. Query public-key directory
                    1. Upload public-key
                    2. Upload signature
                    3. Tutorial
                    4. Submit Certificate Signature Request
                    5. Return to main menu

[Entrer "3. Tutorial" pour voir les étapes à suivre.]:
                                                                   UGLIX v4.0 beta                       
                                                                 (Service terminal)                             
                    Active user: AdrienPanguel
                                                                    PKI tutorial
                                                                    ------------
                    The PKI offers a public directory of public keys.
                    Users can upload their own public keys.
                    The PKI guarantees that keys belong to the correct users,
                    because users are authenticated when they upload their keys.

                    To complete the tutorial, take the following steps:
                    1. Read the openssl documentation manual
                    2. Fetch the public key of user "pki_tutorial"
                    3. Encrypt the string "I got it!" with this public-key
                    4. Submit the (hex-encoded) ciphertext below

                    Ciphertext:                                                   

[Entrer "0. Query public-key directory".]
[Entrer le username "pki_tutorial".]
[Copier la Public key obtenue.]
                                                                   UGLIX v4.0 beta
                                                                 (Service terminal)
                    Active user: AdrienPanguel
                                                                Public-key directory
                                                                --------------------
                    Username:                   pki_tutorial

                    Public key:                 
                    -----BEGIN PUBLIC KEY-----
                    MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAozZd9B4P23YJ21daS2AX
                    K6rkHrs/3jF/M74WulpCmlN9aiI04Siv4WbTW6aH50B56hkLRjafuOk4Kxnv/wmv
                    NqKKdkbIq44aHMi+N0cy3ho8DDdT5iqB6RZU+w18qqmqEfui8wnz9rCgDxUzTzbf
                    mUmJt1MS4YRJtRNR9aQVwg5OhZYj35qqe05wcP/BfV8GxiLpJFT9t6ntn7tuiDzC
                    M9AFi2BMhYj/lB2Fdfo7bX/PHLwefYEHQ9JFkMiTSaFfyFJ7EP0Y1K12iA/swUXX
                    KWQWZkSCOVmkRlFCrD7ijX9OmJNpMapCT2RmklsKuPKz098wlxUP5AfQQ3Qkiics
                    BQIDAQAB
                    -----END PUBLIC KEY-----

                    Signatures:                 NONE

[Sauvegarder cette Public key dans un fichier ./Keys/PublicKeys/public_key_pki_tutorial.pem]
[Il faut chiffrer le texte "I got it!" avec cette public_key_pki_tutorial avec les commandes suivantes]:

printf "I got it!" > ./Texts/msg_pki_tutorial.txt

openssl pkeyutl -encrypt -pubin -inkey ./Keys/PublicKeys/public_key_pki_tutorial.pem -in ./Texts/msg_pki_tutorial.txt -out ./Binary/msg_pki_tutorial.bin

xxd -p ./Binary/msg_pki_tutorial.bin | tr -d '\n' > ./Hexa/msg_pki_tutorial.hex;

cat ./Hexa/msg_pki_tutorial.hex

[Retour de ces commandes]:

55df8f73c2663597b98426d51f093244e362df0f37b38bb71d43f6e17c2435b9d687a663daad8296727ef61afeed735b4a9a180468151326889adb792d1c6d660521f289168a1db2bc26a095e96947461a900e76e7ddfaf2bcaa9ac336b9a5cade4bc262cbd178994b7a5e5194cb2300eabe804faa61466627f25844be746d383d491793df8888af52250f07f4d098a9450c8e82d6dae81484e2c1708ab13c404c92f00d25b71b1a529e0555fb7ed2afbf49254774aecd700c062dae5f892fd95c1c5e4970a90e25a0fc1c62d4d4a32b14911b2cbeb31de528f35ab9760b25e8062efd12b2405e1355968921bdea1fa082842f20be7bcb8f12f57307867b4f10

[Remarque: cette sortie sera toujours différente d'une fois sur l'autre, car le chiffrement ets probabiliste et non déterministe.]
[Copier-coller ce retour dans la case du "3. Tutorial" après "Ciphertex:"]

                                                               +--------------------+
                                                               | TUTORIAL COMPLETED |
                                                               +--------------------+

[Le tutoriel est terminé.]
[Générer notre clé privée avec les commandes suivantes]:

openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:2048 -out ./Keys/PrivateKeys/my_private_key.pem

[Contenu de ./Keys/PrivateKeys/my_private_key.pem]:

-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCxUXBGiQ4bf77d
RpamCfDNHV/3PzA87IooKjznWCdYl1/h8oZLNwTTWQdFYQvbUBpB379CgtmTIH63
OjUEuvGh3un+GL7q8YMEUKuUT++sUQUX91/t5uGZWUGUsELdAQwlxOedgdOZBAdD
pF6ZCZj08PBrOuFgwYBG4yqBvr14L6fC5uoguWkjxySK50g8bNFY7v/k9AC2T9tL
ftYkpQviVY5+pBdWoYn1D5EvDIb7Aq/kFPITzVbirNxJ8dtDjHqGp4oEy3eLrfce
ms4rVk3To866ufcBjAmHWzW/52BlhMUeKwcxKNcohddfPxpw9U7lTsj9jcD0pVXK
Gdkcjue9AgMBAAECggEABAfbo0LUzwO3oTyMSqBxuJvpFUv6qvvehRy2rzSWCmHA
hHiYnGeXBL3imC1lUVowCpzNMnQagYlsz/nzABVGzlzsmUHTPzB3v7acu92YT2S1
Fq8hH12O9cctYjWig3cVYVtpP2+W0YThrGQ1YUmyUCkU8f8P5fzoD1R1ICdnk66J
1+amcF5uE4L6OBbYqjMiVmh6KTOIPRyimAauKW8UJN3+aBofXw99yMmGt0B0SF1a
L1iAyh1HXIqROkSl9NQeG9q6PtpXo7Rw4neDyWSHHUZdxf9xB7b8MoZ/9aYuCEoj
DBBUcKmc/AQ/cgUBC3cjWJJg1Mh844dVzrGrD7URKQKBgQD30AOEAW0M6NugpRwC
od6u9UcGb0Am14Mz3my9iwX7piy8Q9iQ8WGYCFVyheKRrpLf7hzVHiJg5JDHomzh
Ym7UNKjZr2Ei5FqUYtaFQWcy8fCA5i0P5tNJBX+rwU+1T5DgLXLPenmOMjkQ/Ed1
w4LviCmDvJR5+0U47D8dGhgGGQKBgQC3LS+5SjzybdyRgSuAiYjYBJL0fRn6UtBQ
MGgc9l/FBVyKjjgBDvdeb/XKfzSbPfqbuujWyRA46aFBD4EoMchMaMq7k05SaVz+
Tuw8up+rmwi+XdB5cWmtY11pD7Wqk1MUSnwSmOdzpGu2fQKLSxRScJFrB/Qiq342
jUPmbsm7RQKBgQCArSSGMO9dGrSgT9uhikfE9Vux/aaEBLf+AOrZ6QxsRTdJcrlL
WethNEKaOucQ2mMtn8ic6Q7U3RpIbxC2X5RI4CclEaoQoh5emovlmbZqf7JwXBTe
Au+HJTHMD47CCNSjczYAggoISg/TwAujHKgqlLtpykwWouCo1BNZmykKUQKBgGuO
uuEf+F2ZqNQ/dp3JJHNDbE7nTmOwUOVlJx0qhd2YYlhxXe0xLotjTn4S537oi8j5
nVLRSRdCCA+93OcPJD/JoJE309uMRrCFAy49nxgStrWhPJKyx4yqNeVE9jUswLG/
cs8wvWcn+p9zFBVahppJwvmH+BCLhlbd6CrcjtPJAoGAEb+ZEd6eUUEWOA7F/ZBg
R3mXuNWES06STuUrVT+MDCbh0Pl9S5UXy3ECPZEW1yIcYkfKoinaX1eqJ3zz/RJC
y0YNymQUrdHtFgBS7q1KB8EqJClnqExi9NKPrp3iMocWjenKwwTKQg2Y4iDjXAl/
HEtJymRR5Y3PMfVINrpHq8Q=
-----END PRIVATE KEY-----

[On en extrait notre clé publique avec la commande suivante]:

openssl pkey -in ./Keys/PrivateKeys/my_private_key.pem -pubout -out ./Keys/PublicKeys/my_public_key.pem

[Contenu de ./Keys/PublicKeys/my_public_key.pem]:

-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsVFwRokOG3++3UaWpgnw
zR1f9z8wPOyKKCo851gnWJdf4fKGSzcE01kHRWEL21AaQd+/QoLZkyB+tzo1BLrx
od7p/hi+6vGDBFCrlE/vrFEFF/df7ebhmVlBlLBC3QEMJcTnnYHTmQQHQ6RemQmY
9PDwazrhYMGARuMqgb69eC+nwubqILlpI8ckiudIPGzRWO7/5PQAtk/bS37WJKUL
4lWOfqQXVqGJ9Q+RLwyG+wKv5BTyE81W4qzcSfHbQ4x6hqeKBMt3i633HprOK1ZN
06POurn3AYwJh1s1v+dgZYTFHisHMSjXKIXXXz8acPVO5U7I/Y3A9KVVyhnZHI7n
vQIDAQAB
-----END PUBLIC KEY-----

[En revenant à "1. Upload public-key", copier-coller cette clé publique]:

[security engine] pki.tutorial:52:1|8d3a204ece50cdea3d35d5c16bca71d7961841a01f1071dbafd6dc5a441da049      [DEUXIEME FLAG !!!]
[security engine] pki.upload:52:1|a75e2154fd95ebaefb63cb2d469d9d40062e3e32dce8c339b154f634d8f0eeb1        [TROISIEME FLAG !!!]

### FLAG 4: Signer un message avec ma clé privée

[Retourner dans le local électrique]
[Signer avec my_private_key le challenge donné "twerp reply visor ahead churl" avec les commandes suivantes]:

printf "twerp reply visor ahead churl" > ./Texts/sign_challenge1.txt

openssl dgst -sha256 -sign ./Keys/PrivateKeys/my_private_key.pem -out ./Binary/sign_challenge1.bin ./Texts/sign_challenge1.txt

xxd -p ./Binary/sign_challenge1.bin | tr -d '\n' > ./Hexa/sign_challenge1.hex

cat ./Hexa/sign_challenge1.hex

[Retour de ces commandes]:

0e1d8d191c8cb173e02432d4c150c9c903b2aed9e29e89398ce9f3e566156c1492874210ebae69c0941e9bebceafcb328b6c218646414488f43a50f581086755dabbcdf0e312540f934dec5f2613c2cba09e7085e4fd53a4d756bec9547f36d0337061003e57267db113d0dc44884b113205c9985e8692d6846d8081c9e49431eab4cb4cb8b25176e5e3f3243592c7491469e090301e71384b390495b7d855e9ec7e0d6e383607465d83f59ce484756d0c07a5ec4c0156d5a874f6d48cb32b9731aaa14310a61f3c769f2c5e40eceb12f1975073e77a6791ed5d71beb30960d92e2e55f870fdfcd32ad19fe1b08703305789f63c998c8935d261cbc69931a50a

[Upload cette sign_challenge1.hex pour ce challenge]:
                                                    +-------------------------------------------+
                                                    | VALID SIGNATURE --- AUTHORIZATION GRANTED |
                                                    +-------------------------------------------+

[security engine] power.on:52:1|10405faceec8e4e858c1de99d079861bebece22f18a1dfbeaf38819bc16a4891      [QUATRIEME FLAG !!!]

### FLAG 5: Attaque de dictionnaire avec un test naïf de clés

>>> conseil
On y voit mieux maintenant.  Essayez de revenir sur vos pas à la recherche d'une sortie.

[Aller en YZZ devant la baie vitrée et casser la vitre avec l'extincteur ramassé quelque part sur la carte.]
>>> utiliser extincteur
Votre chance de sortir vivant de l'inévitable confrontation avec
la horde de drones tueurs est estimée à 5 %.
(un tirage indépendant à lieu lors de chaque tentative).

GAME OVER

[Il faut réésayer jusqu'à ce que le tirage aléatoire me soit favorable.]

[...]

[Il faut jouer au jeu PAcMan pour améliorer mes proba de survie.]
[Un terminal s'ouvre, et il y a 3 niveaux de PacMan à effectuer (Essayer une seule fois suffit à valider le palier).]
                                                                   UGLIX v4.0 beta
                                                      (Bot Escape Simulation Research Terminal)
                    Active user: AdrienPanguel
                    Survival probability: 5 %
                                                                        Menu                 
                                                                        ----             
                    1. [TODO] Level 1
                    2. [TODO] Level 2
                    3. [TODO] Level 3
                    Q. Exit

[J'ai pu terminer les 3 niveaux et ma proba de survie a augmenté.]
                                                                   UGLIX v4.0 beta
                                                      (Bot Escape Simulation Research Terminal)
                    Active user: AdrienPanguel
                    Survival probability: 100 %
                                                                        Menu
                                                                        ----
                    1. [DONE] Level 1
                    2. [DONE] Level 2
                    3. [DONE] Level 3
                    Q. Exit
*** Q

>>> conseil
Vous ne trouvez pas que l'ambiance commence à se tendre par ici ?  Maintenant qu'on y
voit mieux, re-explorez les alentours pour trouver une sortie.

>>> utiliser extincteur
Votre chance de sortir vivant de l'inévitable confrontation avec
la horde de drones tueurs est estimée à 100 %.
(un tirage indépendant à lieu lors de chaque tentative).

[...]

Après ce petit jeu du chat et de la souris, vous avisez une echelle de secours
qui conduit à l'étage du dessus.  Vous montez, et vous arrivez à la surface.
Enfin, la lumière du jour !  La trappe d'accès se referme derrière vous.
Vous n'allez pas regretter ce sous-sol et ses drones tueurs...

>>> conseil
Commencez par aller dans le labo qui est au nord-ouest.

[Nouveau plan]:

NIVEAU SB
=========

          22 -------------- 32                    
           |  \             |
           |   [LPNHE]      |                      
         22-23 ---------- 32-33                  
           |                |           tipi                       cul-de-sac               
           |                |            |                              |            
 cour --- 23 ------------- 33 ------- 33-43 ------------ 43 -------- 43-53       53 
           |                |                             |                       |  
           |                |                       [bibliothèque]                |      
         23-24 ---------- 33-34                                                 53-54 --- [atrium]
           |                |                           rotonde                   |         
           |                |                              |                      |
          24 -------------- 34 --------- 34-44 ---------- 44 -------------------- 54 
           |                               |                                      |
           |                           [parking]                                  |
           |                                                        [CICSU] ----- 55 
           |                                                                      |
           |                                                                      56 
           26 
           |
   rampe accès pompiers 

[Aller au laboratoire]:
>>> labo

[Cette ouverture du temrinal n'est pas nécessaire, mais elle est rigolote car je peux communiquer avec d'autres gens ;)))]
>>> ouvrir terminal 

                                                                   UGLIX v4.0 beta
                                                    (Experimental Quantum Communication Terminal)
                    Active user: AdrienPanguel
   Id From                             Subject
----- -------------------------------- -------------------------------------------------------------------------------------------------------------
U   0 oscarito                         coucou alex
U   1 TestAlex                         Coucou Oscar
U   2 oscarito                         Re: Coucou Oscar
U   3 TestAlex                         Re: Re: Coucou Oscar
U   4 oscarito                         Re: Re: Re: Coucou Oscar
U   5 TestAlex                         indice flag 7
U   6 oscarito                         Re: indice flag 7
U   7 TestAlex                         Re: Re: indice flag 7
U   8 oscarito                         Re: Re: Re: indice flag 7
U   9 lucien.coudert                   bonsoir à tous
U  10 P3P3                             bonjour
U  11 cmanioc                          Re: bonsoir à tous
U  12 rubinouchi                       le bonjourn
U  13 root                             coucou
U  14 roman.avidano                    coucou !
U  15 adminX                           Coucou tout le monde !
U  16 vtrelat                          Dedicace a Effka
U  17 master                           Re: Dedicace a Effka
U  18 Agathe                           cc
U  19 JYU                              aaaa
U  20 hpv                              ?
U  21 hpv                              Salut
U  22 aurelie_marande                  Re: Re: bonsoir à tous
U  23 maniche                          bien guez mathis
U  24 tomLU                            premier essai
U  25 guilford                         hello
U  26 juju                             ?
U  27 julian                           je sais pas
*** 
(type ? for help)

[J'ai aussi communiqué un message "Salutations très chers camarades !".]

[Plan du laboratoire]:
>>> plan
LPNHE (niveau SB)
=================

                              [niveau SB]
                             /
                            /
                 hall d'entrée 
                       |
                       |
        RC-17 -----    |     ----- RC-13 
                   \   |    /
                    couloir 
                   /   ┊    \
        RC-19 -----    ┊     ----- RC-14 
                       ┊
                       ┊
               salle d'expériences 
                |
                |
                |
               ??? 

[Aller dans RC-13 et lire le post-it]:
>>> lire postit
Un post-it rose collé sur la porte.  Il dit :
        emmalyn87, combien de fois t'ai-je dit de ne pas choisir ton mot de passe
        dans le Cambridge English Dictionary ? Tu n'apprends jamais rien !
        Comment je suis censé faire respecter une politique de securité, moi, tu y penses ?
        ---
        L'administrateur système

[Noter l'username "emmalyn87" quelque part.]

[Lire le feuillet.]
>>> lire feuillet
Une feuille A4, 80g/m².  Un utilisateur a imprimé dessus une trace du protocole 
d'authentification CHAP.  Peut-être qu'il essayait de mettre au point un client
personnalisé pour se connecter ? Il y a écrit :
---> {"jsonrpc": "2.0", "method": "protagonist.CHAP-challenge", "params": {"world_id": "38bf0af045856a2a4688ffc790d402c1", "username": "emmalyn87"}, "id": 236}
<--- {"jsonrpc": "2.0", "result": "U2FsdGVkX1+nH9rYtEFp/PADwdT/aLalA/NT7FkPp2Rs7orZEpe9WpbDEfapMOiG\n", "id": 236}
---> {"jsonrpc": "2.0", "method": "protagonist.CHAP-response", "params": {"world_id": "38bf0af045856a2a4688ffc790d402c1", "response": "trees lever trims loxes filly"}, "id": 237}
<--- {"jsonrpc": "2.0", "result": null, "id": 237}

[Noter le Plaintext "trees lever trims loxes filly" quelque part.]
[Noter le CipherText associé à "U2FsdGVkX1+nH9rYtEFp/PADwdT/aLalA/NT7FkPp2Rs7orZEpe9WpbDEfapMOiG\n" quelque part.]

[Sortir du labo]
[Aller à la bibliothèque pour récupérer le Cambridge dictionnary pour trouver le mdp d'emmalyn87 qui est sa clé privée]

[Plan de la bibliothèque]:
>>> plan
BIBLIOTHÈQUE
============
                      [niveau SB]
                           |
                    hall d'entrée 
                           ┊
   aile ouest --------- intérieur --------- aile est 
       |                                        |
 accès réserve                           bureau du directeur 

[ATTENTION ! IL FAUT ALLER SUR LE TERMINAL UBUNTU POUR POUVOIR AVOIR 40 LIGNES DE TERMINAL ET AINSI POUVOIR VOIR LE CATALOGUE]

>>> catalogue
                    Active user: AdrienPanguel
                    Login protocol: plain
                                                                    Catalog
                                                                    -------
U  0. fascicule du nouvel arrivant
U  1. description du protocole telnet
U  2. spécification de l'authentification CHAP
U  3. Cambridge English dictionary
   4. guide OpenSSL (tome I) : chaînes de caractères
   5. guide OpenSSL (tome II) : chiffrement symétrique
   6. guide OpenSSL (tome III) : génération d'une paire de clef
   7. guide OpenSSL (tome IV) : chiffrement à clef publique
   8. guide OpenSSL (tome V) : signature
   9. guide OpenSSL (tome VI) : script d'exemple
U 10. XXXXXX UNAVAILABLE XXXXXX SECURITY TOO LOW XXXXXX
U 11. XXXXXX UNAVAILABLE XXXXXX SECURITY TOO LOW XXXXXX
U 12. XXXXXX UNAVAILABLE XXXXXX SECURITY TOO LOW XXXXXX
U 13. XXXXXX UNAVAILABLE XXXXXX SECURITY TOO LOW XXXXXX
U 14. XXXXXX UNAVAILABLE XXXXXX SECURITY TOO LOW XXXXXX
U 15. XXXXXX UNAVAILABLE XXXXXX SECURITY TOO LOW XXXXXX
U 16. XXXXXX UNAVAILABLE XXXXXX SECURITY TOO LOW XXXXXX
U 17. XXXXXX UNAVAILABLE XXXXXX SECURITY TOO LOW XXXXXX
U 18. XXXXXX UNAVAILABLE XXXXXX SECURITY TOO LOW XXXXXX
U 19. XXXXXX UNAVAILABLE XXXXXX SECURITY TOO LOW XXXXXX
U 20. XXXXXX UNAVAILABLE XXXXXX SECURITY TOO LOW XXXXXX
U 21. XXXXXX UNAVAILABLE XXXXXX SECURITY TOO LOW XXXXXX
U 22. XXXXXX UNAVAILABLE XXXXXX SECURITY TOO LOW XXXXXX
U 23. XXXXXX UNAVAILABLE XXXXXX SECURITY TOO LOW XXXXXX
*** 3                           [Tapper 3 pour récupérer le Cambridge dictionnary]
(type ? for help)
Delivery in progress...

Vous voyez un drone bibliothécaire aller paisiblement chercher votre livre dans les
rayonnages puis se diriger vers la vitre et le déposer sur un plateau glissant où
vous pouvez le récupérer.

[Lire le Cambridge pour avoir accès à la liste des cés à tester naïvement.]
>>> lire Cambridge
C'est un post-it qui dit : "le dictionnaire est trop gros pour être livré
par les drones bibliothécaires ; une édition électronique est disponible
sur le web à l'adresse : https://m1.tme-crypto.fr/words".

[A cette adresse "https://m1.tme-crypto.fr/words", il y a un fichier list_keys.txt avec un grand nombre de clés.]

[Pour tester de façon brute-force toutes les clés dans le fichier list_keys.txt, il faut lancer le code decrypt_ciphertext_brute_force.py en remplaçant bien les valeurs de "CHALLENGE" par "U2FsdGVkX1+nH9rYtEFp/PADwdT/aLalA/NT7FkPp2Rs7orZEpe9WpbDEfapMOiG\n" et de "TARGET" par "trees lever trims loxes filly".]:

python3 decrypt_ciphertext_brute_force.py

[Retour de cette commande]:

Testé 0 mots
Testé 2000 mots
Testé 4000 mots
Testé 6000 mots
Testé 8000 mots
Testé 10000 mots
Testé 12000 mots
Testé 14000 mots
Testé 16000 mots
Testé 18000 mots
Testé 20000 mots
Testé 22000 mots
Testé 24000 mots
Testé 26000 mots
Testé 28000 mots
Testé 30000 mots
Testé 32000 mots
Testé 34000 mots
Testé 36000 mots
Testé 38000 mots
Testé 40000 mots
FOUND PASSWORD: tautologically

[Le mdp du compte de "emmalyn87" est "tautologically".]
[Retourner au laboratoire dans la salle RC-13 pour dévérouiller l'ordinateur avec comme id "emmalyn87" et comme mdp "tautologically"]:
>>> utiliser ordinateur
[security engine] dict.atk:52:1|8afef7978c20be4f9e3061892df1b4cc4bb0b4ab9b9456110cfd18f1f907ebff        [CINQUIEME FLAG !!!]

### FLAG 6: Générateur de clé RSA

>>> conseil
Essayez d'aller jeter un coup d'oeil dans le CICSU (sud-est).

[En(fait, avant d'aller au CICSU, il faut passer par l'Atrium.]



>>> conseil lecteur
Votre carte d'étudiant doit pouvoir être lue par ce lecteur.

>>> carte de l'université
La porte ne s'ouvre pas. Une lumière rouge est allumée sur le lecteur de badge.
Le micro-écran LCD affiche "SMART CARD CONTAINS NO DATA".

>>> conseil
Essayez d'aller faire un petit tour au bâtiment Atrium (est).

[Aller à l'atrium]
>>> e
Vous êtes dans une petite cour avec quelques arbres, un peu de mousse et
quelques fougères.  Cette végétation, et le fait qu'on puisse voir le ciel 
donne à cet endroit une ambiance apaisante.  Côté Ouest se trouve la grille
en fer qui vous sépare du couloir.  Côté Est se trouve un grand bâtiment rouge.
À travers les fenêtre vous voyez ce qui est manifestement une bibliothèque.  
Côté Nord, il y a un mur rouge avec de grandes fenêtres qui donnent sur des 
bureaux.  L'une d'entre elle est mal fermée et vous pourriez passer.
Côté Sud, c'est pareil, mais le mur est gris.  Vous n'en êtes pas vraiment
sûr, mais vous vous demandez s'il n'y avait pas un escalier métallique ici 
avant, conduisant à l'étage du dessus.  Mais en tout cas il n'est plus là.
En levant la tête, vous voyez la barre 54-64 au sud et la barre 54-53 au nord,
mais pas moyen d'accéder à l'étage du dessus depuis cet endroit.

Ici se trouve une serrure sans contact (NFC) sur la grille.

>>> conseil serrure
Avez-vous lu le memento qui est dans la pièce à côté ?

>>> n
Vous entrez dans un bureau partagé, peut-être celui des bibliothécaires.  Il
y a  plusieurs ordinateurs, des livres, des paperasses, une cafetière, etc.
Une porte donne sur un couloir attenant à la bibliothèque, mais elle est 
obstinément fermée.

Ici se trouve un terminal de service.
Ici se trouve un memento pour les employés qui ont un bureau dans ce bâtiment.

>>> lire memento
1. Dans le cadre de notre campagne de communication intitulée
        "une sécurité maximale, mais avec la classe"
   nous vous rappelons que tous les utilisateurs de ce bâtiment
   doivent dorénavant avoir une clef publique RSA qui contient
   la chaîne "+++ATRIUM+++".

2. Cette chaîne promotionnelle doit se trouver à l'intérieur de la clef
   publique ; en particulier, elle ne doit pas être ajoutée au bout d'une
   clef pré-existante.  Autrement dit, ceci n'est pas autorisé :
       -----BEGIN PUBLIC KEY-----
       MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsHyqhsu3IxBYkCifvMrP
       uM/uv0hfq0PHbCfrUxFYooWLm3M0rru5Q+9BKQXqBRLa9iO+Tgn8Sy9+ABz0EJVd
       RRtatBkRj/UG3k+65UMxn5s47It+2sCXrX8TDmqPPtVa8Heo/5pqH1A/0LGj5YRo
       8GT0/ITj40j3I+Kp/1a9qP6+5eAqvUHfpC/hro2OCBAOi4+Q8qB+Zrx3jCa1l4R4
       0zQpvVf0nE+tjt7ZLBqlwKUnEWvVmFYJ3l/dikT9yG7s0UBOhAT8rZmwZVOluYeW
       yuERSus5TJbN8V9XR8q1lk8o7WBxtpyJotf5l/cCdmVlL9cSaZhVx26cAEcZ496z
       2QIDAQAB+++ATRIUM+++
       -----END PUBLIC KEY-----

3. Pour entrer dans le bâtiment ou dans les bureaux, il faut passer son
   badge devant le lecteur NFC.  Le badge doit contenir la clef publique,
   puis l'utilisateur doit réaliser une signature de manière interactive.

4. Pour simplifier la gestion des clefs, les occupants du même bureau 
   ont des clefs publiques RSA qui ont le même modulo (N).

[Exécuter le code test.py pour obtenir une clé privée contenant "+++Atrium+++]

[Lancer le code CreateKeySkPk.py pour obtenir une paire de clé publique.privée dont la publique contient "+++Atrium+++"]

[Retourner à l'Atrium pour dévérouiller]
[Attention, besoin de signer le challenge donné "scrap pions meted fella basks"]:

          printf "scrap pions meted fella basks" > sign_challenge_atrium.txt
          openssl dgst -sha256 -sign sk_atrium.pem -out signature_atrium.bin sign_challenge_atrium.txt
          xxd -p signature_atrium.bin | tr -d '\n'; echo

[Retour de la signature codée avec clé privée]:
    9a5a62705c1a6db1055050840883cc4081d8231b2703b666132bef666c922d4c4f988c69a8c24a23e377ff60f1eb2bb862fed54496ad65717d1a76c025e1796004508fd67b6cf072bf70e3f89fbecd2882dc2cdc4706e5ff7c1bcb1ddab18dfb1580c1142a4c00dc5dcac3aa2766aa83c30e1dcf09bcae3103ebf0afd508151a3629cbc300c9fd00c1b8df1140fd7d2af504ddf9e78e274cb086034160c3bc6326dcdd0eb790c8e5c978219d179ba4a1d3f853416453ef2dc94e170b488147396d4baea29adcd8ed80f1e3b951c9405c52c9e4d2d4e6ce560c8115ae7b1b65ed3bc9f55d0977e4f303cf1729f7975adeee8bda619886c2935be728159a67c878

>>> carte
        challenge: scrap pions meted fella basks

        signature:  9a5a62705c1a6db1055050840883cc4081d8231b2703b666132bef666c922d4c4f988c69a8c24a23e377ff60f1eb2bb862fed54496ad65717d1a76c025e1796004508fd67b6cf072bf70e3f89fbecd2882dc2cdc4706e5ff7c1bcb1ddab18dfb1580c1142a4c00dc5dcac3aa2766aa83c30e1dcf09bcae3103ebf0afd508151a3629cbc300c9fd00c1b8df1140fd7d2af504ddf9e78e274cb086034160c3bc6326dcdd0eb790c8e5c978219d179ba4a1d3f853416453ef2dc94e170b488147396d4baea29adcd8ed80f1e3b951c9405c52c9e4d2d4e6ce560c8115ae7b1b65ed3bc9f55d0977e4f303cf1729f7975adeee8bda619886c2935be728159a67c878

[security engine] rsa.keygen:52:1|2f5271e051f27f3fe91081d084796a47f4bb2af80b87e88f6197f7add482fe94    // 6ème flagggggg

>>> conseil lecteur NFC
Avez-vous lu la doc sur les certificats à la bibliothèque ?

>>> utiliser carte
La porte ne s'ouvre pas. Une lumière rouge est allumée sur le lecteur de badge.
Le micro-écran LCD affiche "DEVICE DOES NOT CONTAIN A CERTIFICATE".

Une lumière verte s'allume sur le lecteur de badge.
La porte vitrée se déverrouille et vous pénetrez à l'intérieur.
(la prochaine fois, au lieu de refaire tout ce cirque, il suffira
(d'utiliser le lecteur de badge et ça suffira).

Vous êtes dans un petit espace gris et bétonné qui sépare le jardinet de
l'intérieur du bâtiment.  Au nord et au sud, il est fermé par deux grilles
métalliques, et le tout fait penser à une cellule de prison.  La personne
qui fait le ménage par ici a pris l'habitude d'y laisser son petit charriot.
Au nord, on peut accéder à un couloir turquoise.

[Aller dans le CICSU]

[Aller dans la bibliothèque et prendre le CHAP]:

[Lire le CHAP]

[Idée: se reconnecter à tellnet]
[identifiant = "AdrienPanguel"]
[mdp = "__CHAP__"]
[Retour terminal]:

                                                      UGLIX v4.0 beta
                                           (Experimental Device Control Terminal)


                                                         CHAP login
                                                         ----------
        username:  AdrienPanguel
        challenge: U2FsdGVkX1/1fiiNcyBYc7VR1+96SdtC2p0tzT+edb8ghJQ68RA2VRQkrH0H5e2j

        response:

[Lancer le code tests_encrypt_decrypt.py en mettant:
          ciphertext = "U2FsdGVkX1/1fiiNcyBYc7VR1+96SdtC2p0tzT+edb8ghJQ68RA2VRQkrH0H5e2j"
          password = [Mon mdp de connexion a tellnet]]:

          python3 tests_encrypt_decrypt.py 
          'U2FsdGVkX1/1fiiNcyBYc7VR1+96SdtC2p0tzT+edb8ghJQ68RA2VRQkrH0H5e2j'
          64
          Decrypted plaintext:
          amply troll morph buffs manta       // C'est le plaintext à entrer comme signature

[Entrer la signature]

                                                    +------------------+
                                                    | Successful login |
                                                    +------------------+

[security engine] chap.login:52:1|879e8a07b5658f7995eec82d86342dcf245d013441a1b4346d03e5171f7e894a    // 7ème flaaaaag

>>> w
Vous êtes dans une espèce de sas qui donne sur le foyer de l'auditorium.
Mais vous en êtes séparée par une porte vitrée qui est fermée.  À travers la
vitre, vous voyez que le foyer est complètement vide.  Sur le mur, une grande
banderole annonce : ``bienvenue à la fête des 25 ans de l'ISIR''.

Ici se trouve un lecteur NFC sur le mur.

>>> carte
La porte ne s'ouvre pas. Une lumière rouge est allumée sur le lecteur de badge.
Le micro-écran LCD affiche "DEVICE DOES NOT CONTAIN A CERTIFICATE".

[Aller à la bibliothèque pour lire la doc sur spécification avec clé publique]

>>> conseil catalogue
Vous pouvez vous connecter avec le protocole à clef publique pour accéder à encore plus de livres.

[Lire Spécification de l'authentification à clef publique]

[Se reconnecter à nouveau]
[identifiant = "AdrienPanguel"]
[mdp = "__PK__"]

                                                                UGLIX v4.0 beta
                                                     (Experimental Device Control Terminal)


                                                                    PK login
                                                                    --------
        username:  AdrienPanguel
        challenge: fader scrub chins divvy amass

        signature:

[Chiffrer avec signature (la clé privée double avec la publique du début)]:
          printf "fader scrub chins divvy amass" > sign_challenge_publique.txt
          openssl dgst -sha256 -sign my_private.pem -out signature_publique.bin sign_challenge_publique.txt
          xxd -p signature_publique.bin | tr -d '\n'; echo

[Retour du mdp chiffré avec la signature]:
170fb097747f0d90053858038ab6c9d82e3b7aebf7dcdcab80f72bb0b34d31b59f1c1059a2dfad84a8acde9b80b087a2cb4e836f00b4d3e7af16c2666bddfefc6ffb4d1df66cc266b2ecaa759dd97e57dc2dbc179f55653a282c8a46bace49fc588d1c34694dbe4ec0bf412ff68b202e139f30cebf37f27e1ce75d3f8f20baa9b98b7ae3806c945a45e8169bfe4bf38e8af4401d004ed8b8db49716725e025e0f645e2bbebfc0097cae79592bcee016e44ed5510308aedffcdcdd8fddac22783355cd585c8b5cf5d805baf91c2a963fb76439c02307e51306f0b7845f6447a90b4c22261e3561dcf78bb9baacf3af3fc168dfb78e80b362584aa3d403ff3b95a


                                                                UGLIX v4.0 beta
                                                     (Experimental Device Control Terminal)


                                                                    PK login
                                                                    --------
        username:  AdrienPanguel
        challenge: fader scrub chins divvy amass

        signature:  170fb097747f0d90053858038ab6c9d82e3b7aebf7dcdcab80f72bb0b34d31b59f1c1059a2dfad84a8acde9b80b087a2cb4e836f00b4d3e7af16c2666bddfefc6ffb4d1df66cc266b2ecaa759dd97e57dc2dbc179f55653a282c8a46bace49fc588d1c34694dbe4ec0bf412ff68b202e139f30cebf37f27e1ce75d3f8f20baa9b98b7ae3806c945a45e8169bfe4bf38e8af4401d004ed8b8db49716725e025e0f645e2bbebfc0097cae79592bcee016e44ed5510308aedffcdcdd8fddac22783355cd585c8b5cf5d805baf91c2a963fb76439c02307e51306f0b7845f6447a90b4c22261e3561dcf78bb9baacf3af3fc168dfb78e80b362584aa3d403ff3b95a

                                                              +------------------+
                                                              | Successful login |
                                                              +------------------+

[security engine] pk.login:52:1|464830fac0d902b1e193a8045a68fef6bdd8222a7e32cf7163a2912ed63eb867    // 8ème flagggggg

[Besoin d'un certificat pour badger correctement au CICSU: le CSR qu'on va créer avec notre clé privée d'Atrium est envoyé au système qui nous retourne le certificat]

[Entrer la commande suivante dans le terminal]:
          openssl req -new -key sk_atrium.pem -batch -subj '/CN=AdrienPanguel' -out adrien.csr.pem

[Le contenu de la demande de CERTIFICATE est dans adrien.csr.pem, le copier]
[Aller au temrinal de l'atrium, coller le ocntneu précédent pour la CERTIFICATE REQUEST]

[Revenir au CICSV et badger]:
>>> carte

Une lumière verte s'allume sur le lecteur de badge.
La porte vitrée se déverrouille et vous pénetrez à l'intérieur.
(la prochaine fois, au lieu de refaire tout ce cirque, il suffira
(d'utiliser le lecteur de badge et ça suffira).

Vous êtes dans le foyer.  Une multitude de spots au plafond diffusent un
éclairage agréable,  et un mur en imitation bois réchauffe un peu 
l'atmosphère.  Les murs de cette grande salle sont tapissés de posters qui 
vantent les travaux des chercheurs de l'Institut des Systèmes Intelligents
et de la Robotique (ISIR).  Apparemment une fête a été organisée ici à 
l'occasion des 25 ans de ce laboratoire.  De nombreux objets qui servent à 
faire des  démonstrations techniques ont été amenés ici pour l'occasion.
À côté du guichet d'acceuil, un escalier monte vers le niveau supérieur (et
la lumière du jour) tandis que des portes battantes conduisent vers le grand
auditorium.

Ici se trouve un ascenseur.
Ici se trouve une borne de mise à jour de firmware.
Ici se trouve un BiblioDrone-NG.
Ici se trouve un Robot gardien.
[security engine] pki.cert:52:1|8fe700cd09c6930261a71d3f75981625b83f3bcd5391b161e280bbbfd4078350    // 9ème flaggggg




[Mettre dans recipient_pub.pem la clé publique fournie par la commande "broadcast" seule effectuée dans le terminal du labo au RC-13]

[Changer le contenu de tests_encrypt_decrypt.py]:
m = "test"
s = "AdrienPanguel123"
print(encrypt(m,s))

[Lancer ce code]:

[Entrer la commande]:
echo -n "AdrienPanguel123" | openssl pkeyutl -encrypt -pubin -inkey recipient_pub.pem | xxd -p | tr -d '\n '

[Retour]:

b5a25a0fce193fe776d3154e1dbe964474392052918e81698b497c3087460f7045bafd1e34b12b350a40b2d8261b120833006ec544caa25e96ec2bec6e3762d1283210a73509289b7431ce18ef025c089a08298ca81ac223add2800e576f5dc28c1a282113e2c898cc7fcc9dafa7ef34ac7bdf34cea344ac607b55cfe5f79f1f66df1e7b405d77e67a76c9652c0958658c121873743c0cc39062290b06c22e1a1738a975884d34a583dd8429c3e221000cf70a362982053634b442dc2bcc3fd63e1c46a37add62b28486cac02de6a23938942949f1c1716e84e911ae92a8e34a56b0d783cbb1084012a47f48f67cd908fe86aed4cccb5830f924dd40059062b5

[Entrer la commande]:
python3 tests_encrypt_decrypt.py

[Retour]:
U2FsdGVkX19jqtLBLFRzg9ioEkZ7jL5MQcr4dfQsVoE=

[Ecrire le .json à partir de ces 2 retours]

>>> terminal
[security engine] hybrid:52:1|ba7c7348d96337ca34e197eea20f768c094e604ceb34844d6e9759d3bf0de937   // 10ème flaggggggg
[9be4862c2ba03242774ab6ecd69a0d95] Bonjour,
                                   
                                   Je suis un programme que mon créateur à conçu pour limiter le flux entrant de
                                   spam.  Conçu dans la philosophie UNIX, je ne fais qu'UNE chose, mais mais je la
                                   fais bien : je laisse passer uniquement les messages qui respectent quelques
                                   règles simples.
                                   
                                   La première de ces règles consiste à m'écrire avec la technique du chiffrement
                                   hybride, ce que vous faites.  Je vous en remercie.
                                   
                                   Cependant, mon créateur aimerait avoir des garanties quant à l'identité de ses
                                   correspondants. Par conséquent, il faudrait que vous ayiez une clef publique
                                   signée par au moins deux autres utilisateurs enregistrés dans la PKI.
                                   Encore une fois, si vous ne voyez pas de quoi je parle, retournez faire un tour
                                   à la bibliothèque. Voici ce qui ne va pas :
                                   - Votre clef publique n'est signée que par un seul utilisateur
                                   
                                   Bien cordialement,
                                   ---
                                   e-secretary v0.4
[1b82b2cf5efbabc003253099d5779b0e] {
                                     "session-key": "b5a25a0fce193fe776d3154e1dbe964474392052918e81698b497c3087460f7045bafd1e34b12b350a40b2d8261b120833006ec544caa25e96ec2bec6e3762d1283210a73509289b7431ce18ef025c089a08298ca81ac223add2800e576f5dc28c1a282113e2c898cc7fcc9dafa7ef34ac7bdf34cea344ac607b55cfe5f79f1f66df1e7b405d77e67a76c9652c0958658c121873743c0cc39062290b06c22e1a1738a975884d34a583dd8429c3e221000cf70a362982053634b442dc2bcc3fd63e1c46a37add62b28486cac02de6a23938942949f1c1716e84e911ae92a8e34a56b0d783cbb1084012a47f48f67cd908fe86aed4cccb5830f924dd40059062b5",
                                     "ciphertext": "U2FsdGVkX19jqtLBLFRzg9ioEkZ7jL5MQcr4dfQsVoE=\n"
                                   }







[Signer avec sa propre clé privée (my_private.pem) la clef publique de qqun: 2 personnes doivent le faire sur ma clé publique]:

[Moi pour victor.zhou]:
openssl dgst -sha256 -sign my_private.pem target_public.pem > signature_target.bin
xxd -p signature_target.bin | tr -d '
cat signature_target.hex
[Moi pour Karim]:

openssl dgst -sha256 -sign my_private.pem target_public2.pem > signature_target2.bin
xxd -p signature_target2.bin | tr -d '
cat signature_target2.hex

[Pour Victor]:

                                                     +-----------------------------------------+
                                                     | new signature by victor.zhou registered |
                                                     +-----------------------------------------+


[Pour Karim]:

                                                        +-----------------------------------+
                                                        | new signature by Karim registered |
                                                        +-----------------------------------+

[Faire un broadcast avec le out.json d'avant]

>>> ordinateur
[security engine] web.of.trust:52:1|f314e4db3ff276736a12d4109325c66c5aab06318dce9fb8eea4ddfa36b2adb5    // 11è flaaaag
[9be4862c2ba03242774ab6ecd69a0d95] 
                                   Bonjour,
                                   
                                   Je vous informe que j'ai relayé votre message à mon créateur.  Merci d'avoir
                                   suivi tout le processus.
                                   
                                   Bien cordialement,
                                   ---
                                   e-secretary v0.4
[d429ca7d004bfa2d302133e49bcc5bd5] {
                                     "session-key": "b5a25a0fce193fe776d3154e1dbe964474392052918e81698b497c3087460f7045bafd1e34b12b350a40b2d8261b120833006ec544caa25e96ec2bec6e3762d1283210a73509289b7431ce18ef025c089a08298ca81ac223add2800e576f5dc28c1a282113e2c898cc7fcc9dafa7ef34ac7bdf34cea344ac607b55cfe5f79f1f66df1e7b405d77e67a76c9652c0958658c121873743c0cc39062290b06c22e1a1738a975884d34a583dd8429c3e221000cf70a362982053634b442dc2bcc3fd63e1c46a37add62b28486cac02de6a23938942949f1c1716e84e911ae92a8e34a56b0d783cbb1084012a47f48f67cd908fe86aed4cccb5830f924dd40059062b5",
                                     "ciphertext": "U2FsdGVkX19jqtLBLFRzg9ioEkZ7jL5MQcr4dfQsVoE=\n"
                                   }

[Il y a 2 individus A(gjohnson) et B(terrymichelle)]:
>>> lire panonceau
Bureau RC-07 (équipe DEV): terrymichelle et gjohnson

[Aller dans le couloir turquoise, puis à l'est pour récupérer le "d" de l'individu B dans un couloir]:
>>> e
Vous êtes dans le hall du bâtiment, au niveau inférieur.  Les murs et le sol
sont peint en rouge pêtant.  Ca fait presque mal aux yeux.  Une cloison vitrée
vous sépare d'une bibliothèque vide au sud.  En levant le nez, vous voyez tous
les étages de couleurs bariolées, ainsi que l'enchevêtrement d'escaliers qui
y conduit.  À ce propos, celui qui vous permettrait de monter au niveau du
dessus a été retiré.  Au Nord, l'espace de restauration est fermé, mais un
couloir jaune donne sur le coin Nord-Est.  Un couloir turquoise débouche côté
Ouest.

Ici se trouve une clef secrète RSA qui traine dans un coin.

[security engine - WARNING] new security event
                                subject: AdrienPanguel
                                nature: unauthorized physical access
                                location:
                                  floor: SB
                                  room-name: SB_ATRIUM_HALL
                                severity: medium
                                
username: terrymichelle
d       : 4aeb9f587154bd8c124d3b33102ca26b35330e07e29476f8e256fc8bbc3181727348268bdc52032eeeb3cabe8542f189441dd3fed32b7a78f88a6cd43e6d0bccfc2664b957c7c5111711484ab2ee6b78fd8949d82ad7367e972ac3e3b7d981302395579c83dd14d8646956f641261af3deebe715ce95ee77ee3fff133cb850655d46fb9aaeba0d179df907c85911099b72a7ffebc8bab69829e222bbaa9056b0d520cac5d02e5b23bcdbe35ef32bebdeffaa12aea5d2166f5961a78fc85eb8bf01dddfca7b7892c04785113ca07aed262e946fe6052d47767918cd8b155f775c7caef1f4c2445059975fa2953cd9cc7bd3cada81313fb4d9916aab7563e3d5ed
[C'est le d]

[On récupère ensuite sa clé publique pkB sur le terminal]
[Maintenant qu'on connaît N, e, d, on peut en déduire sa clé privée skB]:
[Code test2.py donne la factorisation de N=p*q]
[Code test3.py donne N, phi(N) et d à partir de p et q]
[Code test4.py donne la clé privée de terrymichel]:
-----BEGIN PRIVATE KEY-----
MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDQ4o+MQYLsxmqE
mxhg7lxIrjGQqZOt+Gmh4ooCUVebKxr5zL35agV8s4HPWooujNSzWRpPg6ScLUh8
N/3zHUqs/LedjkbIh3LZNuh6rl8D4Zk3imZ50D2QNYgeFpTq2g5vUmT/nfEaREES
HAmO8FqFujeSiADHik6IUGDlI1Dv1mNsJ0J55TKHiAcR4bMDNPY+fiEz9MOhJlvq
CyJiIj+aVSBraGpnlHJVKAmKl5yknDCb9sz/CJZe4aAY6L7khJ7eV4hKdgrMzbBE
bMD1uzOL+jQpGAovhZPaOvGllvv4ashE+FZbQFVJoM+L7m77yJkcDZgHRcJOf7Ai
XI6B/ycJAgMBAAECggEAKilQqBKhBoGWBmX3qbjyz4i5YGWZ9Udqqs465PTeJeex
bjIxNiJ8MQtabCvuMC8kz35wnRQJKazKMKhsjaGf7QKlXRvWlashN06p5flEHFhw
wJEi1ft+MZlcfBY6wJx6xWVwFVgfzhlwuOMH2t4Qp2VKyjzBS4VTDJiMtjNGpuHV
lpnk0jJxDGNVkaBuxO4ixHreQe7t/l9jwmgFs/ulOZE1Oujhv3nGZ7upHEGGbARH
KfLH9j5m7D7ChJXQy6NSX06gdI06pUksXrCDghcjQWh52eSOgQKa44UewfFXZJZ7
BZ1wW5HHYsPAscSmWZnHKFjVVtKAsLsU2cxlee02sQKBgQDhq9EidH5EvviZKjAT
tPHfee0rJ3AT1qftx8uF8E8FexyhSipH4BdwyRXumn1cGtuq6zio+hvifUMlOc63
pGMgOHndfybZrRyX4GjE9ZVtLkpe6WIrojNxUxG7rawGdpJv0yxsutPjyU1NMg+0
mevSkp9ON46x7Gd4RM0GISNzIwKBgQDs9TfyHUJT6XPpDFkiGtfhOdAnRGLvyP8M
BMJHmfnBLoBHxz/nEfyfDOvFKuJi9NZePq2JpAl6KJKo8ayKqs07Z2AcN87IGuVQ
512pbfF++2EeqqWHH8MUjYIwpSm2xDpbJu4+woVQDIkC0yXd8rJqr4R5CgJRRNZj
Rr0kZSQl4wKBgDH4iebHRO6UGxhPbzXt62FA7nOP2BGMhsLwavDNtbHRARX2BkbE
KGyhGmora3bpu5qtW26Pc31Dn4quskeX7xtDZjjV3xR0cNBwsMJsXxo+FdnOdB6V
XC7L5jFY067asrJwYHXzKNhXyvY9D50+OCn4ra30P3TGlGLdWUjyLZdhAoGAVFEN
j0GKEIHJlOun69LRbns77j0PV3OWDZjD6OaJUIxTaTclLfvggFgArTANTlkAzphO
9+M+3BED3sngM5eDX9fxAxl4owuu/ZLWaSuN+zlH3bmrHOHYcL/Jy7V5mmdIvJal
v/9HoKxVNIQdvVRW2E+MO+Wr3W85Oio5s3Gp4zECgYBoiZG5ooDlmfQW+0EwDP8k
7k9MFXgQ1HLNTCVU69i8/jD7JT3KqsqnV33c7d+Gou5Q/HJELRyp2fyQiJcdziH0
Wlt1sk1FtD2KrCl37tsO2/E5CDFXP/YlOJy/T/Bc51RMPZjsLQ/+/GyIFbBZ6zf9
wgcM14V3PE6kfZGSSpEL5Q==
-----END PRIVATE KEY-----

[On upload data la clé publique pkB sur notre carte étudiant]
[On badge dans le couloir turquoise, mais l'individu B a été révoqué]:
>>> carte
La porte ne s'ouvre pas. Une lumière rouge est allumée sur le lecteur de badge.
Le micro-écran LCD affiche "terrymichelle's key has been revoked (reason: secret key lost)".

[Comme on sait que l'individu A a le même N (et sûrement des p et q différents) de l'individu B]
[Lancer le code test2A.py pour récupérer la clé privée skA de l'individu A dans skA.pem]:
-----BEGIN PRIVATE KEY-----
MIIE2QIBADANBgkqhkiG9w0BAQEFAASCBMMwggS/AgEAAoIBAQDQ4o+MQYLsxmqE
mxhg7lxIrjGQqZOt+Gmh4ooCUVebKxr5zL35agV8s4HPWooujNSzWRpPg6ScLUh8
N/3zHUqs/LedjkbIh3LZNuh6rl8D4Zk3imZ50D2QNYgeFpTq2g5vUmT/nfEaREES
HAmO8FqFujeSiADHik6IUGDlI1Dv1mNsJ0J55TKHiAcR4bMDNPY+fiEz9MOhJlvq
CyJiIj+aVSBraGpnlHJVKAmKl5yknDCb9sz/CJZe4aAY6L7khJ7eV4hKdgrMzbBE
bMD1uzOL+jQpGAovhZPaOvGllvv4ashE+FZbQFVJoM+L7m77yJkcDZgHRcJOf7Ai
XI6B/ycJAh4zg1Q7Hy5VE8NCJKRBFWdnAAAAAD774BNEhQz774ECggEAPaMe/Sby
sjWADzxI1RDMkOwG+6wbCsQEptZhS9UJFAwH7uBvxWAeIPy6aFvK295WF+/EiBrH
4076XVel1Z9FwTO4X2JhUid8syPaGz8bO9ombnX5l9GLpyFZx9SxfOaTrYoz8xdl
sx78IlDDuXcAlhnEtq0fARA3I5lCWuWYAnKYqR2UzYE4l7JS2lYugSOJBeGg/KIW
HTcLW8vjCDdWYQBjuJ4V02apSTpMXzAZcW7SRjjvQspZ7eWvYWTXj25UQ3WWmYT8
NYYYfqd6xxucNW7jzUHz2KSmxAfo9amLVPxQIRiLaAqwaX1ejuoE7yIFg9iPib4B
hE27S1pD4NlefwKBgQDhq9EidH5EvviZKjATtPHfee0rJ3AT1qftx8uF8E8Fexyh
SipH4BdwyRXumn1cGtuq6zio+hvifUMlOc63pGMgOHndfybZrRyX4GjE9ZVtLkpe
6WIrojNxUxG7rawGdpJv0yxsutPjyU1NMg+0mevSkp9ON46x7Gd4RM0GISNzIwKB
gQDs9TfyHUJT6XPpDFkiGtfhOdAnRGLvyP8MBMJHmfnBLoBHxz/nEfyfDOvFKuJi
9NZePq2JpAl6KJKo8ayKqs07Z2AcN87IGuVQ512pbfF++2EeqqWHH8MUjYIwpSm2
xDpbJu4+woVQDIkC0yXd8rJqr4R5CgJRRNZjRr0kZSQl4wKBgQDfs9iHQom4z8Bi
CoBGKtrVK6PlpG43GZeLGGax+HRdGC6paV2/Iw33PqoorHg0RBqOTl1gWqGKeocD
Px+lSri+SvJWorYQXr38rxaicBsEbpnGUZCHoFdQNKkmd59BQyYqEGb3u1OJREDf
0zpCf+IDE0B6z6WTEdu1Z7n5RvGxjwKBgQDUn2eq7gXAZk1CAJTwMVwEwMZN+Hyy
JehMG32GcB4JDkrfy+2IePHlN/OkidoPGywQjiE4qL4aFgBny3fnJLLS2+Z0/1ls
GrCZMMFISIrOV0B6Xb7YZ5ze7rvuEvNsQQyPjIX7xdLmT4hBjKOiGvkojSZPv6Cp
Hjao7iL8+tZV4QKBgGiJkbmigOWZ9Bb7QTAM/yTuT0wVeBDUcs1MJVTr2Lz+MPsl
PcqqyqdXfdzt34ai7lD8ckQtHKnZ/JCIlx3OIfRaW3WyTUW0PYqsKXfu2w7b8TkI
MVc/9iU4nL9P8FznVEw9mOwtD/78bIgVsFnrN/3CBwzXhXc8TqR9kZJKkQvl
-----END PRIVATE KEY-----

[Upload en data la clé publique pkA de l'individu A]
[Retourner dans le couloir turquoise et badger]:
>>> carte
        challenge: riven tying motto droid inner

        signature:

[Il faut signer ce texte avec la clé privée de l'individu A skA qu'on vient de trouver]:
printf "riven tying motto droid inner" > sign_challenge2.txt
openssl dgst -sha256 -sign skA.pem -out signature2.bin sign_challenge2.txt
xxd -p signature2.bin | tr -d '\n'; echo
90c351145951d04c4d1f82f9a1ce3f50193be8ab4199b2f0be5591446f82955bd751e4005696277306d7c625a9e7ecf6ddab942e502547822ae067349512a9f12633fe9c97a1f0f7708173f0084eb2c1941389932e606070c4a43a5fb1d2d4425c76ebd1c51c684e57c996c5e29f60238ad3e42b2b24b0545eb3b2facd3e53735a185928f5e3b422c06185b00941fa32db32018c5e1a9f70daca099d4ba46d33720037498dfae9ce7de5d1ebac9f9d4155915cdb963ec2d4bf8c667842e5fbb54efe34b56e3d371790d8a2fa420c94353bfbfd018b676b322f03df859d9e6ec5ba321c5c2087d4ff47570730ea6ce6d5245c77a942efe2ff098b43c7ee840812

[C'est ce qu'il faut mettre dans le champ signature quand le challenge "riven tying motto droid inner" nous était donné]:

>>> carte
        challenge: riven tying motto droid inner

        signature:  90c351145951d04c4d1f82f9a1ce3f50193be8ab4199b2f0be5591446f82955bd751e4005696277306d7c625a9e7ecf6ddab942e502547822ae067349512a9f12633fe9c97a1f0f7708173f0084eb2c1941389932e606070c4a43a5fb1d2d4425c76ebd1c51c684e57c996c5e29f60238ad3e42b2b24b0545eb3b2facd3e53735a185928f5e3b422c06185b00941fa32db32018c5e1a9f70daca099d4ba46d33720037498dfae9ce7de5d1ebac9f9d4155915cdb963ec2d4bf8c667842e5fbb54efe34b56e3d371790d8a2fa420c94353bfbfd018b676b322f03df859d9e6ec5ba321c5c2087d4ff47570730ea6ce6d5245c77a942efe2ff098b43c7ee840812

Une lumière verte s'allume sur le lecteur de badge.
La porte vitrée se déverrouille et vous pénetrez à l'intérieur.
(la prochaine fois, au lieu de refaire tout ce cirque, il suffira
(d'utiliser le lecteur de badge et ça suffira).

Vous êtes dans le bureau d'une équipe de développement.  Le tableau blanc est
rempli de diagrammes représentant des relations entre des classes dans du 
code.  Il y a aussi tout un fatras d'outils, multimètres, etc.

Ici se trouve une firmware update key.
Ici se trouve une spécification du journal des évènements de sécurité (partie I).
[security engine] rsa.reduction:52:1|4ddb32dbdce721e235de3062ab0c652671c08fd6a26524eb8359b2c9472971a3   // 12è flaaaaag




>>> regarder firmware
Elle est écrite sur le coin d'une enveloppe.  Elle dit :
                    firmware update key: 35ba26a3b0297f0d



>>> lire panneau
Il y a des affiches annonçant des colloques de sécurité informatique,
de petites annonces et quelques messages destinés aux utilisateurs des
locaux.  L'un d'entre eux dit notamment :

    MESSAGE IMPORTANT POUR LES UTILISATEURS DE LA SALLE RC-25
    ---------------------------------------------------------

    - ymolina: 3003469a3e8e7efb1e1c3c9011910e0368fd0233b327f34d685d34456fed30f120b7e9056b0af0c0b21c6563e364ee1bc4ded82ef0e35d6231453ae70a329dd31fb21df9d09c75a8677dfaea504260042eece4663ba2f4f7fdcf44a74b36d338bb5e4c525a8d4553153f00ba732285db6c2f3d3f81b9c8f758d7b040f191b6fe5b0f431e8677da5d31b916d7d698353eff389a58f6e64af17aa86bc328ed3c52420a7b2500133e86d1a44bee1ea4ac8b0cdfe24eb9f3f7e2333a9ac36ddee83a2ea38417b1363fbb0973fc9ee1f008101f73e5da85c109d267f3f87807e8a151ab151f34af0db59dc06c0b62acc1ddf41bfab996a468dc466fa5f1d848b955ad
    - jillian47: 52e6a9083f24008cfb7fa3c80fae6bbcaf30165e72fadc0787bb7ce79582134dee51902b4cffc74608e6da9903737c5843dc8d2a8a09c4d29763e02c954a84e06d8d16f019959c64c5578aed978c6df1993092364cc33463d92a4f24312d0c9418d111c4d8225a005c80e7bed639c96d5b260037ace61436ab25e31dfa4118b909e387458140a5fed838ac8872c09cd177905c999e76f1b2f5738cac08ed798270dec991616375775422d6728b4bed8374094a475a40ed58aaa03e26c58a5c368f1666603632c2767d2dab617e67bc54ff7f4c605fe8593c5e865d1bc0150278059115d8ff9d0468a4b15f44e8486930e0a459ac4531650b90a18ed11bef34aa



>>> lire panonceau
Salle RC-25 (équipe SÉCU) : ymolina et jillian47






                                                 UGLIX v4.0 beta                                                  
                                                (Service terminal)                                                

                    Active user: AdrienPanguel

                                               Public-key directory                                               
                                               --------------------                                               



                    Username:                   ymolina

                    Public key:                 
                    -----BEGIN PUBLIC KEY-----
                    MIIBPTANBgkqhkiG9w0BAQEFAAOCASoAMIIBJQKCAQEArGseb911v/OWCUFFgM3G
                    1IJN9DaXLnbNt/wB/Y+OSIIdhuHc0fXMr8F9gZalkUc+KKyh9Ha+R6DD4OngiPik
                    rNMWIXGx92gHQZCH/+W2+hgAN8xwPYXaYsUK/FCQU//M5aTkVtLJQMO5355TubJ6
                    J+x51y0K54ezfuENoEcpK8C+rI8Qr0ju6F2Hs7gmV+XAVThz7Bg/ZlkrnDKDxDhA
                    l28x9EaWvbVmLK0ZAkWQBmWaOF3RIyIoFC6YWytOapNYXsIUae3EyFOeU2fSSjkG
                    Qv6AGwLdHqWDmaQt/uWpQMGYSkJi9ImEVsdNtE7OYwaTfXSdeSDlE6JOfrYLy14U
                    2wIeeAWSlTXUlpaMc8oziaLZzQAAAAA+++ATRIUM+++B
                    -----END PUBLIC KEY-----

                    Signatures:                 NONE






                                                                   UGLIX v4.0 beta                                                                   
                                                                 (Service terminal)                                                                  

                    Active user: AdrienPanguel

                                                                Public-key directory                                                                 
                                                                --------------------                                                                 



                    Username:                   jillian47

                    Public key:                 
                    -----BEGIN PUBLIC KEY-----
                    MIIBPTANBgkqhkiG9w0BAQEFAAOCASoAMIIBJQKCAQEArGseb911v/OWCUFFgM3G
                    1IJN9DaXLnbNt/wB/Y+OSIIdhuHc0fXMr8F9gZalkUc+KKyh9Ha+R6DD4OngiPik
                    rNMWIXGx92gHQZCH/+W2+hgAN8xwPYXaYsUK/FCQU//M5aTkVtLJQMO5355TubJ6
                    J+x51y0K54ezfuENoEcpK8C+rI8Qr0ju6F2Hs7gmV+XAVThz7Bg/ZlkrnDKDxDhA
                    l28x9EaWvbVmLK0ZAkWQBmWaOF3RIyIoFC6YWytOapNYXsIUae3EyFOeU2fSSjkG
                    Qv6AGwLdHqWDmaQt/uWpQMGYSkJi9ImEVsdNtE7OYwaTfXSdeSDlE6JOfrYLy14U
                    2wIeEHF4fObeyNHi52X48UNQQQAAAAA+++ATRIUM+++B
                    -----END PUBLIC KEY-----

                    Signatures:                 NONE