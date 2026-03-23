# Procédure Journey

## Informations sur le site:
https://m1.tme-crypto.fr/

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

### FLAG 1: S'enregistrer sur le registre des participants pour sauvegarder sa progression

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
[A chaque nouvelle connexion, ces livres reviennent dans cette salle.]

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

### FLAG 2: Chiffrement asymétrique (RSA)

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

[Sauvegarder cette Public key dans un fichier ./Keys/PublicKeys/pk_pki_tutorial.pem]
[Lancer le code sign_plaintext_with_pk.py pour chiffrer le texte "I got it!" avec cette clé pk_pki_tutorial.pem avec la commande suivante]:

python3 encrypt_plaintext_with_pk.py

[Ou bien exécuter les commandes suivantes dans le terminal directement]:

printf "I got it!" > ./Texts/msg_pki_tutorial.txt

openssl pkeyutl -encrypt -pubin -inkey ./Keys/PublicKeys/pk_pki_tutorial.pem -in ./Texts/msg_pki_tutorial.txt -out ./Binary/msg_pki_tutorial.bin

xxd -p ./Binary/msg_pki_tutorial.bin | tr -d '\n' > ./Hexa/msg_pki_tutorial.hex;

cat ./Hexa/msg_pki_tutorial.hex

[Retour de ces commandes]:

55df8f73c2663597b98426d51f093244e362df0f37b38bb71d43f6e17c2435b9d687a663daad8296727ef61afeed735b4a9a180468151326889adb792d1c6d660521f289168a1db2bc26a095e96947461a900e76e7ddfaf2bcaa9ac336b9a5cade4bc262cbd178994b7a5e5194cb2300eabe804faa61466627f25844be746d383d491793df8888af52250f07f4d098a9450c8e82d6dae81484e2c1708ab13c404c92f00d25b71b1a529e0555fb7ed2afbf49254774aecd700c062dae5f892fd95c1c5e4970a90e25a0fc1c62d4d4a32b14911b2cbeb31de528f35ab9760b25e8062efd12b2405e1355968921bdea1fa082842f20be7bcb8f12f57307867b4f10

[Remarque: cette sortie sera toujours différente d'une fois sur l'autre, car le chiffrement est probabiliste et non déterministe.]
[Copier-coller ce retour dans la case du "3. Tutorial" après "Ciphertex:"]

                                                               +--------------------+
                                                               | TUTORIAL COMPLETED |
                                                               +--------------------+

[Le tutoriel est terminé.]

[security engine] pki.tutorial:52:1|8d3a204ece50cdea3d35d5c16bca71d7961841a01f1071dbafd6dc5a441da049      [DEUXIEME FLAG !!!]

### FLAG 3: Générer ma paire de clé RSA publique/privée

[ Lancer le code generate_pk_sk_rsa.py pour générer notre paire de clé RSA publique/privée avec la commande suivante]:

python3 generate_pk_sk_rsa.py

[Ou alors générer notre clé privée avec les commandes suivantes]:

openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:2048 -out ./Keys/PrivateKeys/my_sk.pem

[Puis en extraire notre clé publique avec la commande suivante]:

openssl pkey -in ./Keys/PrivateKeys/my_sk.pem -pubout -out ./Keys/PublicKeys/my_pk.pem

[En revenant à "1. Upload public-key", copier-coller cette clé publique]:

[security engine] pki.upload:52:1|a75e2154fd95ebaefb63cb2d469d9d40062e3e32dce8c339b154f634d8f0eeb1        [TROISIEME FLAG !!!]

### FLAG 4: Signer un message avec ma clé privée

[Retourner dans le local électrique]

[Lancer le code "sign_challenge_sk_rsa.py" pour signer le challenge donné avec ma clé privée avec la commande suivante]:

python3 sign_challenge_sk_rsa.py

[Ou bien, signer avec my_sk.pem le challenge donné "twerp reply visor ahead churl" avec les commandes suivantes]:

printf "twerp reply visor ahead churl" > ./Texts/sign_challenge1.txt

openssl dgst -sha256 -sign ./Keys/PrivateKeys/my_sk.pem -out ./Binary/sign_challenge1.bin ./Texts/sign_challenge1.txt

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

[Cette ouverture du terminal n'est pas nécessaire, mais elle est rigolote car je peux communiquer avec d'autres gens ;)))]
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

[Sortir du labo.]
[Aller à la bibliothèque pour récupérer le Cambridge dictionnary pour trouver le mdp d'emmalyn87 qui est sa clé privée.]

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
[Retourner au laboratoire dans la salle RC-13 pour dévérouiller l'ordinateur avec comme id "emmalyn87" et comme mdp "tautologically".]

[security engine] dict.atk:52:1|8afef7978c20be4f9e3061892df1b4cc4bb0b4ab9b9456110cfd18f1f907ebff        [CINQUIEME FLAG !!!]

### FLAG 6: Générateur de clé RSA

>>> conseil
Essayez d'aller jeter un coup d'oeil dans le CICSU (sud-est).

[En fait, avant d'aller au CICSU, il faut passer par l'Atrium.]

>>> conseil lecteur
Votre carte d'étudiant doit pouvoir être lue par ce lecteur.

>>> carte de l'université
La porte ne s'ouvre pas. Une lumière rouge est allumée sur le lecteur de badge.
Le micro-écran LCD affiche "SMART CARD CONTAINS NO DATA".

>>> conseil
Essayez d'aller faire un petit tour au bâtiment Atrium (est).

[Aller à l'atrium et lire le memento]:
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

[Exécuter le code build_sk_pk_atrium.py pour obtenir une paire de clé publique/privée pk_atrium.pem/pk_atrium.pem dont la clé publique contient le chaîne "+++Atrium+++".]

[Clé publique pk_atrium.pem]:

-----BEGIN PUBLIC KEY-----
MIIBSjANBgkqhkiG9w0BAQEFAAOCATcAMIIBMgKCAQEAylenaYAFrVc6xJEu9/lx
xTdyfzDdfBPaXBctZlu5JzTlaDx3GKN9xC+O/vSp6vZAbBeXEQFNW106YygUfTDo
3H+w3O9uTUUv88dWSSuXGW0wyaIeNy0IeBPlVDYerLSyKvGaFhO0AC+G8J1qJYzP
lpE8qexI7ypnzoejfz8d9gcltCVYvqBQZStiISQTp+RpELE1AfDbswzeTbTZRsoT
Pu/oQ4V1o9HhHGURsorctszBnxWRkNBSt0Jw8EsbBsI3kwQGBmqGtqmrMktKThdD
41dXJ7g2Fg2Zc+2ePL7nIbHp6jsdnp8wEGXhdW2KN48hcPgxHS80Tu0bpfpTAxn+
hwIrEkmtJZTDfOsLJ4TEzgvzis5AjiEafKqyQwioLo8QAAAA+++ATRIUM+++AQ==
-----END PUBLIC KEY-----

[Clé privée sk_atrium.pem]:

-----BEGIN PRIVATE KEY-----
MIIE5QIBADANBgkqhkiG9w0BAQEFAASCBM8wggTLAgEAAoIBAQDKV6dpgAWtVzrE
kS73+XHFN3J/MN18E9pcFy1mW7knNOVoPHcYo33EL47+9Knq9kBsF5cRAU1bXTpj
KBR9MOjcf7Dc725NRS/zx1ZJK5cZbTDJoh43LQh4E+VUNh6stLIq8ZoWE7QAL4bw
nWoljM+WkTyp7EjvKmfOh6N/Px32ByW0JVi+oFBlK2IhJBOn5GkQsTUB8NuzDN5N
tNlGyhM+7+hDhXWj0eEcZRGyity2zMGfFZGQ0FK3QnDwSxsGwjeTBAYGaoa2qasy
S0pOF0PjV1cnuDYWDZlz7Z48vuchsenqOx2enzAQZeF1bYo3jyFw+DEdLzRO7Rul
+lMDGf6HAisSSa0llMN86wsnhMTOC/OKzkCOIRp8qrJDCKgujxAAAAD774BNEhQz
774BAoIBAEsTPzD8IRIFX6jzwgVFJVhaINZbOrtg6i+CvYwfm6yQnL2XLnjk6FFb
2VYssWbTdW2nyFpTTERc2Tn4rffjqRwTpISIvOVxfstIOGB5dPnR5/kFCD/v5aYu
/IVUIdKJsp41pzcCSe1ufWMA8w7V5WONBVyfOqsprEw4ats8H9DT952B5IdSr1k1
l5fXveVg6Hz/d4IJFn8G/RRzXZxBf4pDgyyK5b95AQl8/2tdP/f4epgNF2pQuGHh
7ooGAA/9gTB6OnnQGOREIUd2El/jGMhm1gtHqyi0S3iyzJKOk0fqkghr08VkbeKZ
KLmqlW/3I9Z/aRgnfODVEvkQBIkIi/UCgYEA1Hsl9oNGm63vgy1S5fZn2E15zczR
sLf7vndzAz34BLZ07gVi7fO7hWoUdxx8POEr3spCwO8V0hoPW9VqLgMs5Cg28vcG
/mHuEh81Xy4A6ZJ4DvUR3RCaHNFbY7qg11xZ8hquFsTffXpBgt4Bg4ASMne71kk1
9mkMUrBEultGnqUCgYEA88jp73jYVtdUlvvPZYYaBj8oViDBDubjjIL8xXxd4Tpz
FeQXBxdHrw+OjPq7G++RPp9+KsaNj0jFRb6ZvRGke6s0nvuQnxBAHsayShonoXKY
jOpn5gam/+3QtW35c9QxNDDqsNxUEu3Y8JHauotqdqCyCTfuKS5X+/sqFjv07LsC
gYAI8/tYNIqSbVOIpYH3Sxul8ChV+SAc7Gw37SvX0OvS0d5Nw4XpbLOmVBg5cewK
SX8R630ZjjF/aAK9L1r7ahOYH0MXKqXDMiWQo3C2jjkRx8tSpyyZ4VcpwxRuH6/y
PRnv60p5SYicSYA3b9YbpG61VcxYeNq+DFQlh/pqvkkuiQKBgQCu5lSRpEYI1Jop
chyvfoKmJ+d6pRwG/71QNvkK1j8OVslARNAdOb339HezKUiSFw14USx4UeKI/zNe
CbZETpvlJWrrxrBusbiLyoEoJxT9rP3ET4QjbEe73KEX78Vwz4ZbzFHn4FpDzGNs
dw41HHPDd/oikTSiAtBhjUiqPNijLwKBgEcK/zqDMZbLd9z5Muw9vmO42Jw/npVU
iCdWRjM9qzMhc5R985AgCTJ5q9MQ8d1fXkPUhUpVndsrfSEIXuY9SF3woi+EV/v/
GRnNhynqJ2tXBI9ZESXuv7VvnpJiSyu/TDWuka7GOKWvoBy8e0z8M73VolPV8Hga
bhKjQnE1MFEi
-----END PRIVATE KEY-----

[Ecrire cette clé publique pk_atrium.pem dans ma carte étudiante avec upload data.]
[Attention, il faut signer le challenge donné "scrap pions meted fella basks" avec la clé privée sk_atrium.pem]:

printf "scrap pions meted fella basks" > ./Texts/sign_challenge_atrium.txt

openssl dgst -sha256 -sign ./Keys/PrivateKeys/sk_atrium.pem -out ./Binary/sign_challenge_atrium.bin ./Texts/sign_challenge_atrium.txt

xxd -p ./Binary/sign_challenge_atrium.bin | tr -d '\n' > ./Hexa/sign_challenge_atrium.hex

cat ./Hexa/sign_challenge_atrium.hex

[Retour de ces commandes]:

9a5a62705c1a6db1055050840883cc4081d8231b2703b666132bef666c922d4c4f988c69a8c24a23e377ff60f1eb2bb862fed54496ad65717d1a76c025e1796004508fd67b6cf072bf70e3f89fbecd2882dc2cdc4706e5ff7c1bcb1ddab18dfb1580c1142a4c00dc5dcac3aa2766aa83c30e1dcf09bcae3103ebf0afd508151a3629cbc300c9fd00c1b8df1140fd7d2af504ddf9e78e274cb086034160c3bc6326dcdd0eb790c8e5c978219d179ba4a1d3f853416453ef2dc94e170b488147396d4baea29adcd8ed80f1e3b951c9405c52c9e4d2d4e6ce560c8115ae7b1b65ed3bc9f55d0977e4f303cf1729f7975adeee8bda619886c2935be728159a67c878

[Signer le challenge de l'atrium avec ce retour.]

[security engine] rsa.keygen:52:1|2f5271e051f27f3fe91081d084796a47f4bb2af80b87e88f6197f7add482fe94      [SIXIEME FLAG !!!]

### FLAG 7: Connexion CHAP

>>> conseil catalogue
Vous pouvez vous connecter avec le protocole à clef publique pour accéder à encore plus de livres.

[Aller dans la bibliothèque lire le livre sur le CHAP "Protocole CHAP (Challenge Handshake Authentication Protocol)".]
[Il faut se déconnecter, et entrer comme id = "AdrienPanguel" et mdp = "__CHAP__".]:

                                                      UGLIX v4.0 beta
                                           (Experimental Device Control Terminal)

                                                         CHAP login
                                                         ----------
        username:  AdrienPanguel
        challenge: U2FsdGVkX1/1fiiNcyBYc7VR1+96SdtC2p0tzT+edb8ghJQ68RA2VRQkrH0H5e2j

        response:

[Il faut déchiffrer ce challenge avec mon mot de passe de connextion à tellnet.]
[Lancer le code decrypt_ciphertext_challenge_CHAP.py en mettant:
- ciphertext = "U2FsdGVkX1/1fiiNcyBYc7VR1+96SdtC2p0tzT+edb8ghJQ68RA2VRQkrH0H5e2j"
- password = <Mon mdp de connexion à tellnet> avec la commande]:

python3 decrypt_ciphertext_challenge_CHAP.py

[Retour de la commande]:

Decrypted plaintext:
amply troll morph buffs manta

[Entrer ce Plaintext.]
                                                    +------------------+
                                                    | Successful login |
                                                    +------------------+

[security engine] chap.login:52:1|879e8a07b5658f7995eec82d86342dcf245d013441a1b4346d03e5171f7e894a    [SEPTIEME FLAG !!!]

### FLAG 8: Connexion PK

[ATTENTION, VOIR SI IL FAUT FAIRE CHAP ET PK AVEC UN CODE OU JUSTE AVEC LES COMMANDE DU TYPE OPENSSL, XXD, ...]

>>> conseil catalogue
Vous pouvez vous connecter avec le protocole à clef publique pour accéder à encore plus de livres.

[Aller dans la bibliothèque et lire le livre "Spécification de l'authentification à clef publique"]
[Il faut se déconnecter, et entrer comme id = "AdrienPanguel" et mdp = "__PK__".]:

                                                                UGLIX v4.0 beta
                                                     (Experimental Device Control Terminal)

                                                                    PK login
                                                                    --------
        username:  AdrienPanguel
        challenge: fader scrub chins divvy amass

        signature:

[Lancer le code sign_challenge_PK_rsa.py pour signer le challenge avec ma clé privée avec la commande suivante]:

python3 sign_challenge_PK_rsa.py

[Ou bien signer ce challenge avec ma clé privée my_sk.pem avec les commandes suivantes]:

printf "fader scrub chins divvy amass" > ./Texts/sign_challenge_PK.txt

openssl dgst -sha256 -sign ./Keys/PrivateKeys/my_sk.pem -out ./Binary/sign_challenge_PK.bin ./Texts/sign_challenge_PK.txt

xxd -p ./Binary/sign_challenge_PK.bin | tr -d '\n' > ./Hexa/sign_challenge_PK.hex

[Retour de la commande]:

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

[security engine] pk.login:52:1|464830fac0d902b1e193a8045a68fef6bdd8222a7e32cf7163a2912ed63eb867        [HUITIEME FLAG !!!]

### FLAG 9: Certificat

>>> conseil lecteur NFC
Avez-vous lu la doc sur les certificats à la bibliothèque ?

>>> carte
La porte ne s'ouvre pas. Une lumière rouge est allumée sur le lecteur de badge.
Le micro-écran LCD affiche "DEVICE DOES NOT CONTAIN A CERTIFICATE".

[Aller à la bibliothèque pour lire le livre "Obtention_de_certificats_avec_openssl".]
[Il faut fournir un certificat pour badger correctement au CICSU: le CSR qu'on va créer avec notre clé privée d'Atrium est envoyé au système qui nous retourne le certificat]

[Entrer la commande suivante dans le terminal]:

openssl req -new -key ./Keys/PrivateKeys/sk_atrium.pem -batch -subj '/CN=AdrienPanguel' -out ./Certificates/certificate_atrium.csr.pem

[Dans le terminal de l'atrium, coller le contenu de certificate_atrium.csr.pem pour la CERTIFICATE REQUEST]

[Revenir au CICSV et badger la carte]:

[security engine] pki.cert:52:1|8fe700cd09c6930261a71d3f75981625b83f3bcd5391b161e280bbbfd4078350        [NEUVIEME FLAG !!!]

### FLAG 10: Chiffrement hybride & Broadcast

[Aller au labo dans la salle RC-13.]
[Ouvrir le terminal et faire un broadcast.]
[Le retour du broadcast est un message d'erreur qui affiche une clé publique]:

[J'ai oublié de copier ce message mais la clé publique est]:

-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA4eoFrNMkh5+IQHGnGr52
4NexIMuA0RaVDDTpbCqSTEwIsCn9mMVHDnPBMKrhfvJN0POYAsy2SYjEkliYjJxT
2rbrOxEQmQ9hj48Njn23u6H5udmSNNzstlx7+Zwpq6j/VzizL3OeT+GjlVf+RzSG
9rthA1vVoieO04DjjRjmOFPV26f7n+++96BVcLgr3OkP9KVvpt9AvX0eS+yb7DTW
03nVJzSmZ6jrzFNPWovTjEVWscDoZNCBgsYmMjpFQ+zNMO+SbegHr6K8YHZu3tOg
16ilP/r3Mfi7c0x/CkQY4G/WPzFzzhZ8WkpcMTgTsfbXHKhTe8kRglXCi3XOVXQQ
twIDAQAB
-----END PUBLIC KEY-----

[Mettre cette clé publique dans le fichier ./Keys/PublicKeys/pk_broadcast.pem.]

[Lancer le code build_session_key.py pour obtenir la session_key à partir d'un message clair choisi "AdrienPanguel123" avec la commande]:

python3 build_session_key.py

[Ou bien obtenir la session-key à partir de cette clé publique avec les commandes suivantes]:

echo -n "AdrienPanguel123" | openssl pkeyutl -encrypt -pubin -inkey ./Keys/PublicKeys/pk_broadcast.pem | xxd -p | tr -d '\n ' > ./Keys/session_key.pem

cat ./Keys/session_key.pem

[Retour de ces commandes]:

b5a25a0fce193fe776d3154e1dbe964474392052918e81698b497c3087460f7045bafd1e34b12b350a40b2d8261b120833006ec544caa25e96ec2bec6e3762d1283210a73509289b7431ce18ef025c089a08298ca81ac223add2800e576f5dc28c1a282113e2c898cc7fcc9dafa7ef34ac7bdf34cea344ac607b55cfe5f79f1f66df1e7b405d77e67a76c9652c0958658c121873743c0cc39062290b06c22e1a1738a975884d34a583dd8429c3e221000cf70a362982053634b442dc2bcc3fd63e1c46a37add62b28486cac02de6a23938942949f1c1716e84e911ae92a8e34a56b0d783cbb1084012a47f48f67cd908fe86aed4cccb5830f924dd40059062b5

[Puis lancer le code encrypt_plainttext_session_key.py pour chiffrer un message clair choisi "test" avec le message clair "AdrienPanguel123" avec la commande suivante]:

python3 encrypt_plaintext_session_key.py

[Retour de la commande]:

U2FsdGVkX19jqtLBLFRzg9ioEkZ7jL5MQcr4dfQsVoE=

[Ecrire le .json à partir de ces 2 retours comme suit]:

{
  "session-key": "b5a25a0fce193fe776d3154e1dbe964474392052918e81698b497c3087460f7045bafd1e34b12b350a40b2d8261b120833006ec544caa25e96ec2bec6e3762d1283210a73509289b7431ce18ef025c089a08298ca81ac223add2800e576f5dc28c1a282113e2c898cc7fcc9dafa7ef34ac7bdf34cea344ac607b55cfe5f79f1f66df1e7b405d77e67a76c9652c0958658c121873743c0cc39062290b06c22e1a1738a975884d34a583dd8429c3e221000cf70a362982053634b442dc2bcc3fd63e1c46a37add62b28486cac02de6a23938942949f1c1716e84e911ae92a8e34a56b0d783cbb1084012a47f48f67cd908fe86aed4cccb5830f924dd40059062b5",
  "ciphertext": "U2FsdGVkX19jqtLBLFRzg9ioEkZ7jL5MQcr4dfQsVoE=\n"
}

[Faire un broadcast dans le terminal de RC-13 en collant le contenu du fichier out.json précédent dans le message.]

[security engine] hybrid:52:1|ba7c7348d96337ca34e197eea20f768c094e604ceb34844d6e9759d3bf0de937          [DIXIEME FLAG !!!]

### FLAG 11: Signature collective

[Retour automatique du broadcast précédent]:

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

[Il faut faire signer ma propre clé publique my_pk.pem par deux personnes avec leur propre clé privée: victor.zhou & Karim]:

[Lancer le code sign_friends.py pour signer la clé publique d'un collègue avec ma clé privée avec la commande suivante]:

python3 sign_friends.py


[Ou bien signer pour victor.zhou avec les commandes suivantes]:

openssl dgst -sha256 -sign ./Keys/PrivateKeys/my_sk.pem ./Keys/PublicKeys/pk_friend1.pem > ./Binary/sign_friend1.bin

xxd -p ./Binary/sign_friend1.bin | tr -d '\n' > ./Hexa/sign_friend1.hex

cat ./Hexa/sign_friend1.hex 

[Retour de ces commandes]:

7729ef84020a7c91ea3297a88a12e0775345489f9135277e8c4c5366498bc019b2b2219a8954e9e4b271cd62b470f967924ac5f4a2910a9d69c5fde84a1b4bcc9ada18d87c9b4b051457c27301c09d617055146a3d8bc9bd5eee7c466c9cea39eb9ec4d0fc1a3ff347c516207b8ff6573f50e59ba12132b0460f23d41065ac7744a0607d5499b51d44c5f293ea0131355f32826252e6ce6004802da40f34f9bf37c83ae361795c723938871e0a6761e4738157bc118b29f35f47d543f4a56f3b16909c891fb1fb01cc98c92acd9f4b0d9b22238d7c3df7080ce22215248d113ea8513e6b710171688ee42370d59d05baf732161693b95f33d662dc42beccc684

[Je signe pour Karim]:

openssl dgst -sha256 -sign ./Keys/PrivateKeys/my_sk.pem ./Keys/PublicKeys/pk_friend2.pem > ./Binary/sign_friend2.bin

xxd -p ./Binary/sign_friend2.bin | tr -d '\n' > ./Hexa/sign_friend2.hex

cat ./Hexa/sign_friend2.hex

[Retour de ces commandes]:

10340695a25a8df2b7a471e52b7cbcffeef2e5876e41e1cf948fc87760cf17534dcd1a8cdebf267920c0994ef15d6df9b2ac19e4dcd03acc6ea1cef137afc71d6f9b48f74655e4eba01b4566085be037aecd0e4dea76cc9735ef23184c50ef4d62c12f1fc966a59d56e84f10c3ef0d20c7f63b23ab13b411866f0bbc2628e5110f3a27719c8b71eff7e31cfc5dd9f3ad04d6c2a7b279518a06643e0e5c67b6d5ef726d376253ea79403cbe19223dea7ed75b3648846e020b39be3121c9a0f39bd0c8c8b291850c562daad419c195ec2a45d267eb743cfdab469e397ac6f08424d5a32443c943cb880fd59352bf4051eed777119e32cbfc60943d69f60f6626dd

[Upload la signature faite par victor.zhou de ma clé publique.]
                                                     +-----------------------------------------+
                                                     | new signature by victor.zhou registered |
                                                     +-----------------------------------------+

[Upload la signature faite par Karim de ma clé publique.]
                                                        +-----------------------------------+
                                                        | new signature by Karim registered |
                                                        +-----------------------------------+
[Faire exactement le même broadcast qu'avant.]

[security engine] web.of.trust:52:1|f314e4db3ff276736a12d4109325c66c5aab06318dce9fb8eea4ddfa36b2adb5    [ONZIEME FLAG !!!]

### FLAG 12: Shared modulus Attack (RSA) avec fuite de  Private Key

[Retour automatique du broadcast précédent]:

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

[Idée: Il y a 2 individus A(gjohnson) et B(terrymichelle) dont on doit trouver les clés privées à partir du "d" trouvé appartenant à terrymichelle.]

[Lire le panonceau pour connaître les deux personnes.]
>>> lire panonceau
Bureau RC-07 (équipe DEV): terrymichelle et gjohnson

[Aller à l'Atrium dans le couloir turquoise, puis à l'est pour récupérer le "d" de l'individu B dans un couloir]:
>>> voir clef
username: terrymichelle
d       : 4aeb9f587154bd8c124d3b33102ca26b35330e07e29476f8e256fc8bbc3181727348268bdc52032eeeb3cabe8542f189441dd3fed32b7a78f88a6cd43e6d0bccfc2664b957c7c5111711484ab2ee6b78fd8949d82ad7367e972ac3e3b7d981302395579c83dd14d8646956f641261af3deebe715ce95ee77ee3fff133cb850655d46fb9aaeba0d179df907c85911099b72a7ffebc8bab69829e222bbaa9056b0d520cac5d02e5b23bcdbe35ef32bebdeffaa12aea5d2166f5961a78fc85eb8bf01dddfca7b7892c04785113ca07aed262e946fe6052d47767918cd8b155f775c7caef1f4c2445059975fa2953cd9cc7bd3cada81313fb4d9916aab7563e3d5ed

[C'est le "d" de la clé privée RSA de terrymichelle.]

[On récupère ensuite sa clé publique de l'individu B./Keys/PublicKeys/pk_atriumB.pem sur le terminal.]
[On upload data la clé publique pk_atriumB.pem sur notre carte étudiante.]
[On badge dans le couloir turquoise]:
>>> carte
La porte ne s'ouvre pas. Une lumière rouge est allumée sur le lecteur de badge.
Le micro-écran LCD affiche "terrymichelle's key has been revoked (reason: secret key lost)".

[L'individu B a été révoqué.]
[On récupère la clé publique de l'individu A ./Keys/PublicKeys/pk_atriumA.pem sur le terminal.]
[On upload data la clé publique pk_atriuma.pem sur notre carte étudiante.]
[On badge dans le couloir turquoise]:
>>> carte
        challenge: riven tying motto droid inner

        signature:
[Il nous faut la clé privée de l'individu A.]
[Comme on sait que la clé privée de l'individu A a été construite en RSA avec le même N que celle de l'individu B qu'on peut trouver à partir du "d" trouvé par terre, on va faire une attaque par module partagé.]
[Lancer le code shared_modulus_attack.pem pour obtenir la clé privée de A et B avec la commande suivante]:

python3 shared_modulus_and_private_key.py 

[Retour de cette commande]:

nA: 26369288694727461965859708590289658091463732175154308032138028774380676409300900540041160821083421691174067059830604832522548869864198047056431133019235232451549365591799423959140055261430023473294644129834569855113482917282005527873469511429699958233295085969252631487167667017441819506695833869358542769646874235907157769655269237967572699394977581899697144662410505550970106875050305797439659618621848300000752041676321106955498320153065266126654383080277859247453296995289780021183556824372104786636646373588539758168252467305981051351214112809259690598880084730214415703114626961714763354994387473322771084158729

nB: 26369288694727461965859708590289658091463732175154308032138028774380676409300900540041160821083421691174067059830604832522548869864198047056431133019235232451549365591799423959140055261430023473294644129834569855113482917282005527873469511429699958233295085969252631487167667017441819506695833869358542769646874235907157769655269237967572699394977581899697144662410505550970106875050305797439659618621848300000752041676321106955498320153065266126654383080277859247453296995289780021183556824372104786636646373588539758168252467305981051351214112809259690598880084730214415703114626961714763354994387473322771084158729

eA: 355529687253513778402431023126958456006159727346897464347498693183401857
eB: 98669952307735697561566019299547104474489895689553484676473939076676820135809

[*] Factorisation de n en cours...
phi(n): 26369288694727461965859708590289658091463732175154308032138028774380676409300900540041160821083421691174067059830604832522548869864198047056431133019235232451549365591799423959140055261430023473294644129834569855113482917282005527873469511429699958233295085969252631487167667017441819506695833869358542769646549366743941327048416485326950625738725245164262482710962574014962702979049739263433810788815577683701297796890044950072312908757435842321983987195025085462297656397670985949252982038800671170488179517569324031808551794409938755830644814734133080842931667027423267302555014111278537270511975524409563118276100

[+] Succès !
Clé privée A écrite dans: ./Keys/PrivateKeys/sk_atriumA.pem
Clé privée B écrite dans: ./Keys/PrivateKeys/sk_atriumB.pem

[Il faut signer le challenge avec la clé privée de l'individu A qu'on vient de trouver avec les commandes suivantes]:

printf "riven tying motto droid inner" > ./Texts/sign_challenge_atrium2.txt

openssl dgst -sha256 -sign ./keys/PrivateKeys/sk_atriumA.pem -out ./Binary/sign_challenge_atrium2.bin ./Texts/sign_challenge_atrium2.txt

xxd -p ./Binary/sign_challenge_atrium2.bin | tr -d '\n' > ./Hexa/sign_challenge_atrium2.hex

cat ./Hexa/sign_challenge_atrium2.hex

[Retour de ces commandes]:

90c351145951d04c4d1f82f9a1ce3f50193be8ab4199b2f0be5591446f82955bd751e4005696277306d7c625a9e7ecf6ddab942e502547822ae067349512a9f12633fe9c97a1f0f7708173f0084eb2c1941389932e606070c4a43a5fb1d2d4425c76ebd1c51c684e57c996c5e29f60238ad3e42b2b24b0545eb3b2facd3e53735a185928f5e3b422c06185b00941fa32db32018c5e1a9f70daca099d4ba46d33720037498dfae9ce7de5d1ebac9f9d4155915cdb963ec2d4bf8c667842e5fbb54efe34b56e3d371790d8a2fa420c94353bfbfd018b676b322f03df859d9e6ec5ba321c5c2087d4ff47570730ea6ce6d5245c77a942efe2ff098b43c7ee840812

[C'est ce qu'il faut mettre dans le champ signature quand le challenge "riven tying motto droid inner" nous était donné]:

>>> carte
        challenge: riven tying motto droid inner

        signature:  90c351145951d04c4d1f82f9a1ce3f50193be8ab4199b2f0be5591446f82955bd751e4005696277306d7c625a9e7ecf6ddab942e502547822ae067349512a9f12633fe9c97a1f0f7708173f0084eb2c1941389932e606070c4a43a5fb1d2d4425c76ebd1c51c684e57c996c5e29f60238ad3e42b2b24b0545eb3b2facd3e53735a185928f5e3b422c06185b00941fa32db32018c5e1a9f70daca099d4ba46d33720037498dfae9ce7de5d1ebac9f9d4155915cdb963ec2d4bf8c667842e5fbb54efe34b56e3d371790d8a2fa420c94353bfbfd018b676b322f03df859d9e6ec5ba321c5c2087d4ff47570730ea6ce6d5245c77a942efe2ff098b43c7ee840812

[security engine] rsa.reduction:52:1|4ddb32dbdce721e235de3062ab0c652671c08fd6a26524eb8359b2c9472971a3           [DOUZIEME FLAG !!!]

### FLAG 13: Shared modulus Attack (RSA) (Double encryption)

[Aller dans le couloir jaune de l'Atrium.]
>>> conseil digicode
Le panneau en liège montre un message chiffré par les deux clefs publiques.
Ce serait sûrement utile de le déchiffrer. Mais cette fois, aucune clef
secrète n'est opportunément disponible.

[On cherche un Plaintext qui a été chiffré par ymolina et jillian47 à partir de leur clé publique respective.]
[Comme elles ont signé le même message, on peut le retrouver.]
[Lire le panonceau et le panneau]:
>>> lire panonceau
Salle RC-25 (équipe SÉCU) : ymolina et jillian47

>>> lire panneau
Il y a des affiches annonçant des colloques de sécurité informatique,
de petites annonces et quelques messages destinés aux utilisateurs des
locaux.  L'un d'entre eux dit notamment :

    MESSAGE IMPORTANT POUR LES UTILISATEURS DE LA SALLE RC-25
    ---------------------------------------------------------

    - ymolina: 73abb97126b99496e5146a51ef470c81a1ad2c72f6542c1081306c1bffc8a3fafdfbdec88eaaa9aa43d7a523d68d9e7b84ec317f46163e87ad263721c64b0f5cdeb7da2948a0de56a15200ea36a825b014c2723fe7f789be108294a1e3dd319b512dd284a21583336666eae21d5da7648c71e98dfc75dd3eefdbf790a7334cdbc741cc0d6a3128b23d6bb2981baff723cbb5f7d22816961cc13e4bec22ea22b018cedf8ae8ab3ba93a5a63f7c10ed3536e01b7e05405d3e35b9e5bb14deed8e65bc4919df7613324321dc2de11bd4663879c93f653d2f2db06bdbe512834a00bbae6aef0bff14790a4a56a955a2fcca1e5de36ec281012da04db89f82f2aa420
    - jillian47: 3ecf827250c63d9086bc1b008c4b3a306b5ae0380168537841f878f947022b61b8252f91309558577466c0d81fc93b6d755eb2a0128ddd74dadf0df86e8b548687fc8f889103a79400cc982214329eaf0d2182dc05380f84dd2033979cbd1e195c04137bc76cabc82b1fd25303a0d1eca9ae1a3ace40cab284692fb4b91af78e79a88b28fa834a27d7a8abab524be72429cd8a46bf5b4e46e86cc78d16fd12c5ef027bed9e2719dec9bdfd43ab7315792d726e82c50981833cfa9741abf8611982a2f31ea0bd1043b1f5514c2f42dde4c2e8a996a6d2450d19c5c9672d7abbda5cf2515038ce46450deb9bf01f0914ffb918c4f93bb6347de4517c4d4f8aa5d9

[Ce sont les 2 Ciphertext de ymolina et jillian47.]
[Il faut maintenant récupérer les clés publiques de ymolina et jillian47]:

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

[Il faut maintenant trouver le Plaintext associé en utilisant pour chacun de ces Ciphertext la clé publique de l'utilisateur avec la commande suivante]:

python3 shared_modulus.py

[Retour de la commande]:

n_bits = 2048

e1 = 828359798324333931577948685265643428373743765785527264890313655277318017
e2 = 113487104378672737569216731145184897498857894859115860585438651495477121

DIGICODE = c4b844a35ba8ecb20d40026a7c8903d0

[Donc ils partagent le même n.]
[Entrer ce code stocké dans le fichier ./Texts/digicode.txt dans le digicode du couloir jaune]:
>>> digicode
                0 1 2 3
                4 5 6 7
                8 9 A B
                C D E F

        CODE: :        c4b844a35ba8ecb20d40026a7c8903d0

[security engine] rsa.shared:52:1|6a2190aa0779831e8f3a87a922a01c3c05bc55fe94f22b99b6cf9c8b22d2a148      [TREIZIEME FLAG !!!]

### FLAG 14: Attaque par recherche exhaustive sur une seed trop petite

[A partir de ce moment, JE N'AI PLUS ACCES AU SITE INTERNET OU JE DEPOSE MES FLAGS !!]
                                                                   UGLIX v4.0 beta
                                                        (Security Engine Monitoring Console)
                    Active user: AdrienPanguel
                                                                      Main menu                    
                                                                      ---------
                    1. Monitor active threats
                    2. Exit
                                                            +--------------------------+
                                                            | new information acquired |
                                                            +--------------------------+

                                                                   UGLIX v4.0 beta                  
                                                        (Security Engine Monitoring Console)
                    subject: AdrienPanguel
                    nature: threat
                    level: medium
                    objective: monitor

                    First name    : Adrien
                    Last name     : Panguel
                    Email         : Adrien.Panguel@etu.sorbonne-universite.fr
                    Status        : student
                    Program       : MAIN4

                    Website access: ALLOWED 

                                                                   UGLIX v4.0 beta                  
                                                        (Security Engine Monitoring Console)
                    subject: AdrienPanguel
                    nature: threat
                    level: medium
                    objective: monitor

                    First name    : Adrien
                    Last name     : Panguel
                    Email         : Adrien.Panguel@etu.sorbonne-universite.fr
                    Status        : student
                    Program       : MAIN4

                    Website access: DENIED

Related security events
Entry in security log                                                                             subject           date
------------------------------------------------------------------------------------------------  ----------------  -------------------
pki.tutorial:52:1|8d3a204ece50cdea3d35d5c16bca71d7961841a01f1071dbafd6dc5a441da049                AdrienPanguel     2026-02-02 15:57:35
pki.upload:52:1|a75e2154fd95ebaefb63cb2d469d9d40062e3e32dce8c339b154f634d8f0eeb1                  AdrienPanguel     2026-02-02 16:05:25
power.on:52:1|10405faceec8e4e858c1de99d079861bebece22f18a1dfbeaf38819bc16a4891                    AdrienPanguel     2026-02-02 16:46:00
dict.atk:52:1|8afef7978c20be4f9e3061892df1b4cc4bb0b4ab9b9456110cfd18f1f907ebff                    AdrienPanguel     2026-11-11 16:57:17
rsa.keygen:52:1|2f5271e051f27f3fe91081d084796a47f4bb2af80b87e88f6197f7add482fe94                  AdrienPanguel     2026-12-12 13:26:35
chap.login:52:1|879e8a07b5658f7995eec82d86342dcf245d013441a1b4346d03e5171f7e894a                  AdrienPanguel     2026-12-12 13:59:01
pk.login:52:1|464830fac0d902b1e193a8045a68fef6bdd8222a7e32cf7163a2912ed63eb867                    AdrienPanguel     2026-12-12 14:36:55
pki.cert:52:1|8fe700cd09c6930261a71d3f75981625b83f3bcd5391b161e280bbbfd4078350                    AdrienPanguel     2026-12-12 15:22:57
hybrid:52:1|ba7c7348d96337ca34e197eea20f768c094e604ceb34844d6e9759d3bf0de937                      AdrienPanguel     2026-16-16 17:05:44
register:52:1|b644c1e209b41a83e9ed72be2f7878f8eb9c34fde9a06f0e9701f5448840e16a                    AdrienPanguel     2026-18-18 10:04:08
web.of.trust:52:1|f314e4db3ff276736a12d4109325c66c5aab06318dce9fb8eea4ddfa36b2adb5                AdrienPanguel     2026-23-23 15:52:26
rsa.reduction:52:1|4ddb32dbdce721e235de3062ab0c652671c08fd6a26524eb8359b2c9472971a3               AdrienPanguel     2026-23-23 17:34:34
rsa.shared:52:1|6a2190aa0779831e8f3a87a922a01c3c05bc55fe94f22b99b6cf9c8b22d2a148                  AdrienPanguel     2026-24-24 20:04:17

[Mes flags sont maintenant enregistrés dans ce terminal.]
[Aller à la bibliothèque et lire les livres "spécification des enclaves sécurisées Uglix Secure Vault (tm)" et "tome VII : chiffrement avec clef et IV explicites" à la bibliothèque.]
[Retour au labo salle RC-19]:
>>> conseil terminal
Si on résume la spec, on trouve que : 
1. une graîne de 16 bits est générée, puis
2. une clef de 128 bits (secrète) et un IV de 128 bits (connu) en sont déduits.
Une attaque par "force brute" (en fait, recherche exhaustive) est donc possible.

>>> conseil terminal
La stratégie consiste à essayer toutes les graînes possibles, calculer la clef,
calculer l'IV, vérifier si l'IV est le bon (le cas échéant la clef est bonne 
aussi), puis déchiffrer et profiter.

>>> conseil terminal
On peut déchiffrer avec OpenSSL en connaissant la clef et l'IV en allant lire
le bon mode d'emploi à la bibliothèque. 

>>> conseil terminal
Il n'y a que 65536 grâines possibles, donc ça prendra un temps infime.

>>> conseil terminal
16 bits, ça fait 2 "bytes", donc en python ça s'écrit ``bytes([a, b])'' avec
0 <= a < 256 et 0 <= b < 256.

>>> conseil terminal
C'est tout !

[Aller au labo dans la salle RC-19 et ouvrir le terminal]:
>>> terminal

                                                                   UGLIX v4.0 beta
                                                              (LPNHE Research Terminal)
                    Active user: AdrienPanguel

ы└ы┬ь╠ы┼ы┘ ь╔ы┼ь╗ьЁы┬ы┘ь╖ы└ы┘ь╥ь╖ь╗ь╧ы┤ы┬ ь╗ь╗ьЁь╖ь╥ь╘ ы├ь╣ ь╢ы┐ы└ы┼ (ь╗ы┘ь╧ы├ы┴
ьёы├ ь╖ы└ь╨ь╖ы┼ь╘ ы┤ы┼ ь╖ы└ь╢ы┐ы└ ы┬ы└ы┼ьЁ ь╖ы└ы┘ь╜ь╙ы┬ы┴) ы┬ы┼ы▐ьЁь╙ь╝ь╞ы┘ ы│ы┼
ь╣ы├ь╖ь╧ь╖ь╙ ь╖ы└ы┘ь╥ь╖ь╗ь╧ ы┬ь╞ы┬ь╠ ь╖ы└ы├ь╢ь╠. ы┐ь╖ы├ ы└ы┬ь╠ы┼ы┘ ь╔ы┼ь╗ьЁы┬ы┘ 
ы┬ы└ь╖ы┼ь╡ь╖ы└ ь╖ь╖ы▀ ьы└ы┘ь╧ыы└ы└ы├ь╣ ь╖ы└ь╢ы┐ы└ы┼ ы┘ы├ь╟ ь╖ы└ы┌ь╠ы├ ь╖ы└ь╝ь╖ы┘
ьЁ ь╧ь╢ь╠ ь╧ы├ь╞ы┘ь╖ ы┌ь╖ы┘ь╙ ы┘ь╥ь╗ь╧ь╘ ы┘ь╛ы┤ы┬ы└ь╘ ь╗ь╠ь╣ ы┘ь╛ы┘ы┬ь╧ь╘ ы┘ы├ ь
╖ы└ьёь╜ь╠ы│ ь╗ь╢ы┐ы└ ь╧ь╢ы┬ь╖ь╕ы┼ ьёь╝ь╟ь╙ы┤ь╖ ы┘ы├ ы├ь╣ь▄ ы└ь╙ы┐ы┬ы▒ы├ ы┐ь╙ы┼ы▒
ь╗ ь╗ы┘ь╚ь╖ь╗ь╘ ь╞ы└ы┼ы└ ьёы┬ ы┘ь╠ь╛ь╧ ь╢ы┐ы└ы┼ ы└ы┤ь╟ы┤ ь╖ы└ьёь╜ь╠ы│. ь╝ы┘ьЁь╘ 
ы┌ь╠ы┬ы├ ы┘ы├ ь╖ы└ь╡ы┘ы├ ы└ы┘ ь╙ы┌ь╤ы┼ ь╧ы└ы┴ ы┤ь╟ь╖ ь╖ы└ы├ь╣ь▄ ь╗ы└ ь╖ы├ы┤ ь╜ь╙
ы┴ ь╣ь╖ь╠ ы┘ьЁь╙ь╝ь╞ы┘ь╖ы▀ ы┬ь╗ь╢ы┐ы└ы┤ ь╖ы└ьёь╣ы└ы┼ ы│ы┼ ь╖ы└ь╥ь╗ь╖ь╧ь╘ ы┬ь╖ы└ь
╙ы├ь╤ы┼ь╞ ь╖ы└ь╔ы└ы┐ь╙ь╠ы┬ы├ы┼. ь╖ы├ь╙ь╢ь╠ ь╗ь╢ы┐ы└ ы┐ь╗ы┼ь╠ ы│ы┼ ьЁь╙ы┼ы├ы┼ы▒ь╖
ь╙ ы┤ь╟ь╖ ь╖ы└ы┌ь╠ы├ ы┘ь╧ ь╔ь╣ь╞ь╖ь╠ ь╠ы┌ь╖ь╕ы┌ "ы└ы┼ь╙ь╠ь╖ьЁы┼ь╙"ь╖ы└ы┘ь╥ь╖ь╗ь╖
ы└ь╗ы└ь╖ьЁь╙ы┼ы┐ы┼ь╘ ь╙ь╜ы┬ы┼ ы┘ы┌ь╖ь╥ь╧ ы┘ы├ ы┤ь╟ь╖ ь╖ы└ы├ь╣ь▄ ы┬ь╧ь╖ь╞ ы└ы┼ы├ь
╙ь╢ь╠ ы┘ь╠ь╘ ьёь╝ь╠ы┴ ы┘ь╓ь╝ь╠ь╖ы▌ ы┘ь╧ ь╦ы┤ы┬ь╠ ь╗ь╠ь╖ы┘ь╛ ь╖ы└ы├ь╢ь╠ ь╖ы└ь╔ы└ы
┐ь╙ь╠ыь╚ы┬ы├ы┼ ь╚ы└ "ьёы└ы┘ь╞ы┬ьЁ ь╗ь╖ы┼ь╛ ь╖ы┼┼ь╖ь╠ ы┐ь╠"ы┬ы▒ы├ы┬ь╖ы└ь╧ь╖ь╞ь╙ы┼
ь╜ы┬ь╙ ьёы┼ь╤ь╖ы▀ ь╧ы└ы┴ ы├ь╖ы▌ Ёь╝ ы┘ы├ ы├ь╣ ы└ы┬ь╠ы┼ы┘ ь╔ы┼ь╗ьЁы┬ы┘

*** Process received signal ***
[UGLIX:04968] Signal: Segmentation fault (11)
[UGLIX:04968] Signal code: Address not mapped (1)
[UGLIX:04968] Failing at address: 0xb)

Dumping core... 
[Uglix Secure Vault Enclave]

IV = 96c2089c5c89644420794597e1eba19b

SOP2nk7iNuuglfxxcrdBuBnPFyINykfDAsX+IvzY5YMmjHNgBwOG5O31Ljdv7fCZ
o730ICMWhWs2hA97pvmDq9nK4ZRgZfdtZjJxARw4e96MgM6BvRKZOBySE1NlRCly
4NbJRfc49wAyY7/Zo+JS6E01NPmdlZgtW/SAt2U1CDAu1Liv/QviWa64C8YL31kr
lgIIKoDlORbcnCP7gIDuFEbSn06bxQGrAotlG+i6fa7jyMq0XCoTRajefjFBqMad
qRqeDW1MDq5YkHMcnWwGcH48PFqHDSWtIus3lNkEx+kFGszm8ORdMts2j2XFrRlV
s3r4jL74ivb0FxjvUf1BX3WZVmzOiCWlL0yLGlplE62/M2CEd7PZyQpYLZtx86/S
QJV7K75apvw2+VW7vuf2HNosX2ZkOKLrQdQa35LlHuMifwRE7kvWIjzifqnNpxiA
f9bpEiVAl8rpLvfqXE/fdi8TAhxD+TL47yYbeZ3rbEqp4rlmoMEn2+06GQqDkw3r
gmz43CiZ0zrq8XUFAz3/pbjHPW2TUntcMnTdSYIkRStYZ7VGR2Q7slzx9TSQUum7
+JGAmkbfGA1Yb3TB0TygP2tGOlnR+VjoTUlq4TTUTW4PL3d8u3AkEgeF0hyXoqu4
Rfz9DTVxGqFHF9KKj7Q5rLvxXq5pz9oQWLwvlfLmvAnVx0w36R/ufwtYlbhm5UC6
QlMTXVt8VOWg+V0osA2W8GXNzymTvnwKYrecUpxselDVc2gEad4j68a6UiIEoQ5M
tgrOR/zyPYPPeogko0naqCNPzqpUTHG9dKywPj8ht955QAJKKwbdK6t5IDw7lm/e
CrbB6dXZivJaDTOXbHN3bVSnW2gxxElZ1s4stHB+LsTerIuMEBF6tpAD8bkpZm0o
4s1RbFl8qeCUbt909wV4QOAvt24SXGkfIPJzets+edlXrl+4SoFmXvBqz2X5ng2N
MonbqS1A0Aul+gmn1GEYRTalQ5m3L4nyiRY/2A2NZ/tmMOI8i5Y0mBJAtNHie2QN
5E/CviIWDuE/T1mQXYdmxIAgCuWzj8fiKCzrL2LQhXh6S9Owxb2/d6Kw1YIYpsTd
XIh1B3R7jjJ6eoucxRwTG9Y3YtK9E9kUZtIbC/ZUZbX8skTYqPOj7N0mnevgLv3K
knFo3HreD6YjHA0TuMvkRq3RU3haziVB5uVOpUH6CdPWu2lfF+8c309tbQpVkSlq
5ct37JjMjy9xcILLbevgW9OeQPPN+tqqeBo3WrmgR9B+OCTyw8LLiMrzdOmgDBw4
9b6qQi6MjUHWVjRzPgkgnrzh56D5x1SotvK/ZwYbxEnZe4c53xbgfJID+41yubEC
Z0GTOCftMoAAUf7/cPdM9mQG5N65XMQN3NDf2ZDqqUW0kQ2lgsrnvVioojxxl3zT
OZAFeIfP6seTMUnnvihuPiU/sBlHp+amGuxK63wBBSDLEUO8Cz1NdSkg8wg2+lGL
/pcxXmlBnEVuwmAKGet9BnKIT+WDvjMJs7GXbhyXZOfTsA4YXLS00ULT8FshpP1G
zUHe356HtuLcHTEZZaOUgsj4jcKVYEQNM/CEnN3qeVGc+qwHpwL8MMJs5VMdA9xJ
F/h2I3JvQeG4n8B6mn9kwvWZCZAsK+SQdWenzcLi9rZzx8wvCARpv5/XGq7LwVBi
xn7f1OVyAoX2kZ3Fhd36mI0rtSciDp14WeJb3yJaiGp98UP4vifKaOZJCj+1tynG
H/yT9WBLhWCfpQ2JcFuEq2U293FE6FQSY7gKUblgfMVjvyOyH58GlQQXCw3peoUM
Gny2Ab8uYRP7Ku8e2HdSWEAkHGtg7nebvn3Q1nXcTjYyUYG6LtggL+q0OqbMl9HJ
Pwemnvmkl44/8JDc8yIjTwqrxKTRJku7jpsfv7wfVFWRfNZKKoQQhtnyaMoUCxru
VNlLrne+ZLQ/dcyxiD9C2kdnQrTdrT2rI7a4dIdHY7JB2KiYgvdZQ9TZn7N0me8D
cu8tVdHknx6OFE/1mb/b8d12NTccuPhCrom8i6lF0ZwtAyNpd2I41ecD2s1e4yix

[Noter le "IV" quelquepart et le long bloc64.]
[Lancer le code key_expansion_seed.py pour identifier la bonne seed avec la commande]:

python3 key_expansion_seed.py 

[Retour de la commande + stocké dans ./Texts/key_expansion_seed.txt]:

[+] Seed trouvée: 56607 (0xdd1f)
[+] K  = 662d96351653d4242ed0ab569e78d9d1
[+] IV = 96c2089c5c89644420794597e1eba19b
[+] Plaintext plausible (UTF-8) :

Cahier de manipulation
09:00 Démarrage de l'accélérateur
09:27 Puissance nominale
09:45 Première tentative de broadcast à cette puissance
      Envoi de "Hello world!"
09:57 Réception depuis les coordonnées 9be4862c2ba03242774ab6ecd69a0d95 
     de la chaine "Qui est là ? Il y a quelqu'un ?".
10:23 Echange de plusieurs autres messages.  Apparemment notre interlocuteur 
      est un être humain situé aux coordonnées 9be4862c2ba03242774ab6ecd69a0d95.
10:45 Légère surtension dans la bobine #3.  Arrêt et inspection des dégats.
14:12 Redémarrage de l'accélérateur
14:58 Puissance maximale.  Tous les systèmes OK.
15:03 Démarrage de la tentative de téléportation d'une brique de légo 
      vers les coordonnées 9be4862c2ba03242774ab6ecd69a0d95.
15:07 Explosion majeure dans la salle d'expérience.  stanley42 évacué par 
      le SAMU (brulures superficielles)
15:09 La brique de légo a disparu (vaporisée par l'explosion ?)
16:20 Réunion d'urgence du conseil de labo.  Point sur les procédures de 
      sécurité.  Les nouvelles expériences doivent être validées par le conseil.
17:39 L'équipe de nettoyage constate la présence d'un objet non-identifié dans
      la salle d'expérience.
18:20 Réunion de débriefing de l'équipe expérimentale.  Personne ne reconnaît 
      avoir déposé l'objet en question pour faire un canular.
18:30 Nouveau mot de passe pour la salle d'expériences : 3f478ea5e21e3b82c68d2fc33ce50587
18:45 Fin de la journée

[Noter ce mot de passe "3f478ea5e21e3b82c68d2fc33ce50587" et l'entrer comme Code dans le digicode dans le sas sécurisé]:
>>> sas
                0 1 2 3
                4 5 6 7
                8 9 A B
                C D E F

        CODE: :         3f478ea5e21e3b82c68d2fc33ce50587 

[security engine] secure.vault:52:1|b0839215cb365aed8c7c033ef9e056202b3d847a5cbbd9db7ac9c8f0ad851aff    [QUATORZIEME FLAG !!!]

### FLAG 15: Théorème des restes chinois (Small public exponent)

[Aller à la bibliothèque et regarder le distributeur]:
>>> conseil distributeur
Il y a une commande ADMIN, qui demande un mot de passe.  Vous avez ce mot
de passe, mais chiffré par trois clef publiques différentes.  Commencez
par récupérer puis examiner les trois clefs publiques.  Qu'on-t-elle de
spécial ?

[Lire le livre "Manuel_d_utilisation_des_distributeurs_automatiques".]
>>> lire manuel
Cet épais manuel (environ 570 pages) décrit de manière détaillée toutes les
procédures de remplissage, nettoyage, paramétrage du paiement, etc. pour les
distributeurs automatiques de friandises qu'on trouve partout sur le campus.
Version courte : pour accéder au menu de réglage, il suffit de taper "ADMIN"
puis d'entrer le mot de passe.  À toutes fin utiles, voici le mot de passe
(chiffré avec les clefs publiques des trois développeurs) :

    - davidrodriguez: 09dcdd93b468ca6617dcdbfb2d167673cff9c0be2042046c22e790cf1bbb3720868784d624592698080a0d7ff00c49b6377b8dbf48a9c2d6a71c8939086e8d4963480e031c0cfc164dfbe746bf265d86fcc1a2e3fe1eef0370d2e5f270a0741fba6ab98dd5a7023708672831e50f68398210807688478ca897855432d090bae43c146848af5c58f1c6e331f2f39f791bdc0c80deb175104b1826e6216b7f4b5362badf620ced2d8450a99a7a978924db24942a5168c786203d83b9128c716b5a2b98ef4c754688aacbd4cf621fcdf54e2521a40c74264201d198176e15ddcc15ce7956bf504205ed753b16f948020873c8a60d4d7be5a6ab9ea765c8441dbdc1
    - jbowen: 99a2bb1d4e1cad08900b41225471058ddbab94aec8bbd93d6870c185027f3b305e9e66cb25f6e51f73e525c3d43163115336bed8a1fa94db98643125959dc1850c81a60fdf6284c8ff4b89bbf0a3b9ad896142727165138f206875c90be9405b7d5b6a5c4df9b41d21221d060ee070eaf770c4c9f11240bdfd320f621fb43bad8a87df3cbcdbc6887de2adc43bf4dab77f6f745134e33cf62e7ecd0102b073956ed9a4b88bce3583e29976c97437f8449d1b693b2857ddde8ee77f2ca382164779a38fac889202c9d2b87fbb279ca95a435f0ef42d8c18d494e33b9afa16799f130d31d929124cde4d5384b4b227f147546483b3ae9cef044b51f331ed89b20e
    - samuel83: 2c59b0e207b3c8c223eb2753dd9cc7936d2c84d8dd472944dc46d35c96532fd5877bb4efa0060669d0a15d8ef1bb2dd823de007f26c45e6595c7048e85cef1c246bb593f8c4dfd286113f48b58a4592a6959ecef6dbf3581df3e8f9b677ba3ab3ea113f10f1cddd6ce44809e3b05e667a1b2b01f4a5389a018f9936433e04ea37bee6d16d079cd3d1bd01cfc07d65f5a2e3bd58faa1e78b380abea54196fbdf36d3b5f9f19ad4991022032d72f126e6391bd2411dc5366c0de9acb646bdcef1d2f63e72bd5953d77a3f5727907e63b51040ad9c32ee63cd029c8af9556c54a928c9e2448e365918d9ba39fa3e616b1ff4de25baa82a34ff6aff36a69fedb63de

[Enregistrer ces Ciphertext dans 3 fichiers ./Texts/ciphertext_distributeur1.txt, ./Texts/ciphertext_distributeur2.txt, et ./Texts/ciphertext_distributeur3.txt]
[Récupérer les clés publiques de ces 3 personnes dans le terminal.]

[Extraire le "e" et le "n" de chacune de leur clé publique avec la commande suivante]:

openssl rsa -pubin -in ./Keys/PublicKeys/pk_distributeur1.pem -noout -modulus | sed 's/Modulus=//' | tr '[:upper:]' '[:lower:]'

[Retour de la commande]:

bee9bd6750beb5a56d88685d199e193e3ec8e38e6af70021a47e091dbb5c41f7d832ca99708ef1a99813fbd3986c5666ddb63ef11631272a4851df3f99e701fc7e1de1a85c5b5c187850cae49144bde455a9100cad8bd137b5e0459cbd2a3b75b06cd243d8862dfca0098bbe411b1a63e74f913636027efb9138d4f011f597a5d3e2383a7a4bfb00df37941fe403e495c8084d37bc3155e7d9c007f07721e28f5cb557a1d2da8b80f5153f11f7e2d01f9d6cc9cd7126011972d3d714e3593161b196ccbbada38f5bbe9964b7080695951e941dc6712687c8a0c2982be3388d3f4696021948bd30c8bf4dfe87233d30b3379a2791a2198089292faf35f48e8c35

[Idem pour les 2 autres]:

openssl rsa -pubin -in ./Keys/PublicKeys/pk_distributeur2.pem -noout -modulus | sed 's/Modulus=//' | tr '[:upper:]' '[:lower:]'

aff0cca51213ed42b68971b60d53588b131f921679017d9060591d17cb1a75fffb527b22f71b08a1f973e845781535ce6d3bc35b4225dfb607d4326f53092d44cb478a0521cb610d6e390a54156b4898ddd30452bb46f3cc718e4eb40085aab82d8940eb4fd9e4a3d005ca437214cf86c8b8b6221a079692b82ff7bfbc3f14b1dffac2b18bfa5decb89630b5416c1c1c0ad109908ba678cd1248f827e3140992f20df5642006df47a7f659e1cd42c73cb93607bb03eff97ff306662199befcdd559ee96c3a6fedad1e91bc36ccf5239e2a498f6180d49d4e478d002c52beae5356485e18666858174de2fb3794ecf5e0ce58af3dbeb480c156c1aae8056fbe27

[Et]:

openssl rsa -pubin -in ./Keys/PublicKeys/pk_distributeur3.pem -noout -modulus | sed 's/Modulus=//' | tr '[:upper:]' '[:lower:]'

b8b7f7dbd82d6a733a8faed66d8dd6c3098f4b78270fa37d28121791a3d7e871c80cd60ec9688ffa02ca8d544dd84bf8526eb24971d1eab0c8d2485e8cecb0916596b7c268a54632e589ef244f50a08d68a7d66eb3288899007469a57c60ed3529eafae7ceea65e26f3586e72a902052a48f737ee36acc0df3b4d0582a33e6de996f520b49d5a1ca468fea773f6c86b35b3a0c8f765325a78a17022352b7e30aef593021093d687d01c9ae24fce18b1dc3786a7bd4fe88dfc1767a3e1ef220bb7af47e91cfc1db73bf2ad7a58eff1c1f0c4d38733a781d9d138969bcc3d394b9893fd2eb0084d4dd11c474821e7bc7be4f2629d98dc92f2a379ce9cf08a5ba11

[Lancer le code decrypt_ciphertext_distributeur.py avec la commande suivante]:

python3 decrypt_ciphertext_distributeur.py

[Retour du code]:

[*] Exécution du Théorème des Restes Chinois...
[*] Calcul de la racine cubique...
[*] Valeur brute de m (hex): 0x298bbf59056e63122c96e729b13807e06bdab680f449926ef429bbf861373f03de877f4a29993716e33e96c99a6057b1b5043310c64dbcd0744c24484509f5a7b99f46ff963747585d9ef483aa2d6fe60e4f6708580b08ba6977fb61238eb8a3e4fd271ac17ba741bf633f8b405f2d22131b894f182d6d30d8a30575a2f3bd915c3fbaeb9eb857411be31c12ea70953f36f9b77eb4b76f5786be6386bb2b19b95a2445e0845f3d343d993442021df1d406ded10dd182780a3824c83d96498375c0ca5ab7cee36f4a5bd2213666cec006d6f74206465207061737365203a206264333466313963363431346134646430366132376465353438386633356432

[+] Résultat trouvé :
mot de passe : bd34f19c6414a4dd06a27de5488f35d2

[Ce mot de passe est à entrer dans le distributeur avec comme "CHOOSE YOUR PRODUCT": "ADMIN"]
                    PRODUCTS:
                    =========

                     1 : Chips
                     2 : Snickers
                     3 : Twix
                     4 : Oreo
                     5 : KitKat
                     6 : M&Ms
                     7 : Crunch
                     8 : Biscuits diétiétiques Gerblés
                     9 : Madeleines
                    10 : Barre de chocolat noir
                    11 : Paquet de post-it
                    12 : Boules Quiès XXL
                    13 : Boules Quiès XXS
                    14 : stylo bille ``top budget'' (promo)
                    15 : Walkman (new)
                    16 : Écouteurs bluetooth
                    17 : cable USB

CHOOSE YOUR PRODUCT:
#$$$ ADMIN
                    password:                   bd34f19c6414a4dd06a27de5488f35d2

                                                   +----------------+
                                                   | ACCESS GRANTED |
                                                   +----------------+
+------------------------------------------------------------------------------+
|  Cher opérateur,                                                             |
|                                                                              |
|  Malgré tous nos efforts, nous n'avons pas réussi à terminer à temps ce      |
|  module d'administration.  Nous vous présentons nos plus plates excuses.     |
|  Pour vous dédommager, nous vous prions d'accepter, en guise de cadeau,      |
|  un produit sélectionné aléatoirement.                                       |
|                                                                              |
|  Très cordialement,                                                          |
|  ----                                                                        |
|  Les développeurs de VendingMaster Inc.                                      |
|  (bientôt en burn-out)                                                       |
+------------------------------------------------------------------------------+

[security engine] rsa.crt:52:1|4296c6ee787bac7de665521d490c63dc61ae9c81de6688266a0577c72448a498         [QUINZIEME FLAG !!!]

### FLAG 16: RSA blinding

[Aller à l'auditorium au CICSU]:
>>> conseil laptop
Pour commencer, pour obtenir une signature correcte (c.a.d. qui vérifie avec
la clef publique en utilisant OpenSSL), il faut appliquer soi-même l'encodage
PKCS#1 v1.5.  Ensuite, la programme va effectuer la dernière étape
(l'élévation à la puissance d modulo N, où d est la clef secrète). La spec
de la signature RSA PKCS#1 v1.5 se trouve à la bibliothèque.

>>> conseil laptop
Une bonne manière d'appréhender le problème, c'est de commencer par faire
signer n'importe quoi puis de vérifier que les signatures sont valides.

>>> conseil laptop
Conseil général pour la mise au point : essayer d'abord avec une paire de
clef qu'on a fabriquée soi-même et pour laquelle on connaît tout plutôt que
d'utiliser le serveur comme une boite noire qui dit ``NON''.

>>> conseil laptop
Ensuite, pour faire signer ce qui nous intéresse, on peut exploiter la
***malléabilité*** de RSA.

>>> conseil laptop
Concrètement :
- on soumet (M * x**e) mod N, pour un x aléatoire.  Ceci "masque" M au serveur.
- le serveur renvoie (M * x**e)**d == (M**d) * (x**ed) == x * M**d mod N.
- il suffit d'éliminer le ``masque'' x (en multipliant par l'inverse de x
  modulo N) et on obtient M**d mod N, c'est-à-dire la signature voulue.

[Récupérer la clé publique du directeur dans le laptop]:
                                                           UGLIX v4.0 beta
                                                        (Lab Director Proxy)

                    Active user: AdrienPanguel

                    DIRECTOR's PUBLIC-KEY:
                    -----BEGIN PUBLIC KEY-----
                    MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvtbNyPFC1hhUtr3cb56z
                    a7v05dq3cgckAHgpPDhOtT1OOgsvJQ1t0RkkSJc7JQ1WNRchjJChLARH9bMd83QQ
                    2KLiFXPA8FqKqZJBFHCAU7CIeNO1PM01ujUWwCw2ktBIrUbpi3++E6mbRnD8yW3V
                    HnoEo9qTSTq1tbD/eud3CNdPjJZBElI/7VnBvclJv+okj/CjkoUwKwKSprjeI/mK
                    kgE1zxtWYOFutP3bsktDEu9cWfSgKmff8rKKbRsMPjlCwXNvqkOpTwmV4EvabIc6
                    HLr2aFQkGWq8YYXT5A/BzCdvrnLeBGXZdI5ut+FltigApT8sZ+RpPMkrN6nuS8RJ
                    6QIDAQAB
                    -----END PUBLIC KEY-----

                                                                Menu
                                                                ----
                    1. Lab Director Assistance Program
                    2. Exit

[Mettre cette clé publique dans ./Keys/PublicKeys/pk_director.pem.]
[Récupérer le N de cette clé publique RSA dans le terminal avec la commande suivante]:

openssl rsa -pubin -in ./Keys/PublicKeys/pk_director.pem -noout -modulus | sed 's/Modulus=//' | tr '[:upper:]' '[:lower:]'

[Retour de la commande]:

bed6cdc8f142d61854b6bddc6f9eb36bbbf4e5dab77207240078293c384eb53d4e3a0b2f250d6dd1192448973b250d563517218c90a12c0447f5b31df37410d8a2e21573c0f05a8aa9924114708053b08878d3b53ccd35ba3516c02c3692d048ad46e98b7fbe13a99b4670fcc96dd51e7a04a3da93493ab5b5b0ff7ae77708d74f8c964112523fed59c1bdc949bfea248ff0a39285302b0292a6b8de23f98a920135cf1b5660e16eb4fddbb24b4312ef5c59f4a02a67dff2b28a6d1b0c3e3942c1736faa43a94f0995e04bda6c873a1cbaf6685424196abc6185d3e40fc1cc276fae72de0465d9748e6eb7e165b62800a53f2c67e4693cc92b37a9ee4bc449e9

[C'est le N de la clé publique du directeur à déposer dans ./Hexa/n_director.hex.]
[Lancer le code blinding_plaintext.py avec ce N.]:

python3 blinding_plaintext.py

[Retour de la commande + stocké dans ./Texts/blinding_plaintext.txt]:

--- DATA À ENVOYER AU DIRECTEUR ---

b8172d5e5eae552d7aeb205a8dafb2dba370d55aad8322ba28c0529e821a1d75267e85917d22551116373fb48eb903b2e637ace79241e744e4340b10b830a506ea9ee8b6d14a20a9c9988542af3fd55559018774ebf7719b5f7be4ca867628442dacc6454a475dac1923895712e54c1c8ccd2dfaa15ff76c66355733c1bffeb47949cd7bad503e522b45dfd47633ff6811efd12f6270a9ec8607012019b48c1c60e90b925561dd31872677b26b271803c2ed1eda660d3d2f4bd5672f5efb30fbf05f741a370c50f85c16a30336dca26af82b63359ba84fe2ca9c846645c50aa5df7dbc6c6d9e09fc9bb0c758d740755a815a8768258fce76e6998e844f8960bf

[Ouvrir le laptop et demander à faire signer ce blinding message.]
>>> utiliser laptop
                                                           UGLIX v4.0 beta
                                                        (Lab Director Proxy)
                    Active user: AdrienPanguel

WARNING: - This prototype is INCOMPLETE.
WARNING: - It does not fully implement RSA PKCS#1 v1.5.
WARNING: - Here is what it actually does:
WARNING:   - read the input as a hex-encoded number (big-endian)
WARNING:   - run the IA decision algorithm on the input
WARNING:   - raise it power d modulo N (d is the secret key)
WARNING:   - print the result in hex (big-endian)
WARNING: - This does not produce valid OpenSSL signatures
WARNING:   out of the box because the padding is not applied

YOU HAVE BEEN WARNED

                    Data:                       b8172d5e5eae552d7aeb205a8dafb2dba370d55aad8322ba28c0529e821a1d75267e85917d22551116373fb48eb903b2e637ace79241e744e4340b10b830a506ea9ee8b6d14a20a9c9988542af3fd55559018774ebf7719b5f7be4ca867628442dacc6454a475dac1923895712e54c1c8ccd2dfaa15ff76c66355733c1bffeb47949cd7bad503e522b45dfd47633ff6811efd12f6270a9ec8607012019b48c1c60e90b925561dd31872677b26b271803c2ed1eda660d3d2f4bd5672f5efb30fbf05f741a370c50f85c16a30336dca26af82b63359ba84fe2ca9c846645c50aa5df7dbc6c6d9e09fc9bb0c758d740755a815a8768258fce76e6998e844f8960bf

                    Checking data ...

                    No problem detected

                    Signature:
                    8b6821c407716ad36b6fec58af03b25a3e3d410614a920ba19d8a0c193479e4f4647bb725157afb463c3307d05a09b307db7ce75f80d00b79b4bae2b18f6623aea8c0f827840f8d7ff52a7663fc12e25afbf10761bd5c7b0064416a2609bda951741e432a4fea8ceed0d980941abdbd7e38baecb3cc2fdd3caf77c7c3386c6bd3b633dabb3ef035b928cdb5102f605cf48256475bbee6ab98cb46538eeefc3465ece9176222c4c430fbaba81c688c7e44735ae43039ca41f10848696fc8a212e850a1309e860369a314fc1c33939a9a6ac183576a375fc6df0ced4cfcbfa060c58a79e04f44505c650a9da57c46435b4b8275632b8086f17c30e960af20da490
[press any key]

[Noter cette signature dans ./Texts/sign_blinding_plaintext.txt.]
[Retourner au Robot gardien et donner cette signature.]
>>> Robot gardien
Vous vous approchez prudemment du robot gardien, et à votre grande surprise
celui-ci entame poliment la conversation.  Vous lui expliquez que vous auriez
vraiment besoin d'emprunter le BiblioDrone-NG.  Il répond : bien sûr, c'est tout
naturel, seulement vous savez, le règlement...  Bref, il a faudrait que vous lui
fournissiez une signature (réalisée par le directeur du labo) de la chaîne de
caractères :

        "I, the lab director, hereby grant AdrienPanguel permission to take the BiblioDrone-NG."

Ensuite, bien sûr, vous pourrez l'emprunter.

                    Signature:                  45b410e203b8b569b5b7f62c5781d92d1f1ea0830a54905d0cec5060c9a3cf27a323ddb928abd7da31e1983e82d04d983edbe73afc06805bcda5d7158c7b311d754607c13c207c6bffa953b31fe09712d7df883b0deae3d803220b51304ded4a8ba0f219527f54677686cc04a0d5edebf1c5d7659e617ee9e57bbe3e19c3635e9db19ed5d9f781adc9466da8817b02e7a412b23addf7355cc65a329c7777e1a32f6748bb1116262187dd5d40e34463f2239ad72181ce520f8842434b7e45109742850984f4301b4d18a7e0e19c9cd4d3560c1abb51bafe36f8676a67e5fd03062c53cf027a2282e32854ed2be2321ada5c13ab195c04378be1874b057906d248

                                                          +--------------+
                                                          | Acknowledged |
                                                          +--------------+

[security engine] rsa.malleable:52:1|420d66ffc695a390bcc41c89dd521f355bf8a1ce8bc62b0180671b53d2e891a8           [SEIXIEME FLAG !!!]

### FLAG 17: Interpolation polynomiale

[Lire les livres "spécification_du_journal_des_évènements_de_sécurité_partie_I" et "spécification_du_journal_des_évènements_de_sécurité_partie_II"]

[Pour l'inteprolation polynomiale, on cherche à retrouver les coefficients d'un polynôme P(X) de degré 8 qui a donc 9 coefficients.]
[On trouve ces coefficients avec les 9 premières clés qui sont comme des "points" dont on cherche l'image par le polynôme P.]
[Lancer le code interpolation.py avec la commande suivante]:

python3 interpolation.py 

[Retour de la commande]:

Points uniques : 9
R(0) = 3227412088583349083
hex(R(0)) = 0x2cca1231ebcfe35b
Il manque 8 point(s) pour S(0)
Il manque 16 point(s) pour T(0)

[On retire le "0x" dans l'hexadécimal "0x2cca1231ebcfe35b" pour n'avoir que "2cca1231ebcfe35b".]
[Aller au CICSU dans le foyer, sur la borne et entrer cette firmware-key.]

                                                     UGLIX v4.0 beta
                                                (Firmware Update Station)
                    Active user: AdrienPanguel

                    Firmware update key:        2cca1231ebcfe35b                    
                                                 +------------------------------------------------------+
                                                 | Firmware updated. New command activated: ``#!sudo''. |
                                                 +------------------------------------------------------+

[DIX-SEPTIEME FLAG !!! (Directement dans le terminal du RC-25 de l'Atrium).]

[Désormais, on peut taper "#!sudo#, un terminal ">>>" s'ouvre, et on peut aller dans n'importe quelle tour (tour 26 contient tout) avec un ascenseur et taper]:

>>> #!sudo

[SUDO]>>> ascenseur
          Level (SS / SB / JU / 2 / 4):

[Mtnt que nous avons 7 flags, récupérons la 3ème firmware key en lançant le code inteprolation2.py]:

python3 firmwares.py 

[Retour de la commande]:

Points uniques : 17
R(0) = 3227412088583349083
hex(R(0)) = 0x2cca1231ebcfe35b
S(0) = 5120953362034886927
hex(S(0)) = 0x471147f3676e890f
Il manque 8 point(s) pour T(0)

                                                                                     UGLIX v4.0 beta
                                                                                (Firmware Update Station)

                    Active user: AdrienPanguel

                    Firmware update key:        471147f3676e890f

                                                      +-----------------------------------------------------------+
                                                      | Firmware updated. New command activated: ``#!bluetooth''. |
                                                      +-----------------------------------------------------------+

[ On a aussi la commande "#!bluetooth".]

### FLAG 18: 

[On monte au niveau JU dont voici le plan]:

 12 --------- 22 --------- 32 --------- 42
 |            |            |            |
 |            +---- SHSE   |    tipi    |
 |            |            |            |
 13 --------- 23 --------- 33 --------- 43           53
 |            |            |            |            |
 |            +---- EVE    |            |            |  esplanade ---- Atrium
 |            |            |            |            |
 14 --------- 24 --------- 34 --------- 44 --------- 54
              |                         |            |
              |                         | tumulus ---+
              |                         |            |
 15           25     tour Zamanski      45           55 --------- 65
 |            |                         |            |            |
 |   patio ---+                         |  bibli L1  +--- ISIR    |
 |            |                         |            |            |
 16 --------- 26 ------- grille ------- 46 --------- 56 --------- 66 --------- Esclangon


PPTI  : 14-15 / 3ème
UFR   : 24-25 / 2ème
LIP6  : 24-25 / 4ème + 25-26 + 26-00
LPNHE : 12-22
DSI   : 33-34 / 2ème (accès par la tour 34)






















[Retourner au CICSU et prendre les escaliers]
>>> escaliers
Vous arrivez en haut des marches dans une espèce de cage en verre qui donne
sur le patio 44-55.  Vous voyez le toit en plastique qui le protège de la
pluie tout en laissant passer la lumière.  Devant vous se trouve le ``tumulus'',
une espèce de damier en 3D au milieu du patio.  Enfin, pour l'instant vous êtes
à  l'intérieur de la cage, et la porte en verre est obstinément fermée.




























>>> voir BiblioDrone-NG
Il ressemble à une (grosse) voiture téléguidée munie de capteurs et d'un
bras articulé pour manipuler des livres.  Une afficette explique qu'il
s'agit de d'un drone de Nouvelle Génération aux performances améliorées.
Hautement évolutif grâce à ses 4 emplacements pour modules optionnels et
doté d'une armure renforcée, il est conçu pour les missions de
récupération de livres les plus délicates.  Ce prototype devrait être mis
en production à la bibliothèque des licences dans quelques mois, après
d'ultimes réglages.  Vous admirez son design sportif et élégant.  Il s'en
dégage à la fois une impression de puissance contenue et d'agressivité
sauvage.  Un seul module optionnel est attaché ; dessus il y a écrit
``Compact Pulse Laser''.

>>> prendre BiblioDrone-NG
OK




                                                                      UGLIX v4.0 beta
                                                                     (library terminal)


                                                                   Library Administrator
                                                                   ---------------------
        username:  dcook
        challenge: wooed tribs rises hadda dorks
        signature:






                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                UGLIX v4.0 beta
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               (Service terminal)

                    Active user: AdrienPanguel

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              Public-key directory
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              --------------------



                    Username:                   dcook

                    Public key:
                    -----BEGIN LAMPORT PUBLIC KEY-----
                    YxxN4ciBGDd53htN8+83czGEfQuTLncrJZ1CJN9z2KH35nKjkfLqECtW+dszo+/s
                    HVJf+DgvefWbN26MKlrojk1pxr5TrCb+L9l5EQ1D00MwC2C557vXeiEDQGUphN5L
                    clkc1zGvTAWtpVnQomcL4SLK73ZYwRm3JC/r6HMsC618bMbLOUy38bYjqkcRB/1g
                    xyqTNHpMA7WVLQkYZbJ7QBBHWdtyJxGQQIrNDiNsuXCvmeMyqckG3bUfQzpM8LnP
                    NuYwl95IrmVuJT/zViRs1kcBt1PvcUKuDYtPSubIW1II0PHL0sgXge8nFq0qbsi9
                    ma9SxeU8dsb6FN1tE4ObmSmDTLpgxt+norOd5x8aIVM1eqQQEaak6ip4IUHtkUkL
                    UjSx/TtG5wfslsoiMy5R1jVDl46hPobkKhRE0RiTZuOf6RkuuXdyiTkiL7StRdQc
                    cvOaLQ1pEODf7n9beApfPdVbgBCc+0JDCNp70T3V5H4VVnJmI9SY5qHLIrd4ROB8
                    eiFJ+aMfG7CKzzKZ1y4SkP8AKmSj6OjkZ/eVdHH/RcFJhE6Cs6ZmmhfBD8hjTmrg
                    ALSe+HrZWGKMq+jixkjUm6ewMKoFuXGk2NXzOR5xJM6jFrTuQOQNVN8nmfIGr/FR
                    zX2K8TjpvjTLXNvakFvuRL5Xpr/5Zw9KZ96NvrS7v6syFEcI+kDwY1aow1sEHFNb
                    s6CoE8GyS0pPlZ8j0qURnYJCaKsbQM/MNphntQgiAj0twm3Ny/JabVWOCJ53t4Kx
                    YnOeL0zj+B7UGRd55CdRNyGR1IS/XH1qh9JqmTq/uXWx9+zxeZCQJ9nHQW5d35cT
                    Z63ULsmhCbKwSailLIDjK6JOIwz2P/wWMymZzV0///0wHMDBn7CP6p5ftHPQWZpf
                    XLrAow1CuzrvoMHGaQS0HTvfYEXybQiMh/5XfIHQbrONPq0+TjpcBR7iXVom53m2
                    tv//CRGaNchENsoH035RlWW9XPXGv6eRf0vtTEmNe6deVmTSHkF5lf5dXmYIYdqi
                    TkngEY8oERHhmyYp3l/oKxh9xUkkuv5auYxydVfXMPrTUMKv2Lxs2JrxFTrvKMgq
                    ry3Wat7zxOp/tnmDtGM4yk10VysgML54A3rqdiXhhJhmsJE/646mLxbOp8NWb2Pz
                    pu0nAP4ObLinz9ZQrxWtE1pVbXjVKnSItQpBdzUtWEDc24ZrlkQf8LQvK7HtZe0x
                    4ya3DTsA36I4L9IWy1NXDjGsPjJAL2YKyKAccwMtPmAXBlOjeqvGO2XiOYjSxgyR
                    tYMVP6uVd+D+4j9VQXU+4w+iXTGKPOVKOBy3ghbKvp2C5FXgay7YhpuiUBA4G2Rw
                    UwsWdq2oT6scB2J6yb6CbudSz19KzirCbDihQFuu/IKFTv0BgZGbPfwEjIJqEi1+
                    lQhFjIZY86L3JOlCrOHoaQatwezIH79T7VykZ2Ug5cTUdsaJ3nbLDYdJGPN/DBbK
                    FexpI2KyO04xRiLuaj/WbC/VotreHNykxiUNQqEMjNF25gAt0QjI78vzv77x9qtK
                    SlWbphs/s/DdcyAGFF9CcufFu+AqbpbWHFkOfNO24+lmNPPf5USKKxg0dH2I7fpz
                    wzq96BBzjGKe0xq/ot5ETkL3OSC1GSWeCcRvnCw6DEJg1Wk+6Kb5CRnfJfzsyVrP
                    lPGySFPqSZ/6o35bY0h2i1bVG0cn0VYZlk2s/8yBn8OR3o4edr/QkGHPuG3JXDij
                    gettKpxnD7Ab8tMdDw6pn+MqazwpQ3E7BKLeCgj+7RpFU7cYXVWzF9rM1KKmrsqs
                    3xqXgBzo5kVPQ2CnI8RdUYCYmM4k+czaMNrG8FVbDPY8uk1XRqUBEFSSICin89b7
                    9WCJaBMXI4j8piFzSiYpQ3JciryiVmYcxNOn6yZgJmTrm/DvWE562qEubcylAOWD
                    NJRT8qOXmgnHHqrLyWdzfhgWuhzrSm1Y8TgPMoF+ODzL/vULmrabrnVEP3beBfkP
                    1xbaq3BYuRTKkOy6WaROEuvlUiaAoALagFxBZ6Fe69c7cknh+yzhHOpL/bnICR+W
                    NKbNlvPVyDbbDjJmGHL0Pkd17VkeY3B3Wf7ZGnmttFTmaQFozMLfArbZvAOM7L0r
                    73CW2eBPC1Xwqomkmv26ZxQzEn6mdKHgTiFTRoeaAlFTsArBkHiuJhY3u3u6tkLZ
                    aWxrtq9tAf4hqP4YxLada3hJMvEGzQP2o3Ox9byUs1wJAUcR9/6OmzHgS1sHZ316
                    KYfXyDeWD7Keh1zuZ84y76OwxSleFf+XElt94EpIx+76xbYcyY/5jWJnUAQ4tzb2
                    w6jYYMDhPPkKsrGD/k0XHHpGX3hp2wfbUtjabakTg7FLae3Yayd1yT2ND3AE0hSD
                    SXyaar7WeATdrG8KSL90r/NKvnr5uouMdT6PTk48Ze7EmpRM6K67tEOI30u5Dq6y
                    eFzxWm8KVcIoZv+naIlT8iUj1JhtnibtPgACyhbfaw13NjYL+yP+uwTU9BB3lDaT
                    UmXaL4WS8ufXUv855V4Az48bQZg0v0kV8iN/Lk9iE2hD6p54I0IjpPBFoR7n5254
                    aZfVTbfk0LyueY1uoliD322k1LE+U6hoDF0+tqUYL8SP55xIUfM4pVZitspACSm0
                    LLjtrtZBgBlaWPL19nKyuG+2E1AxpGzpXZlWX7oLw1Tt+RmWhzkNB88SnuEEbWAR
                    //H3Wg4aDBjY8MbwtDl1HmoAvk4X3oTY2NJPdkAF1sEsbWXh+Zl4C+h6I6FIn7wq
                    CB+4gy0Jgh+2QFi59aPPCeiTQg/q7xU89jJ+Ioig2t5NBvhxdvhHb1f1d2nA6+0X
                    /k6k+/8jIbbK4c7PZCmNsNMuMk5KbSd/YB6u8I1uHnosRqRj1ti3Uv4M24DEyuuH
                    wCxB+WxYG7hIAuk5s3Wh/jHGauO7GXwtM2ZSWK+DBDMEwXSnWurVxvpgTvtXC35a
                    f5xO2kh29qoh0iItb6Ribta9htUeH3hwHf7RTsXP2y6ovNXmMjhYOnAHJccaPQDs
                    KPBiUgXUhnU9+3/bNhQUxNIOWKSq1PmlFCXAWASxfWQg5KH8kMkPo3f47e2+LIol
                    EJwvaMXxlgviJanOC6l2JkHsnpRGAA7mHEa6rhJgS8WM9dlgse2EaEfMM48DCm65
                    vECTEFogwlP5dbBu0wt1iAXllAZ1VyTZ5o7oop4EXn9+gyP90HZodBeDVNfvDU4P
                    10ZSH2EPK8d/Ms+dHoIYjK+msyBHpUgcQAzcdfEOTszvK3HRRDtNlSQHVH1G9xZT
                    chlKwc/2/ko/GLtzM9nB7O1qP3+/BM0/YGrxWi2nZIjOBBCPObq+j6Ls87kveU1D
                    fcoPilZSZQcEPh/KiHT4NcMTa9KakkrNlNzP5A8x0iu51v9x6kSkipcuzn2hxkTV
                    6B9kSXkOT+ht1PJ1tQHPObjiqPeGzpmQP5jSpk6p1scPAOugVKSBiS/dBijZ5QIb
                    dU42E0DTuUPtFv4enGlbq/KqeB8KzpK32gKRi7WhD+lLpi4u5PLt4kQKFlpMQWra
                    8ztNn01ikAYRHUjHJlG14LCJ3w9UiOB7/FiIZpmuyCVD41xr2LHxChdc9/zR2yXR
                    gMG5RjKTr/JTXDef6Od6/t/oQg/W2NfnBqM2L9JofwM+EdDK4q29ffuRf/tIu0if
                    tgsPoRT1phnlpgJQEH4EE0cQocwJcwdtdUSYrlxbEumPBSmaI9reg8QbwD8Lza6D
                    HlcAfnNDd2sO5fL6/pEAc5RrJQAEgAhbXI8uJBIXiXywHOrG2czkCE1+OQPr8cSB
                    moHuVDReNmHUQKpDTCTS/yiBmrhzXETI2TgtOGN8RwIfr7I8xnl6VGgTmah7gWQt
                    904l2FPXkyntfnC6mxCLz1OeV3WQm5H9IboOJ2Aui3gOUhe3AwObzEc+eOzH76HD
                    K04Uy6auADaSwACPPgxTWttbe9j4GDs7zSW3GJml0jldTeSSxfHmPuxxGh0X4vYU
                    jVHUU3Mq2wQIaBbcYimpUg8HEhgKQK8o6y0OHiGQ59YHIPmco/v6fhJKssrqKmS8
                    nIK2hjWtp+BQ3sZdKhHYT7emfy+9WwPk0sF+DPwCQdY6enTPf3UUIjTSq0WxaTJj
                    Ey5pRpmaCAv49XwnE34ZRlRxdJpMur6szTZ1ho8PDocvpmolZEv1bwWX48bysEYY
                    AEhnaNVZzK9TtDa6XDnFZks+FHgvw2vDLr6o3RoGs/hQxMC68cpsa1eNYB5fyKSf
                    GagT0/kDo4c5Rpm2/Lq+EfXYlPWHjMl9qFulyKBMcuClrfGE8kZliHqe7fUFFtMM
                    i9gij3T1JXfVv/EbbCDbrWqjRMEOwr8xNBQ+kiJcw7/j+QxOCvsmqzIUXaHjkIxH
                    736+xErxTBOUf41Vj8mxEJTKGxh8C5Sld0Uek6jeQ2wOdWQGStHTpEbU1r9gW4N3
                    sMSKbRLxeAq9CsP4ZTaCBNgwkzCbc2lInSi9qmll3jENvR06wuvxypdQ8dFibu+a
                    PVYE4Go5JMnNgnQXiQbkSD+rXkUn7wUie44o4CUs7eHLewE6yr6RZW02A4tbOpC4
                    ZHoQPE/74qaoD2dDB0mRXQOHVVwVrU9lgt8HV/OQ1VRzKe+twdGKV6JtJuAPoB3+
                    NmXNEegMdF98rNAxvfuyw6hjRMaf03civNhoPINWCFDee1P8gJtyE65fb+Z7JgK8
                    8gHn5Teh6QX7wupsQAN87Wv1SZ4YP+yVGz5DI0SeKAU53pP+/FuKXMQknMdQK4hW
                    KBzvJQzNKH0v+EabN47dxCUvvbuhpD3gjlcgyFsDDpoarPFcP9VsCtgKDoMW/WUc
                    Y9yWFTDSoprh5NTP4MPVvNsmMVF5cKuOftyTv2/uWxzgCPxi2x0diwVFvjnwxFq1
                    z5Vh8wFJdLCVX6bYROl3XsvHvgTHLlsG1v1rbr1ixIQktcpvunAdFQTdi5lqWQwD
                    h3WL9xIUg5HwJvKNW8jdGvr/Q1T27uJBAoW04JGpRoBRzA+niehN42A7hGwPFD/m
                    oydCUJ4bZIU6IbBZ5ZIqhzxMHo9U/fK2Ud7ITVGLeVZe2xcvv3JDMaPie+8jKM1N
                    bayDqPs6Uk9r18TDs12daWNFPx5kWKaGZgQvKNMX45xic/xZz3YfnV6VwAzeOdsj
                    6ITR/yWrGXDnv+OCmXwXnKuhnLYG67RuNB19g0ldoTuTfGldRYRj8PWlqPYO4Moj
                    YNHHemR87/q9NpiF4E56r36zKb3SGoHp/helhuUJz8qiDuOY6+TL8lsWD6LGK0Fw
                    9DyphIzDb/KpqXt6U1JCwaHpyzdBKj0nGi2uH6Ujbx6BusSb7Sfw7zAZH3mQhcix
                    7BBZLjjUFklNTHOppAmTKRpTReM9lc8byrzBk+PG0jOiAYaARVQqJhodus4yboro
                    3hZS9EwpQckTewraC3mUgvUUbeDUOZqt8UX4uWCMJCz5kSmBZ4OB6wEIxm+JJMdB
                    Bq9NbVzDM5ybvxmk9Ok1AOnUn3Eej17XUIWobXjOP4etLZhYZ51gXYYxJpF0pUAI
                    OAkjo0kah7NOx9Q+RZKz5zbzPD2Se7NqH+deNdSHECCDHhsMwPfvd6FK99ix1udG
                    ETaMXjSLIEmmaYmBTFZGPNOWM63wKb1mxmNoR11znjUnJKmdMxmMc5PSzPbPiPNV
                    GpwT9w2Z+2XMydRwycXENLUctYxNDtqIGL21jrruH1oICjW4u4+EOOjmMiUkn2HA
                    MZK1VDO3NgnjYzFu+gQmCohzZWm6Cp1AuD4kTukKBx2pIv/ALrXMhC4z4B1iWIRR
                    Vidjlqkv58LO+5YCwzvifXbTctNtCCJe8o9ZQZ3vGwldQvjvOoFcJgdw0c1OHqIv
                    KJDstLH5E5nUQkQ6riRdytaFesCrhp91u8SbRqQL3syHVbCYVNl+STBKfue4+qg/
                    mXCvBp05Ug6QG7G4GrL++ilWwuD8thK1PcbSjQuj+db620EfbMopzwEagIuHDOQM
                    Yu+zbo4eU3HFhXfEsQFJHy5Gp2qTYw/OrTehd2DkptzgjFQzfhj45WqKMkFito5L
                    AUnDUTT0BzFgx0Xekt1xxoR6jL3mQkaS7TSeIEsmfAtlboaKizStgHbn1I8vh9Ik
                    W4YGSgOxJ+qBs8x8LBt1mWNGrAnFjuHQ8yyLGZo6QTxJCUStPdRpm0yhEqDOYmKp
                    myLzBS5vSw3upStCFREGPI4BWRYv3W8e4PrJ7cowFo6YYToYOXPecFE20GZRC3gt
                    2M5bYtybrfWSzxWqBV1ewSdJOzIaYBQDex+noCUfelR8302ynICLXwuqn5oUQBBH
                    TUhrKNiVO6ZaaOzMkGhwWYa+bLfmy9FGDveHfkXitHv1BSSNLA2u5r/zbKbTt7wy
                    Xz8KHn2FGMGrL3DkGOmhCi5BA4+0zHupLuuxRhij5rte+01tgRSheDOz1qmKRy7O
                    yflaWQ33NE0w8kPQRiyUPnLf9PsIvhsYJH4X9GiKNShEsX9ghsy72rBaaRgTzmhr
                    vOntJ0ma/EcaSMVLGDvFh75/6nMdsz5xMXXCiu9WnsMUHDEZM1IABUf9o/DiOMnp
                    zaHZNXQvaIb+TYpAou/gCqWZghRLmFti+b4rSXsdIWWtUZKcr9R/CM/5PwZtT5+8
                    FpkuRghj3CZEuIoTPfDd6tQMfYV/DvDGPd5d15U+033/hXMVmn6L8jhNurIUYl/d
                    Cr3I1VeKyAk5kf6Y61ozobVDZI+6acs432E+R8mbxb6afBCDB/Sqr9QJo3w4M58M
                    /3bLOrf9baANmfAVco14hpfJREfF57oHvP5B2sd5ud56y+eOBLtRJxewws9gtvAM
                    g8NPziGAoVIlO8PB6Np6A8vuFv4pF5A47QEcw3ZuiAFKrhQqW+rIFlD2N6A5Skjt
                    Hsg+L399Zr/UHZUoN0JNjP19Sp5v+y1wB5v0DuBcjM4f3T+A1J7PfXIVcUA0WPOr
                    ZQ7ZlkUsYFtBwHrRZDCIMN5QXHr67VfN32KeinyxKkApBDtlbDRIiC7F0Lf++DSE
                    CRrkHglBWhwJTHFi95KeAvve8vLC9LdcIK5zU266F5tso79RxUkBJkhIrzcoBj5E
                    F3peIL6rd9EWt4fHqcmZCoQ1LSe6aeAJ3aaSq0pZTSoXN60Xd0UGpYr1FKn9tMNJ
                    dnckkJ5alZ2a4LdlP8lFxHCb407Dooyfn8LM2y/0fws7E207FTNELAAhCYlIHcjd
                    JjAgFVtXYvTz0+G8dQRNop5kaThwTyOda7ZsjNqw0wvntpgW7YArsGvNkBRMSzeS
                    uqtFKzPFcrxT8XPmJ0L73JoFxdhHUVths8YMk8NxjpQLYf0T6vCOXHmPOikn8eqC
                    ua63kezWg0qH0l28m7td0o02GabUwuwUfD56zFlAmZItt5MTYyyIbAJXoyzqOc/j
                    hD7LMVMXwVZPiFioLYfZPu8bfWraRmoSzQW11ngzlvRgZGSFSPZSRXLM/ClA1QbT
                    0CODuPRCQDx6bRIsu2/5ST1xTSx2brNxwIHwRV06M/W5hNJZFOM1kzDQiKkhsUEr
                    jgeVA4/oikUBOzx50iLlszR0fa8J3tkwrsjBuAJTnH1XoPg5zV7mSujG6AH8RkOG
                    io4u0Je85yAn/BNbvI0WouBb6XDHExPq4FgKlP6jEye8VPO/E4DMY9kU8rjJUaT4
                    7U5FFVufP9SXICpcJPEVGQIO0wwxbbiqdCjPRdGi4Y31+RHMC/9znXXYY1dSKCZa
                    PIU7UImPyI0S+yPXkwvFUYRVW2qjmpIrapTsHghfLZ6PuXpIg0O/sWKx+Z4OeKFj
                    6UbYkBP3sgQs64r/I4Ql1FQshN9M7A7BWxlsCl1PUNAB411NoyLLQpNAXU/jzYoT
                    XboADPv39GG3c8C6baJuMYBBqrW8lJbi8awt3ps++hFfqb4Xg1j3hR4ra+lGsmzP
                    5AEfAZZaGqcK6R28q6v1b45K9n4Xpbjy4kxGhOTcKFHq525tbgXedDJ+IcYvPPNO
                    qnRQZAHru5hCpoLHPchWhqb6y0DZIqbHfbZy+p//6nIYW/Hbukd45f6wrJR8pr1G
                    4W0351atcqTe8U60mTjE0wiL38RwGRKRCuVrQbbNBr1mE3UJUrn3FqglUk8Qkz+c
                    PLNdlsP7Wy0xoIJVxi/DLn7oeKOKxI7Ru/2xjXQNgsrYGYsmasnNTxkZDWdXjXLH
                    1wOmv2Ort757hPJ0qXh7KJRDwHOdkEac/oc2wJ6F3mkhLvfaiUgzgOvA+t6DOIvu
                    DXk1Drhf9F+o1PZzCAccUgmUVmL++bqHH1MOwh8Tm0xJzA0WDl8U/WH88mPZPUkE
                    LP/tVKMKjWpeSFxiJbJ+bGN1Mf6Foi8SIQv/dsNGxfjZ7KQt+n5jw9d9VLcCM3tV
                    qyZ2Bvbam+aOB2qbU0QoypIcs+mT3n/4zEGYVuW3ETGYVcjVBq1yOPTAqm2GaJFg
                    SwZp5lRLYgLZrF9TZz2amfGL7F09AzUx5lYMFlwvNW2vB048X3IxzGcny3Fmrm0W
                    oYHR20sCc0Y0HhSo2wQWgVTcymbO59lRdTIMYUWUrLj8WGGr1a4KULS9JKPcKL6R
                    s5TH6wcxM5qo2HCgweQI5xeeafiLkUlZ99ntq1lrqTjwcOvmhFnOd8MHXzJFEsMI
                    wCcW1x9XcNMbwD7EAPEkBK2mMSiK2e6fFPl4AdCk9MFpJj/eOvWIPL41eoooYpLG
                    iDiP26I0fFc2zCiXLZr7ffidN2Nj2j8Qyok7ldqdtr81JmJuNERAFtP+6TO+PJwW
                    siguxfrdxIRG17xObLU+iizUbSkwW0kaUfXwu6ToIskNEg8LfAilH106KAIY/age
                    Ph3XOfOnfIo7yxSEAicv34s2AKhH9/D2ViyK/b+TX4ZTp/1LlEkEch0REAPkCc9a
                    q7cYzZr7EoUTYifMI4pQww1lksb0BQr4DV3rqbK47sBuW4Btxho5w+KVsGWDceRC
                    V1aX07sj+L8aiF2O+4oA3JzFjGXd0EWXCE2UhplU0ov5KCYwpA1al+5QDQU/zt+d
                    9g0FHQxwyMzEoJpeBn+abG12b7WCPIUm1thbicPNiIOk5yIz6ojDY1sIAyOvPsf7
                    vEy10bhWZUE/6708VEIG2v7p47zNV4tZH7BWJCvxWC25dOEmVFWCpq0ziH/AkewX
                    tYnlEn1JePNAhVTKRNPbWigJ58TQ12/KLQsyhDm5JNddqm0fT4KO87XnBta4gIWr
                    3b4yx+csLmWdPHmOsTb0+V4htlTEGSP+Uut1HD/sDnhRfeEPVSMHLEk5yICbwPdN
                    LcDLdo06UnEcACZ6Ih05oAf1dx901BHgKA8A9I0GQ+7yKubdgytP9HLqFIHcojII
                    SbhrlaEYIFZYVF5e7gIzEV0UShY+UYXSRgDsAfFZLACO+56sQhHgHI96LSNY1wg5
                    FL9X/HOzSOyFGn2ycqUBkvGNJgaEY0AchEpTztByXz8QRHprQXxw0wDyrpUeTGqr
                    JpUoEjhNGLOJw93Mjkgj2qX9glF8nn05ZdKjqGcmGzgB4zx8YEmQ3tzPYc1S3gnH
                    Z1uev1h0VU/ml2oGsxY55JocIeNAPmoVwmYN75jof8909hKFetWPSDPE8cH0fn2t
                    T+aX5aDKJWhzjyaXqNVtskFzp82+FoKBCBHBqVn+Jdjw89lXAfuYxU5W0OxOLcp0
                    IBZZ7Fj+7rriaimyjiL0T6ul7+cpRAkoAHjEXSyzXofZHBueONG+B99w6JnhgGp8
                    BCAaEV8spgfOFJJeRpKOKha+Di1Kqif9sNJy23dCDXeNtLblWgScSS3CXvex1PfU
                    tJE+zrOJt94BhNkomRo4uu+1Ir1L6u7tFLOJixGafEHNvv+I2PYZXqn6XF2qeCFm
                    H5bReytHsVn2WgRVw3suW5UZDIk36LWLnKjU2kyux++UPXncOWsdM2Ax9oQkLRl4
                    nAAHb303w3yJ8MWvZTcFH4mOxwiHWgd9JmCEhkb1sShxs1MkGZwU7b8Ok3UAp3hE
                    RsedqLhnNlWwzZuuDRkiXKHZgOXA/iSpzn9F74UWSYhqqKiql3ZVuwW6nAQsnt0q
                    e7SBKJT+6o1GlQiOmwbL/uRoyvcw63MJeRGLocbp2L+YocE3Npev+M8VjBFclHzO
                    8qPnHVLVadp4iDWjRLBM8EKKaV1YflLf1+EoptYKcWMD3TKjYCePn3wUHX3BtIK5
                    XmUCTGxaEJHCrAuluxNO4sRJqAao9+34EamnbMjNOaqnJlia12+1PuZaBOrzNoD+
                    P5T+PlUOUoTPrT/quwvn72WpJcxw8qe6CaN9PxFzt34v95NFjz9e/BzJt2VBaoMP
                    Mw5V92OB330eq9SMclHY+1pt7rcDK5j7ZkwYKUqASnFUuZ3PUneU0Or5r7ALGesF
                    9BQyAuqDbY6bqhrD8NcPIuNcOegmMDwWuUW2usK5EXg+zlSGt2QY9/RZVni7L1jC
                    DpjoT8SnM3YyobCyG4+URZGO3pfsJmSDVEDOlsxcpNqVgl5uskthdTKHn6VywY5X
                    zxR+fKYqouOSv2Ztk5dIyTkfBYNg0l+U/Va4h8UkM0zQJ/5GvCDrhk7da+HhqXrm
                    myfqo85o0NKwQFsdxvDZ2QJ5YjQMLevQ3VBmhnicO5NCxltUbWXxU+5XS60289jH
                    EjLvlQDl2PxSaQe3KosxZPCHjuFvch0nUCyTH49CBYnZ7ii6Smahnu3KiI2Clq0m
                    gChPH80oa/nmaUySEQ3hgL/1YSxF29SY6VK1nfmR2Bg/CQYODTt3RXzVk+Mx6WHv
                    lEunDXF7cKKRfF+s+D19HuHGdAmIR0XL7y2xH5oT35ZOrzE3wSNWmD0vHZoAgbpZ
                    YGLFy5bc+QmjlidQAoQdwweirhQOfwwW0WoFo+FtxdkDAffNghd8TwkWYHBmM1oa
                    XWlgXo6qJ0I+zoaU+iiOLcToxA6Ec1J29l/Ywf9X3VsFvZJBlBL53rMiuS3LrCLf
                    Ixtee7BQcK8xMAE3lJfezxhgenBJZcGw5CPcW0cesLwAp4LjFqkiJtjB6ex/AttV
                    fiwoEFyMcNQ7LRKRDzZ5p4S84dRj42dkvrsr/GY2F1Fchl4hp8ZkdyIaUMUr8E8m
                    1fGJlV4cFfQbLMg0THiphEi5mxnyd/7O+dkV1spE1n2NO1+9/UZ0ui84JJFBEzk7
                    IhLkbNUsTBdSbASy6sHqTwKA5+CckVNvGnie0HdW2vSFDJ7C3UOzAWfZQtxboxTi
                    nECSEBcqTOGTikgIaBbSceADblWlyHLFwi9A5kNqdePqsjF3GCux8io68jvtEEf0
                    AyWAVwAeWOVIfsp61M9/rHiOiR3w/k4xXWWxEcyyVZcNeyv6IR8N3tb8LYQvO5La
                    R0goJ0tsnFT3oUx85R9/o/du4RVSRLMBy1kpVIpxsWvhiZw/T651Pt+nnA5P4CgH
                    xgcJWxBTO1glznuel0uV8ix3yQNA/kzXrBSbA+JDBxxkz7cWxeVOE19zJ61iQVAk
                    m7gWxoSdUcQ7VSod/lfkulMsxaGBVbWz/O3Bep9ixRofgfASSmgZ1s+5oTCD2cOl
                    5CWBbzHD2x3JWFy7G1/IcinzywC9Fl2pxU7ZzJhw8IkTbdXhOv8k1lZAjvKKBmKk
                    +u0adKod9t1+syJlWj95eUcMpQrTWRqy3BaKljDe7yGJ1K6lh6efPSlXwq1eOS4C
                    zWXBEeV0juoRJ4vOSonvQPFDpBrcIaalfQfTCUezhw8CNNB1jrIlL63aidG3vz5m
                    pJf/IwHq3Py1pDZlmJktaCH1Sy7jIxT2Wgh+TbsWGjDLGkdKMI4It1umJC18npvB
                    3ys4epOPJlYypTcRKceS8jUNmaMUe5lDn7non/W1uW9E0H9fauX3fcK1EXgRQgHC
                    iSmmSjOfX8RPz6PQKc8pNvTzJaWPTGtgV8JxERUBCIH49g9hkJXDss4c6hw/IIMr
                    TyKu1kuUQ2fNEwp2qxnigkpLmoyTZQvKwSSzv+sZomkivHCCvZahgf7Gww+3TcK0
                    oHS1TNBvH9WffdWC1dnu2SleEn5tQ3k8ystU4lR5mHOLJ3u3Mslm8gvE2aqMmc/H
                    7mvtMbyhwzkGYMGywf6Pkh4NpX/bx2d9gQp1y9R/61qZhz4RnjwLPmSSuUJyTD3P
                    AltCVvgWe9yhvJG7H8gdALiQc8rDfHBnYg2eK9Dg4/7iEQkcGttfLATMnbuS2jIb
                    KBCTGKyVBcgYVGPxf+r40OSrsmcygxLsS5Y1KAr5UExhQPQb+r5OnrFPXYPgdmk5
                    G6+JV8+Kg80C6L5d7HLDH1eBfhx6xpeq6poSDqz3ME4E+JUuSjphlwK7J3IjedH8
                    EtMGlBo1UgQ/nijbsOygBcA/oj0Miu0j/1d2Ys3Xze6T9numAkB0/RBW3sarNa7N
                    iPzS85NEv8XuJ4E2qJIFUVx49EaaObGW5eHznW4LaPBSYrrIdT15IrLR+N52b996
                    mGM64g/fhmUQlqeF69YspWisyvOKX+IuaVqrEPecs1pdkk+yRZIxz3WYDnLobFZy
                    VPtchleeVHyOmqZvLtMrtvUsryfiRVDizQCMTJuT7IF3xbON6oLhLE4wrmMydMMr
                    50qVfDEluCyvI6yvt2qir47/Rji/04I8f8XLuX/GRdD3CMVnCJ15B+0OzuQQYoPE
                    MXir54qdXncRulo6nn7n421rtDEMXeCjlofK5zK7US1yx3qQkcKM43J4WZQTjdGj
                    lH9HkdHJEIeTjteMLGexN9eqHz0sRW1IjCtZPJ54Hl7wE87Zkuop9C2mdMO8wOfb
                    HinHLz2CuQ2Iq1DVsXuqVgXx4jZpHnV+0zzHZm4gFJhp9/YxzhcXptYZkOpGqZz1
                    R2Y8YrFGjQV2mjNhaCYXQLDvWlpyrfagqpUbU5qgAWL+EjsodEztAbIr5/+NcuLF
                    m4xdooqfAEoe3vT2Xc6e9CpjtcZI49daCJA8XbQmjT/bia/tpBlQgrvgVi/bLn4I
                    Zsi5MkgPQvYzB1gdLkngnLsSrJ2zThpmwJOIhdPiLZm+mcXt3QWMeJxT7PpB8BD6
                    Odnz1ZKdWpvZ4I94rqjWxPXGTEWRRWwaXAoux+B+yZRa9+IW8AGMKLzidRBJYD8I
                    O4YcXalca4TSTf6ulxpuFU90cB3kHOSxZgRWWOmtTNP33pDfvdLxaa2fy816qYzD
                    dfSnW7TCefBbSri7ih5eQlc752frXMdqIhIyc1DEZF+RAxbDKeazMHjMxcS0/Mzo
                    5nC5IdQXrfY3RG4718167s6wpTFW+yHehdFdbiLyQqQnYzv3hWClepCCCzVUiOpp
                    +Retr93bT30Vubdj0YNd6Sg15L8hZol4/3Ox4kHTk752JGIz8ZOxuAp9lD5GsMI3
                    dgMSleMTa0ip4lOgOPwe8tLhzD5P9cEqAceMR8yFkUmtWaAeKWNDjTpdgNNmyF2v
                    HUJAJeVXuYCcyWXU2c0nvX3sh3Rl2gHFjiik5u6e2WjpbVKtXdFMpc3kPJanTXbH
                    YWdqQY0HKsh+npH3ilxAyAflWQL/HJwJlFHvcA3hGjV8edvChO6XTPOVv5lI1Okm
                    AxvXXpOVXO+MPCl7MAom5GAHm1tf+a/spYVOVh9pJrZ4S9Kd6x7D0XMXeBp1mzxH
                    YVIT29FLKbkDFAK79jh79wASxbcrak1udfXlQHQgYkoqEYJ/FrIrbhvbj67vLhO+
                    dGlB1yMG6J2/7lpg7bdugtrqjAKfF3ThYjmEnqgTuHpjnSk4AF6sIqGYSArc2JXI
                    J6V/XkmVcXUrm7oXavkl5RypaR8yIggrBWKPmZtL/hbJjMdxkHEQl0X5Mai9ZBS3
                    WMUnB9Be6BCGIxPl5Mnp+CinxH6qvqcJ1iZJzfE4fGDBEr/wrWnsq30lARIBGnKB
                    dUxs1xDM29nax8tOLDRoPyyhdqi1wFibeQhnV4IVn7vfh3mhhRg67Jb5xIe+ijnM
                    qIo7kXEtKrgWPbxyq7F0PnCI9PpVRQ/Tz6HdV6R8euAOi+YqXECwETO6beGoRb/J
                    Kn0tJv0B2pcgh2OGNL6gHwlkON/594Rfb1IQsS0noJ6F+3rCZe7Fgyt5nt7oGKqJ
                    9jAGK11GojMReHRYhXJBUR0yoGf3NonQOg0MU0y8E6pZJVhvuPG0m1/DdXX0CVrP
                    e8SBkG/cR11hMM3jv+lfHbhYD1EydHvfKfF34eORpd6Qd6Ze724d+insaQ4aA2Da
                    W6pH1cCx5r3maqOd1K7t6jPErvlSTQpwAs463ujQGphz2srJYjDb6fiKwdPqEO2Y
                    cXSZrpjiAZ43y8CR1UVe+LfgKAatChO7DETQ1MQjznE05G29E1jUb9OqMYxk9YiI
                    oKACDXxJXrfKQk5bMUzP1k0j1PUvzV43ATTVUucfMAKyAgj/3c2JowsifKH6s3SX
                    sq7wUc6mgyR/W51PsPKle/GG1pIs25WBBVUmv7LnE77B5lqdsBJWDRNvnrnLFInL
                    9bBF3X9JWDE+ctM9vUruqCh8RpqXwFpiHqiv6bTlw8HW7yr9p8ebwe99IJ2rLr0T
                    dJxU9ZB5LY3cdOlFqPA84sKxHxHnu7IBXJB3kVdZT8aM0OIq4O+81cBlZkSgMCQ4
                    C7Q05K2K/UST9q6RYJF6lpnJko7tZI2ywXAFkcb/aA1LnVnXBPKgLk5HGWIGOPOb
                    DUHQQht2u9btqXLwyAWrEHWBsvb4iuEavCxIdqHLIbymdU8TlCoGpVBI/VSK+4p2
                    Qu6bz2W7EeFrw8z8qj+N6zBjYMhWctUw9Zkf4JEa6Wyx/TUwiDauyOd925NHSjht
                    kEs+WT8ZvK01rN7JkF9MpZ0+t3bJiz++NiVI0eKhBEe0KSW8KeocIbRpn4DPrA8E
                    nj1Y1mm1csy1CEPyAS3dv0I1iONx5p0gsAFzYD1/04uja8lScKKQ/+ouviB5r3h+
                    wTHTZD6MOCX74CDtEErcmUivHzSaJzbpuqYquByHtjAWHQzVWWct7mMNCkkzM+e0
                    xUiV31gcsomRL+ZtAnymDb2WBAKQnn65X5aykfqs4b/d0jR/9Ocav/9vIk85hulM
                    Rph71jEhfRvwoIX35suqVcUu/R+I/DZmlf2MyH7Dqlq9dEIAF3uxeRKXKL0rG5Un
                    qfUY9f50IE9gqvS01ripeYIKRa8DVcNw36i6/0AlEMGwufWXWyQCeycfSqndLGHV
                    FFzliDulUAvK/Xa9ML745VfgLo4ZKYDED4noGviVVoHegEdpMFCLd4S9ARMcgX85
                    9mDMDxPwXMQgaktmZnBh4at2Xs8/7Kv3olvOPWPuMLZ19usAZ1WBvHE99I07zPhU
                    0SPWv4pHGwck79ZSXlW/TJjEwhFxqs5B5V1/xgp9OIQ2YYPvt6cLIonY2310eC0w
                    U+fDiV7qklGmXwzoWp1iorKlaYcOiLb3ZphfQufjH5kXev/sEqQur5hXZ5fSDG/N
                    CB3B1p46jmKdRPSTceqw9SlIQK8Mr5ZeIC2FYdty0j0oDG5u0gClq2tYHJHfmAlL
                    +Rh5AQVv0aKLxTc5iU0DOTY5xhmQtAa23+m0g9KzWJTmiVezGfsWvTOSChTIlSs7
                    897iV/IpYAC4dl32UqAZwZrLM5tRwUA7EUysFCMrXtf8g7myMCYKNzIgKqP1Xnhr
                    qwYHHBjbDTGv1I7GMXXNVuex3/HcJJ+MjSzRJeh8QvrJmFtEnewHdpKu0hDWvN1j
                    s/I4byV/awLK1ekR0Ju0LR54pDu0uz7Nz8iN3G8qOIW+ZRFWN4QxGrYgDdAIJGIB
                    8+qi51MlZ+x5vRR3FAPavQsqQ1Zd3I4LkVQzkcE9/1K8yrSm7ajGLLR7cANQXaKQ
                    H1JkN9+fo+2/rvKsLIpP4H9owAp5BFg4cBBQtgwZ7nLiPWhp5u1WRSgu/mcUeApJ
                    Hw0rnIStaHMaNQrZdOhgd0BwJpt5cia2msUypEQXsHdDLeWb6GNkPmjFFzRz5s/M
                    QdCFfyKdtLon3XE4UxsnAaSIjdbuZxm18XNTB8I7CxlsS+QC9e8OCMcFHZ6fmtEt
                    yLYhyzWl72FPAhd0NGx+Oibx/YfUWVVIX4wpY+bCiNeajUrhw6oHkn4SqEYei3XQ
                    7alNC0n5gCtwdjaiBzy5qRsMBwgoE9v90ThxNSzTjkwYoeXEf0qjR1cEOaGle6ml
                    gtL+N4dcezbtb8NQHQ1foDT/1kr35DC+TO0+TsttyZfltexE/2z3GASUcz2CcDt2
                    uHB+AO0nZm6CMlo2U3Ie5+EZDSjXsobSEqmS5QKssRJFaz3MBnczFiW2dfEVUwzk
                    BwqLZw0dJMZP9AntyS+YelWpe1gA9WO/Y7m1EuGwgOGtPApHPpTSeQ5EupiMv4Bc
                    wE0iZpxwzzSvT1+8oKAyL+gjn70RVI47tlmB+xVbt/cWAAfY3NGqkwRLqzQIFWMB
                    VWZF2nEEEOZc3yUCjfqwV+s3vJvcaTR+nlJoynDaF3Y5gI0KCdN0BD6FHMYnU1Cm
                    239nNtFquhfqyDk1ijGHoHRUoiCI3xi6eYJ1E2kbcXIRSE08GpkmHBYfey4JzIkT
                    XxXI+76EFkEt9WvgErdnIZR37hjR3YUHSK97LGZyn1lWCC7Cl6AAKm25URl8L1JX
                    xRAh6EChqma6MT+nmYCJ4rXvypx+Cig7iYt2qolKpAx8JQMttcKhqa5OjAF+Dxc/
                    5a78PAcBNHMt9XcuWLuinO7df3QKbN/p1iDDHdYifbz4UrwJgg7bBthxDVfec5Se
                    ZI97yZivifecpclOZKoAWEXN9VMlSRkvPZZLw7PpngZ48Kj8ViCJQ7xOHWP6mDtl
                    v2wo/yhjPiizjF5PailxSAjl+pJYJrys0wJ0WLxGkCYjUJrHnRz/zWxRhUwREasE
                    5YwEY6MWEy+SUL1KgaiMrA0qp9SRCCJQ6GFxPM1/Aydif0FxzXsAnCcff6zBv81I
                    6DiyrqzP2ZH0ijqnDUt7e0ffC/4wQpk0V0y3hn1bdeLuvRzIffWV7NwqhrwUaSeV
                    ucKEwa4XXtp4QYNXiKXzVpF1mxzZQ3QgyaNmiRHMJOgMrjVzcOjlgRbWLkjd5iMi
                    0iNh9vSmyLP+NJM3jeQUIAW3Ewf/t/4wv04Uo09C5Z8gXY+0p7I+v8fzVqS1rgWF
                    HFU0QyS8W+WcLlaUvVT6da9Ii4liROCiQ/Wv0XCX4zuLboNmBApJJk7Zc0Hqw7Ks
                    sy+nlPK3pf25RsKGGL4iXky5OOzfr2L9X26B4PP38Rv0+UK9ZftRA04w8ihmIitQ
                    3P4rfqTtP9lTD/1YgvuaiUHQXwcOPVBx5DaaKq5R/qntebsV+DzpERz9WuVxIXqM
                    wZrv/RUgxOtqBs3tDgumOfGeW4fkwVhrBXMmcKpWxMCNwRGeFPTAdvgiyfnIrM/I
                    UsBCSao/Edv+CMia8SMNMxg73C2qVpvqBdUe9HXkq2SFDqdFAcjbLNOmtQ+mnc26
                    sc/H2jr+CvH/oXuu2LyTB+UH95TucbVWXGIKSFxrMtlvQnrGh+CeZvc2U0k6j7nu
                    ka/rPpgrVYA/7q3hgEJeL6VFe2srWgSTQHddHM6CwkraCtsUd0FnqunnwkNYTJ7q
                    Pex+bLcG1Pz6EQH0uhYQZl8bKMv6hPm3nFbZXdLk3weFvKCVNTEAJPlXpo6tnuXz
                    UrCEo+p9I2qvWtyvL01MhlejSMRdrZ+wON1v0JMKJ6g5cOA2L/gdC/RKfiCZCAlM
                    NAH61Tq5KsMzH8ZqiO2slHuf7ooY7+jEM7qcnI3xGE+f4Sgbf4p6r3FXf8xVe+jS
                    7UafRam0OhNgucI/OEAHiah549uIaIeRo3U+mPb/KDMqJZbCbjoQ4ZylHaBXo+RN
                    MBIfwvugbtwy/yaSWnNmWq5YlqrbzpgaaaBKpWoXmn4Ut10VN8MCWDj5ndyeYA4+
                    iBqxcthoplu9RurcSQjWjAhycDco0YxKWrgXNMWzSOmyd5M7VkdLP5kUWKWxLE1I
                    xBqJgEGY1YTaZB0i5NELsKtIMXKKg3ygM2bNXK+yA5yG4RBes1x75/Qw7btsmQNe
                    rHf96xaRyRGJyFMFZWaBncUlio5K5+/VsXkXIaSe+UGOAqYAioUQMcYr+9uAoT4y
                    Au4UGvL1EpAEy0R61ibntKY/UY2RIkvqcNtm/90KmqLCQd/IEl3edjTMqriUWYWF
                    PP/MVYCaEAluxMXPaSjzZKoTKk504YJpo/Wwl/zkf33Y1fR7hDN3u7JdVes/SFUJ
                    SgxsbLMS4QnJ6UF4Og4jCaIJwLgOQe/2glwJonBnRFkCHJQzM6WLzybNggqNGUJB
                    MmFmiWdDYUe3crB4TB4PtORxu+Ze84qkdMc4vnOLDjrbtex6HAAgLq8BZU8CnSdM
                    PyRAoEdN4LFVKB+0v7LQ6K8GYzReyHcyJZCbuXh7EeQ+IOkiHcOGJkCHZDgvjegf
                    +0txr0dHUTm5oMdqRtA1Zz4/oCOSA9/ml1Vu2k/yh1r3BDGstoapCfhGE/DUV2WE
                    z97BzbxZfz8i6kXxsxRmjgera97ZGraM9AJ9RH2HqCoDEJwHvT2yTXKw+o2pt17F
                    9oS/Xtjo2NL8RnOJEab1g2hOXF4vpL0IcvlTUobynCSLOXCQ9aBNEPNVtfjH7xD/
                    XP1zhvHcMZT2W0/jteV8OHlXjKHvPr7eNfy3qJ269+izrx6EOaygFTgtreVh6pJg
                    sbS2gZEjaphijejB3CuiZIkMfC1PytEE/8xS2G8DYeAKwtjn5WC1nOazGkagOkaz
                    JJe0LVK5YeabtCffv3MP+4v2KnOI7EruEDWnh+h9ca2fnetpLSnRYmDmJy/fZM+f
                    AzV6LN7Oed3VZ812DXQPB3x31biPsETZQd8oEmEfoyfxSxZOVuQUU6PFYbx4EzA2
                    jLebEj8Pcosx2c2UxgM6Sz7jvPTVA6IMFOpZ0a0S+mvcI/PIg7UuMiEfDnpx6S+E
                    KzX37YsdZGbUOCiFG6p/sw0Tb07ViY324yYveCM7V3jo4QZXTDlVF/70IBwQOfsL
                    Pzc3HVjSAtMyyA/8ykteJnA0SACUbFwvfY8EmYZ5LPbUBIlwCniXoYr+70D6w6w5
                    9Jg+kaXkw+rVHqWlsd15ZU+k0/xwjaQCFCQ9yhSaNqJeoh/72dZ2sB/T6sp77A5C
                    L/Rg0XxAJXEtVYzWwjpdSKBApZkeBSDxYqQa2mK+FbqUK5Bpl3p39mg7tTpUo+Dm
                    +jTHRBp1EGsFmdyWxdnbX2wXjZ7SXq2kEhGECZEyszp5PMLurcxWOC9lmNALsYUY
                    b9qJzcMmT25tKMT7TnW3ZmR0/pzlnKD/D4E57wNjJKnD6cYAseUN1smD+Vc975P6
                    eQfoOOR1JnctzC6EfTn6TY8ysHeEXeLoph5W9M17byKbiq+9Vosp6WVSj6CTLpeW
                    0SBJqgsiHxi+bT4UjLPA93EoNQ97Hef0IuPFI2/BFjQGtiFibkYUzqDXesO9/IZA
                    FEasAaGIsLHCPUKayR7rGvG4i+raqFVmljT9t7PdMa/Owuq4m8ctSUG2z9I82qGI
                    hxO6SXDYjFi+u+5kUusJPGVflHmv54DTTq2lVRg/+enKSTeoxY7B0W+Eewv+fwsQ
                    a/bAslFUC9ENzGfsFNcrPHq39nvUb+5i95UnpIserLB/Xov6pCZedQ8ovPRBzezm
                    ZJj2ZQHuhdMHsqjBXbjsmZi9rr7KcznKLwErPuZJE0RZtaLbX9ulttN60YPwsJ34
                    xY56xeUMYMJu2fPstvpCaQy02cZHZYBlXwrgA+EByfTxnyaRLDR+FojR5xnEHGZ6
                    +V660DTX/SS3hAeuFVtFf1rjaSa3tBWpo72Vp6nWbf+mQI9Bq/udDr6p4O+qkh/T
                    I1WPzAlFDJonwBJ8N2Vb94T6BH+G/DehJlkhKz6MVD4VhRGHy7h2BkUtrEO+C1mf
                    8WjbUuMw5akt3GxkojW7WyMnlwrFwuKRKAAGF1n7VPw1qXOcmarFRmayGCLzi2qo
                    22XdNNCTHw/UHC+Gb0jPurarzfAhju0lmF4XwOWTQU/E7zUq9bJM4Zzb5U8gfjxy
                    wuQm3Ug+Lf/lLeseNjaCmCQ4BbueTbCboXX7jrp3pfaBbAgqq2SDuOQoBFWF+EIh
                    1hf7eIlQ9ijk04EYtLmSFwwHxJOEH9ktafQ4IuRBcvYzamUMsdfOTww0aMxqxvG6
                    RQjUv1wHifSblD6nv5WMx2wE8p1zT7VpL/zf2wuXX5TSTkyXtkSrRvS9TFkbnzxP
                    QynTWPpEV0RAKLUEsbNurDCRTHKUovJ+Kul6IxhKiQ9n1fZDz3C7F7z2JZhUIuDz
                    sJVWkIaKfI4g+dlSgt2JRqrWTSdydyZwaVFjyJgxX+SFQh3/QiIg+JfVgbNLC0xQ
                    e6hPiY+ZzKYYGDf8eIoAy6iDxMM/gP7EnehstbDShHM3X7JT2nzcc0oNdN5m5svF
                    iX0W8EZA3XZseXYQuWGihp5HClPa7PYnI/MCpg+ViiBn7UpAnak29KV4b20X/fIB
                    lm8D6hXOsY/+jkZVWPxQum5+maVulWXb8E6Pl9iFNuxCxsYsOQpZ4UlJ1mTbWKph
                    O6GuPTqjMaRMUSfOo3KLB6DM1OWeg9DmoXqhmTFJBbAXqurD1a+JYis61hkX+MYx
                    lb63Wbm2hVoh2CInU+GnupiaxxKmf/pxLEXtZQlr8h2ZJukckmW6Cxm29qxHo4/8
                    WIOsbj3xXwesalwkSmq+uFNSlMaWKsHLLFXtQvw5RBnk9pqEjnpJQjlkZgs6Qj/j
                    6WbpZJUJdphlpkEqZt2hVVBr6lbUV2hlT0jnCgxeaYiGsPRXzfsyG6DU59KAGb2R
                    n7x7N4Mmh/3BIwRMgY0EF5QICwgaSI/egeYnHpLAW0WCKZSlYBm1x1dGO6ntDKcx
                    Ro4RToN1rqC/pvRpKF2y3DrWWW5hxGOxueSKsr6FPj0iHPo5Fo9hdaPJm9WPsp6J
                    tDnIbC9hDUO68PQpDd3E1EqyJc/zylTSSZuEiOSDGQLQ+Gap9ZIwPDioJpyb4KMB
                    qs7Ukk8VRrQOp9Mv3pBFuy+QMFm4mLt1Nb0GPRoIgQyDVXCotKWhnLArDZ8VKXNo
                    P5SM0RWkB5lBxZvsCNeMTeAmg/b4WsB279tRd+hKjV33mOgGpC75ny/nScUDbEF6
                    AkOTUEJZ68+W0jF4U3YqrtLJ+AQGIPxcVlY8gp2ZSvGCOdXiBFPYb4XhQqWRCv+g
                    ngLLy+E/ugvaxPDnQtNRXJPbvrxy9p7ukTrQAgoCTcLvXxaMRM3NwMjpKHs/gaRS
                    BTOxlFUdn4WlkjlF4ZRnC1uC8WB0QLmKHNRyJdDIGOFuVi7/A9M5WkohSxLuLxAj
                    Wrj0d0+u3WcaudscgrrhiTVtfpwBRRtR/G2w+lgyt/NuGGkIEHskOqo+lpMFYoKm
                    xZCpLw4NETceAWoX+uIWQa9OMWGEd7D+A3SDKVHZBXXgq9G/IIX1vBP0GrrgEm+d
                    aOtENIhVCZKzajfCVSnx+XxEn0lR1K65kdt8g81b7dESIiny3ggDfFOXyPONNui0
                    6v3wEhsfysxdI0gJywuhm39VZEDRwPKr748TGUSwpRni9mKOquykgwJl4HSnInsf
                    Cgj9OYdSHqRybrIXkFOdzL/IZhOutLTHMCMMOWoeDolkIEX8ZuOCMRGD7D6vRdnh
                    5bS/Onq2XYegMiBJnLYBizTT7lC0tO3TDlhqg5YjPRCbbafgoH2MOpHjXOckrEIL
                    B8ZTpEiRswp7gaLsovXR1yyI8FBgx5wuTxddbZUHKESGpBw2dPnAxsgX1YOavxYj
                    msJXiu4snsrx6H/mkLSlEP4w1noGBrTYWMKnE/jtTGlWeqGyxNa4JVgSuS2TmWHe
                    VVGae0lzurFniTODRNTwJd4axPZnBYLggXrttYkNbXg8ru4sg9HeZkwRmA1tF77Z
                    5Gr4/vwaT/h81iNC4K85oXTHaifmwBR4N9RnrgDwVuAGe8RBRtCcE5LOJYTqBegB
                    ulJ6pwSNfpwN28++2NbpT0GEZ8S5lgRRvLtZvD4g4K8gz4FQmYQmzl+PkDUmr+9W
                    RZ8WEYXU7C/bps72ZUI9GA==
                    -----END LAMPORT PUBLIC KEY-----

                    Signatures:                 NONE

[press any key]



























[PEUT-ETRE UTIL EPOUR PLUS TARD]

[Au RC-07 de l'Atrium.]
>>> regarder firmware
Elle est écrite sur le coin d'une enveloppe.  Elle dit :
                    firmware update key: 35ba26a3b0297f0d

[Peut-être utile pour la suite...]



                                                      UGLIX v4.0 beta
                                                 (Firmware Update Station)

                    Active user: AdrienPanguel


                    Firmware update key:        35ba26a3b0297f0d



                               +------------------------------------------------------------+
                               | Firmware updated. New command activated: ``#!item-debug''. |
                               +------------------------------------------------------------+

















