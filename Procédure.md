# Informations sur le site:
https://m1.tme-crypto.fr/

# Lancer le terminal:
telnet m1.tme-crypto.fr 1337

# Fiche d'aide
>>> aide
Pour interagir avec le monde extérieur, il faut s'exprimer en langage
(presque) naturel.  Une phrase typique se compose d'un verbe,
éventuellement suivi d'un complément d'objet.  Dans l'ensemble, mieux
vaut parler à l'infinitif. Autant dire :
    ``regarder statue''.

C'est plus facile à comprendre que :
    ``Hmmm.... et si nous regardions la jolie statue qui se trouve dans
      la pièce, hein ?  Juste au cas où ça nous donnerait des idées...''

On peut aussi, si on préfère, essayer de parler anglais.

Comme les informaticiens aiment être perçus comme des gens lettrés,
la saisie est sensible aux accents (étudiant != etudiant).

Le monde se compose d'objets et d'endroits.

Les objets peuvent être examinés, utilisés ou pris (ça les ajoute à
l'inventaire).  Certains ont des effets particuliers quand on les
utilise.  Ils ne sont pas tous forcément très utiles.  Certains sont
particulièrement importants.  On peut parfois faire référence aux objets
en utilisant un morceau de leur nom (doc convient pour documentation).

On ne peut se déplacer que dans des endroits qui sont proches de là où
on se trouve.  On peut utiliser les points cardinaux (nord, sud, est, ouest)
si on arrive à se repérer comme ça, ou bien essayer le nom de l'endroit où
on voudrait aller.  On peut aussi essayer des directives un peu génériques
comme monter, descendre, avancer, revenir, entrer, sortir, etc.

Si le système ne réagit pas comme on s'y attend, on peut tenter de
formuler les choses autrement, ou bien alors c'est que ce qu'on veut
faire est tout simplement impossible.

On peut utiliser la commande ``conseil'' si on est coincé.
Enfin, CTRL+D permet de se déconnecter.

Merci de le signaler les bugs ou les erreurs manifestes.

# Commandes utiles

## Directions de déplacement
- n: se déplacer vers le haut
- s: se déplacer vers le bas
- e: se déplacer vers la droite
- w: se déplacer vers la gauche

## Options sur place
- i: lister ce qu'on possède
- p ou m ou f utiliser plan: regarder le plan interactif qui indique notre position
- >>> d ou é ou '
Vous êtes complètement à votre avantage sur la photo,
mais il n'y a personne ici à qui la montrer...
- >>> x: utiliser l'extincteur ?
Il n'y a pas le feu !
- aide ou ?: ouvre la fiche d'aide


# [Se connecter à chaque fois dans la SALLE DES SAUVEGARDES]
>>> utiliser terminal

[Entrer id "AdrienPanguel" et mdp "Didi!-03?/"]

Vous entendez un bruit électrique derrière vous.

La machine bizarre qui se trouve au milieu de la pièce est maintenant sous tension !

                                         Process complete --- shutdown                                          

Vous entendez la machine s'éteindre.

Vous vous demandez à quoi elle sert vraiment.  En attendant, quelque chose a l'air
légèrement différent, mais vous ne parvenez pas à mettre le doigt dessus.

[security engine - ERROR] corrupted configuration file
[security engine - INFO] enforcing DEFAULT security policy
[security engine - ERROR] corrupted event log
[security engine - INFO] starting event log recovery



# Historique de l'aventure

## Objets en notre possession

- une carte de l'université
- un plan
- un pied de biche
- un guide OpenSSL (tome I) : chaînes de caractères.
- un guide OpenSSL (tome II) : chiffrement symétrique.
- un guide OpenSSL (tome III) : génération d'une paire de clef.
- un guide OpenSSL (tome IV) : chiffrement à clef publique.
- un guide OpenSSL (tome V) : signature.
- un guide OpenSSL (tome VI) : script d'exemple.
- un extincteur

## Détail des guides:

### tome I : chaînes de caractères
Une chaine de caractère est une séquence de caractères.  La façon dont
ces caractères sont représentés par des séquences de bits est decrite
par un système d'encodage.  Il en existe de nombreux, et ils sont bien
sûr tous incompatibles entre eux.  Certains ne permettent pas de
représenter tous les caractères.  Par exemple, l'encodage ISO-8859-1
(a.k.a.  latin-1) code les caractères sur un octet.  Il est bien adapté
au monde occidental, mais ne contient pas les signes asiatiques, par
exemple.  Le KOI8-R, lui, permet de représenter les caractères
cyrilliques, etc.

Le système unicode permet de représenter la plupart des caractères connus,
mais il n'est pas très compact (4 octets par caractères).  Représenter des
chaines de caractères comme des séquences de caractères unicode offre
l'avantage de faire disparaître tous ces ennuyeux problèmes d'encodage. C'est
le choix des concepteurs de Python.  Dans ce langage, une chaine de
caractère (un objet de type "str") est représentée en mémoire dans le système
unicode.

Il existe aussi en python un autre type de chaine, les objets de type
"bytes".  Il s'agit d'une simple séquence d'octets, comparable aux
tableaux de type char qu'on a dans le langage C.

>>> type("toto")
<class 'str'>

>>> type(bytes([0, 1, 2]))
<class 'bytes'>

Tout ceci a deux conséquences.


A) Traitement du texte
----------------------

Les programmeurs doivent se soucier de ces problèmes d'encodage
lorsqu'ils doivent transformer des chaines de caractères en séquences
d'octets, par exemple pour les écrire dans un fichier, les envoyer sur
le réseau, ou les transmettre à un autre programme (comme openssl...).
Par défaut dans UGLIX, les chaines unicodes sont encodées en UTF-8
lors de leur conversion en séquences d'octets.

Les chaines unicodes ont une méthode "encode", qui prend en argument
un encodage (la valeur par défaut est "utf-8").

>>> 'toto'.encode()
b'toto'

>>> 'aïlle'.encode()
b'a\xc3\xaflle'

Quand ils sont affichés, les objets de type byte sont préfixés par la
lettre 'b'.  Ils possèdent, eux, une méthode "decode", qui prend
aussi en argument un encodage (utf8 par défaut).

>>> b'\xc3\xa0 V\xc3\xa4\xc3\xafn\xc3\xb6'.decode()
'à Väïnö'

Une situation où l'encodage apparaît explicitement concerne l'utilisation de
OpenSSL.  Il est nécessaire d'encoder les chaines de caractères unicode avant
de les envoyer à openssl (lors du chiffrement), et il est nécessaire de les
décoder en sortie de openssl (lors du déchiffrement) pour récupérer de
l'unicode.


B) Traitement des données binaires
----------------------------------

Il est parfois nécessaire d'envoyer ou de recevoir des requêtes
contenant des données binaires, qui ne sont pas interprétables comme
des chaines de caractères (il y a en effet des séquences d'octets qui
sont des encodages invalides en UTF-8, et qui sont donc rejetées lors
du décodage).  Par exemple :

>>> s = bytes([5*i*i & 0xff for i in range(10)])
>>> s.decode()
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb4 in position 6: invalid start byte

Dans ce cas-là, il faudrait transmettre des objets de type bytes().  Le
petit problème, c'est que les bytes() ne sont pas forcément affichables 
sur un terminal conçu principalement pour afficher des caractères ASCII.
Pour contourner cette difficulté, il faut encoder les bytes() en
quelque chose qui soit du texte acceptable, pour en faire une str().
Dans UGLIX, on utilise généralement à cette fin deux encodages : en base64
(les séquences d'octets sont découpées en paquets de 6 bits, et chaque
paquet est converti en une lettre) ou bien en hexadécimal.

Pour ceci, on fait appel aux fonctions b64encode et b64decode du
module base64.  Voici un exemple

>>> import base64
>>> base64.b64encode(s)
b'AAUULVB9tPVAlQ=='

Notez qu'on récupère des "bytes".  Mais ceux-là, on peut les convertir
en texte sans douleur.

>>> b'AAUULVB9tPVAlQ=='.decode()
'AAUULVB9tPVAlQ=='

Les objets de type "bytes" ont une méthode .hex() qui fait
ce que son nom indique :

>>> s.hex()
'0005142d507db4f54095'

De plus, on peut convertir la représentation hexadécimale en bytes()
avec la "méthode de classe" bytes.fromhex() :

>>> bytes.fromhex('deadbeef')
b'\xde\xad\xbe\xef'

### tome II : chiffrement symétrique
CHIFFREMENT SYMÉTRIQUE
======================

L'essentiel des tâches de chiffrement peut être réalisé avec la
bibliothèque OpenSSL (la version 1.0 est requise au minimum).

La plupart du temps, les utilisateurs d'UGLIX chiffrent leurs fichiers
avec un mécanisme à clef secrète et en utilisant un mot de passe.
OpenSSL se débrouille pour convertir ce mot de passe en une clef
secrète et un vecteur d'initialisation. De l'aléa est généralement
introduit dans ce processus.

Pour augmenter la portabilité, les utilisateurs d'UGLIX stockent
généralement les fichiers chiffrés en les encodant en base64.

Enfin, par défaut, les utilisateurs d'UGLIX sont invités à utiliser
l'AES-128 en mode CBC pour chiffrer leurs données.

Vous êtes invités à vous reporter à la documentation plus détaillée de
OpenSSL, en particulier en exécutant "man openssl", "openssl enc
help", ou bien en consultant la page du mode d'emploi de openssl
dédiée au chiffrement symétrique ("man openssl-enc").

Déchiffrer le fichier "foo" en utilisant le mot de passe "bar" peut
logiquement s'accomplir par la commande :

openssl enc -d -base64 -aes-128-cbc -pbkdf2 -pass pass:"bar" -in foo

Il est très pratique de pouvoir invoquer openssl depuis des programmes.
Pour cette raison, un autre script open-source est mis à la disposition
de la communauté. On le trouve dans le guide intitulé "script d'exemple".

Vous êtes invité à l'adapter à tous vos besoins.

    ⚠      Il existe plusieurs versions de OpenSSL. Ce serveur UGLIX utilise
   ⚠ ⚠     "OpenSSL 1.1.1d  10 Sep 2019". N'hésitez pas à vérifier avec la 
  ⚠ | ⚠    commande "openssl version". Il FAUT une version supérieure à 1.1.1 !
 ⚠  o  ⚠   Si vous avez la 1.1.0 (ou plus ancienne), l'option -pbkdf2 ne sera
⚠⚠⚠⚠⚠⚠⚠⚠⚠  pas reconnue.
    |      
    |      Attention, sur les versions récentes de MacOS, "openssl" est en fait
    |      LibreSSL (un fork). Et il est partiellement incompatible !


### tome III : génération d'une paire de clef
GÉNÉRATION D'UNE PAIRE DE CLEFS
===============================

Openssl permet de générer des paires de clefs, avec la commande : 

    openssl genpkey <options>

Encore une fois, vous êtes encouragés à consulter "man genpkey" et 
la documentation de openssl.  Par défaut, le résultat est envoyé sur
la sortie standard.  Le résultat contient la paire de clefs, au format
PEM (c'est de l'ASCII) propre à openssl et un peu pénible à décoder à
la main. 

Par exemple, pour générer une paire de clefs RSA de 1024 bits :

    openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:1024


Une commande permet d'extraire la clef publique uniquement, pour la
communiquer à des tiers : 

    openssl pkey -in <fichier contenant la clef secrète> -pubout

### tome IV : chiffrement à clef publique
CHIFFREMENT À CLEF PUBLIQUE
===========================

Openssl permet d'effectuer du chiffrement/déchiffrement asymétrique, avec
l'algorithme RSA.  Vous êtes invité à consulter la page de manuel
correspondante (man openssl-pkeyutl). 

L'usage d'openssl pour effectuer des opérations de (dé)chiffrement asymétrique
a deux limitations :

1) Le message clair DOIT être plus court que la clef.  Si ce n'est pas le cas,
   l'opération échoue avec un message "Public Key operation error, data too 
   large for key size".  Avec une clef de 2000 bits, vous avez droit à environ
   1800 bits de message.  C'est une limitation de l'algorithme lui-même.

2) Openssl ne prévoit pas d'encoder le résultat de l'opération de chiffrement
   en base64.  Par contre il y a une option pour l'encodage en... hexadécimal.

La commande essentielle pour le chiffrement :

   openssl pkeyutl -encrypt -hexdump -pubin -inkey <fichier contenant la clef publique>

Ceci attend un message sur l'entrée standard, et affichera son chiffrement sur
la sortie standard.  Pour déchiffrer, il faut fournir la clef secrète (et donc
retirer l'option  "-pubin")

### tome V : signature
SIGNATURES
==========

OpenSSL permet d'effectuer des signatures numériques et d'en vérifier avec
plusieurs algorithmes, dont RSA.
    
La solution la plus courante consiste à utiliser une fonction de hachage
cryptographique, et à signer l'empreinte du document à authentifier.  OpenSSL
peut accomplir ceci automatiquement avec la commande  "openssl dgst".  Vous
êtes invités à consulter la page de manuel correspondante
("man openssl-dgst").  Par défaut, avec une clef RSA, cela produit des
signatures PKCS#1 v1.5.  Voici les exemples les plus pertinents :
    

Production d'une signature
--------------------------

    openssl dgst -sha256 -sign secret_key.pem
    
Ceci attend les données à signer sur l'entrée standard, et envoie la
signature sur la sortie standard.  L'option -hex peut être utile.
    

Vérification d'une signature
----------------------------
    
    openssl dgst -sha256 -verify public_key.pem -signature signature.bin
    
Ceci attend sur l'entrée standard les données dont "signature.bin" contient
une signature.
    
Les signatures sont des données binaires, donc on doit généralement les
encoder, par exemple en hexadecimal avant de pouvoir les transmettre sans
douleur.  L'option -hex ne permet pas de vérifier des signatures données en
hexadécimal.


REMARQUE IMPORTANTE
-------------------
Une signature n'est valide que si les **mêmes** données (prétendument signées)
sont fournies lors de la production et de la vérification de la signature.  Or,
lorsque l'une des deux étapes sont effectuées par un serveur distant, on ne 
contrôle pas forcément les données en question.  Il faut savoir que la **majorité** 
des éditeurs de texte (vi, nano, gedit, kate, emacs, ...) ajoutent un caractère "\n" 
invisible à la fin de tous les fichiers.  Il est généralement impossible de 
l'empêcher, or ceci peut entrainer l'invalidité des signatures.  On peut vérifier
si c'est le cas en faisant passer le fichier à travers le programme "xxd".  Si on
voit apparaître un octet 0x0a à la fin, c'est le "\n" maudit.
    
Une solution potentielle pour écrire un fichier sans caractère excédentaire 
consiste à utiliser un petit programme du type :
>>> # cet exemple est en python
>>> f = open(FILENAME, "w")
>>> f.write("contenu important")   # <--- pas de \n à la fin
>>> f.close()

L'autre solution consiste à écrire une fonction qui invoque directement OpenSSL,
par exemple avec la fonction "subprocess.run()" de la librairie standard de python.

### tome VI : script d'exemple
import subprocess

# ce script suppose qu'il a affaire à OpenSSL v1.1.1
# vérifier avec "openssl version" en cas de doute.
# attention à MacOS, qui fournit à la place LibreSSL.

# en cas de problème, cette exception est déclenchée
class OpensslError(Exception):
    pass

# Il vaut mieux être conscient de la différence entre str() et bytes()

def encrypt(plaintext, passphrase, cipher='aes-128-cbc'):
    """invoke the OpenSSL library (though the openssl executable which must be
       present on your system) to encrypt content using a symmetric cipher.

       The passphrase is an str object (a unicode string)
       The plaintext is str() or bytes()
       The output is bytes()

       # encryption use
       >>> message = "texte avec caractères accentués"
       >>> c = encrypt(message, 'foobar')       
    """
    # prépare les arguments à envoyer à openssl
    pass_arg = 'pass:{}'.format(passphrase)
    args = ['openssl', 'enc', '-' + cipher, '-base64', '-pass', pass_arg, '-pbkdf2']
    
    # si plaintext est de stype str, on est obligé de l'encoder en bytes pour
    # pouvoir l'envoyer dans le pipeline vers openssl
    if isinstance(plaintext, str):
        plaintext = plaintext.encode('utf-8')
    
    # ouvre le pipeline vers openssl. envoie plaintext sur le stdin de openssl, récupère stdout et stderr
    #    affiche la commande invoquée
    #    print('debug : {0}'.format(' '.join(args)))
    result = subprocess.run(args, input=plaintext, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # si un message d'erreur est présent sur stderr, on arrête tout
    # attention, sur stderr on récupère des bytes(), donc on convertit
    error_message = result.stderr.decode()
    if error_message != '':
        raise OpensslError(error_message)

    # OK, openssl a envoyé le chiffré sur stdout, en base64.
    # On récupère des bytes, donc on en fait une chaine unicode
    return result.stdout.decode()

# TODO :
# - implement the decrypt() method
# - write a KeyPair class
# - write a PublicKey class
# - etc.



## Partie 1: S'enregistrer sur le registre des participants porur sauvegarder sa progression

Vous êtes dans un local poubelle.  Il fait tout noir. Il y a des néons au
plafond, mais ils sont éteints.  Seul un éclairage d'urgence de faible
intensité, au niveau du sol, éclaire un peu la pièce.  Le sol et les murs
sont couverts de carrelage, probablement pour faciliter le nettoyage. Une
porte équipée d'une barre anti-panique donne sur une autre pièce.

Ici se trouvent des déchets.
Ici se trouve un conteneur-poubelle.
Ici se trouve une inscription sur le sol.

>>> regarder déchets
Au moment où vous alliez attraper un sac poubelle, vous avez l'impression de
l'avoir vu bouger de lui-même.  Mieux vaut les laisser tranquilles, on ne sait jamais.

>>> regarder conteneur-poubelle
Un conteneur à déchet en plastique vert.  Un logo indique qu'il est fait de
plastique recyclable, ou recyclé, on ne sait pas.  Il est rempli de déchets.

>>> lire inscription sur le sol
On dirait qu'elle a été tracé avec le doigt, avec un liquide marron foncé, 
légèrement visqueux mais qui est complètement sec maintenant.  Elle dit :
      ASK FOR HELP




> n
Vous êtes dans une sorte d'atelier, assez haut de plafond.  Toujours pas
de fenêtre.  Malgré la faible intensité de l'éclairage d'urgence, vous
distinguez une espèce de grande trappe dans le plafond.  Elle est fermée.
Le mur ouest porte une inscription à moitié illisible à cause de l'obscurité :
        _     _   _     ___  _     __ __ ____         __ _  _ _ _ _        _  
   /    /  __/ ___|   __| |   | __  |    \        _   _| _ _ |          \ 
    _    |              |     |  _  | |_)    /     |   |   |     |        
 /  __    __  |_ _    __|    _|  ___   _ <  / _    | | | |     |_| |      
 _     _\ ___  _  |__ __ _    |___ _ _| \_\ _/   \_\_    _  _| __ /|    _\        // Je lis "accelerateur"

En dessous, il y a une porte blindée bardée de panneaux avec des pictogrammes
en forme d'éclair, de point d'exclamation, de tête de mort...  Et la mention : 
"portez un casque et des lunettes de protection".  Vous avisez aussi deux autres 
portes : une porte la mention "local poubelle" tandis que l'autre est surmontée 
d'une lampe qui indique une sortie de secours.

Ici se trouve un interrupteur sur le mur.
Ici se trouve une inscription sur la porte blindée.

>>> actionner interrupteur
vous actionnez l'interrupteur mais ça n'a aucun effet.  Panne de courant ?

>>> lire inscription
              5F1                                  Q3
             27   4                               9  1
            75 0                                     2
           8  8669 4                            87  6 2
         8    9 9  14                          046  4      1
       0   5 330  8   4                                35  2
      74 29   8 74 6 78                      41   5 3     80
     65   6       9 7  7                      0   6 59 65  3
       6  0 4    2509                      75     57     94 56
    3 0 2 38  8   44      5                  8   92  0  0  1444
   1  982 21   8  9   2   6              5 6 2 2   8 6159 6    6
     1  96   1    7 328                 781    1        833  3
  99  0     3 21   67  50                  37      03 50    7 3 75
     8 89  7 5   01 3  62                 72 8  7 9  27   9    83
     09 0 2   6 450               90       796 1  8       2 56
      92   5  7  23 186         3  5                      9       63
  12     20 0           5     1   4  699     1      754  4        51
                             9     0  8
                             1        856
                                4     2
                                4    7


                               3 1    4
                                8 4 0 8 8
                             0 4      8 54 5
                            37        231 922
                                0   3   9   7
                          0           0   8 7
                         20  7  643586  0 9  3
                           2           789
                          9 88  32 2    6  3   3
                      297 36674    4    1 30 9   2
                     49     5 1  76 39   2 28 1   4
                      4         3 609    5   48  68
                       8           43  1 4   192 7
                             78   8   10

Dans l'obscurité seules les grandes lignes sont reconnaissables, mais ça vous
suffit à appréhender le concept...                                                // C'est sûrement une tête de mort




>>> ouvrir porte blindée
Vous êtes dans une grande pièce complètement obscure.  Avec le peu de lumière qui 
vient de l'extérieur, vous distinguez un gros fatras de machines étranges.  
On dirait que des dispositifs expérimentaux de physique des particules ont 
été entassés ici depuis des générations.  Là-dedans, vous distinguez quand 
même quelques objets.  Il y a deux portes à l'est et à l'ouest surmontées de
lampes indiquant une sortie de secours. 

Ici se trouve un dispositif expérimental étrange au milieu de la pièce.
Ici se trouve un pied-de-biche.
Ici se trouve un terminal posé sur un bureau.

>>> regarder dispositif expérimental
Une sorte de machine pour des expériences de physique.  Il y a des fils, des
tubes, etc. qui convergent dans une sorte de globe métallique. C'est assez 
imposant.  Impossible de deviner à quoi ça peut bien servir.

>>> regarder pied-de-biche
Il est rouge et il a l'air assez solide.  Il vous rappelle "half-life", ce
jeu vidéo de 1998 où une expérience ratée avec un accélérateur de particules
téléportait à vos pied une horde de monstre depuis une autre dimension.
Il est fixé au mur, derrière une vitre. Il y a écrit : 
                          +-----------------------------------+
                          |  Brisez la vitre en cas d'urgence |
                          +-----------------------------------+

>>> prendre pied de biche
OK

>>> regarder terminal
On dirait un PC fixe des années 1990.  Il fait vraiment vintage.

>>> ouvrir terminal
ERROR: unknown username ``apanguel''     // C'est pour récupérer sa sauvegarde d'une autre partie





>>> w
Vous êtes dans un couloir orienté nord-sud.  Une porte donne sur une pièce
côté est.

Ici se trouve une inscription sur la porte.
>>> lire inscription
                                                         5 6           
                    57                                  6315             
                 7 9  0                                 3   991            
                79                                 68 9    8            
              32   8   8                         5  55   47              
         6 54  798   2 4                        3  6  5 2   8 0            
           7 5 0762  2 6 7                      53  0  4264   2 9           
            8  6774   7 2 5                       0 45 0 0 742 62            
               6  1    9                       1       74  63   28           
               03     1   2 2                399 5   4  94 7 7 8446           
     63        5         6   2              350   82   7   0       1           
          4 2   4439 87 18                        0 8  9     7 7  55                 
    60     7  5   6 2134  53 5              9  0   13   4  2  4429              
     9        16 9    8  3814               79           08 5 9                   
    1    4            6  8         5206      2 3  5  2   34 73 07 6  3       
   941   7 6  7 591 7 12  8    6       0 2      33        87   2 7             
    2 50 00  6   635 9  1      92 5  634 7     0 1  00   90 2     01                 
                                    5   394
                              81  14 60  20
                               595   3   4
                                 3   1  


                                 6     41   
                                3 3   853    
                               0   9 78 08  0 
                              05   4     453   
                               7      3 56   4  
                                  95    7 2  7 1 
                            0 5 67    95     6 0  
                           18411        6 368      
                         26 9 5    6986  75 90 67   
                         8 5  22  4  637  9 5 00  1  
                         369      1 3 727   63    38  
                      2   6     39         5     9 12 2
                          8 2        1   09573   6  
                             3  78  3 4  6  6      // C'est marrant, c'est la même inscription que toute à l'heure !





>>> n
Vous arrivez dans un petit couloir en forme d'arc de cercle, avec l'éclairage 
d'urgence.  Sur un mur, il y a une inscription à moitié effacée :
                                    _   
                               / |__  / 
                                 |  _   
                                   _ ) |
                               |_  _ _/   
Deux portes donnent au sud et à l'est.

Ici se trouve un ascenseur.

>>> utiliser ascenseur
ELEVATOR OFFLINE




>>> e
Vous êtes dans un couloir orienté est-ouest.  Les néons ne fonctionnent
toujours pas, mais avec l'éclairage de secours vous distinguez une porte 
entrouverte dans la pénombre.  Elle donne sur un local de service.




>>> e
Vous arrivez dans un petit couloir en forme d'arc de cercle, en béton nu, 
assez sale et poussiereux.  Il y a des traces d'infiltration d'eau sur les murs.  
Personne n'a dû venir ici depuis un bon moment.  L'éclairage normal est en 
rade, mais l'éclairage d'urgence fonctionne.  Il y a pas mal de portes qui 
donnent sur des locaux techniques (plomberie, climatisation, courants faibles, 
etc.) mais elles sont toutes verrouillées.  Trois portes donnent sur des galleries 
à l'ouest, au nord et au sud.

Ici se trouve un ascenseur.
Ici se trouve une tourelle de défense inactive (Mk 3).

>>> utiliser ascenseur
ELEVATOR OFFLINE

>>> inspecter tourelle
Une sorte de tourelle fixée au sol, manifestement équipé de cameras, d'un 
LiDAR et de divers autres capteurs.  Elle est surmontée d'une sorte de canon.
Un laser ?  Elle est passive et n'a pas l'air alimentée.  Vous ne savez pas
pourquoi mais ça vous fait penser à une scène dans Aliens, le deuxième opus
réalisé par James Cameron et sorti en 1986.

>>> prendre tourelle
Elle est bien trop lourde.





>>> s
Vous êtes dans un couloir très sombre, orienté nord-sud.  Sur un des murs 
vous distinguez une rangée de néon éteints, mais l'éclairage d'urgence au 
niveau du sol, lui, est opérationnel.  Au plafond, il y a des passages de 
cables, des conduits d'aérations, des canalisations, etc.  Quelques portes 
fermées à clef donnent on ne sait où.  Deux portes palières donnent sur les 
extrémités nord et sud du couloir.  Il y a aussi une porte marquée "trappe 
d'accès" au milieu du couloir (côté ouest).

Ici se trouve un plan interactif.

>>> inspecter plan
On dirait une sorte de tablette.  Elle montre une carte des environs.
L'emplacement où vous vous trouvez est indiqué en rouge.  Et en fait, 
pour "regarder" le plan, il faut l'UTILISER.  Et en fait, il semble 
que vous puissiez l'emporter avec vous.  Qui sait, ça pourra peut-être
rendre service ailleurs et plus tard ?

>>> utiliser plan
                          local de service 3            |     // Le plan ne semble pas être entier, la partie nord manque
                                  |                     |
            XYY ---------------- XXY ----------------- ZYX 
             |                                          |
             |     +------------------+                 |
             |     |                  |                 |
             |     |                  |                 |
            ZXY ---|      ??????      |---- trappe --- XXZ 
             |     |                  |       |         |
             |     |                  |    poubelle     |
             |     +------------------+                 |
             |                                          |
            ZZX ---------------- ZYZ ----------------- XZZ 
             |                    
             |      
             |      
             |      
            YYZ     
             |                                          
             |                                          
             |                                          
             |     
            YZZ  ----------------- YXZ --------------- XYZ 
             |                      |                   |
             |              local de service 5          |
             |                                          |
             |                                          |
     ??? .. ZXZ                                        XZX 
             |                                          | 
             |                                          |
             |                                          |
             |                                          |
 réserve -- XZY                                        XXX -- local électrique 

>>> prendre plan
OK

>>> o
Vous brandissez le pied-de-biche devant vous dans une attitude de défi.     // Peut-être que "o" fait utiliser le pied-de-biche ?
Mais rien ne se passe...





>>> w
Vous êtes dans une sorte d'atelier, assez haut de plafond.  Toujours pas     // Retour à une pièce précédente
de fenêtre.  Malgré la faible intensité de l'éclairage d'urgence, vous
distinguez une espèce de grande trappe dans le plafond.  Elle est fermée.
Le mur ouest porte une inscription à moitié illisible à cause de l'obscurité :
        _     _   _     ___  _     __ __ ____         __ _  _ _ _ _        _  
   /    /  __/ ___|   __| |   | __  |    \        _   _| _ _ |          \ 
    _    |              |     |  _  | |_)    /     |   |   |     |        
 /  __    __  |_ _    __|    _|  ___   _ <  / _    | | | |     |_| |      
 _     _\ ___  _  |__ __ _    |___ _ _| \_\ _/   \_\_    _  _| __ /|    _\

En dessous, il y a une porte blindée bardée de panneaux avec des pictogrammes
en forme d'éclair, de point d'exclamation, de tête de mort...  Et la mention : 
"portez un casque et des lunettes de protection".  Vous avisez aussi deux autres 
portes : une porte la mention "local poubelle" tandis que l'autre est surmontée 
d'une lampe qui indique une sortie de secours.

Ici se trouve un interrupteur sur le mur.
Ici se trouve une inscription sur la porte blindée.




>>> e
Vous êtes dans un couloir très sombre, orienté nord-sud.  Sur un des murs    // Revenons à la pièce précédente, sans faire une boucle
vous distinguez une rangée de néon éteints, mais l'éclairage d'urgence au 
niveau du sol, lui, est opérationnel.  Au plafond, il y a des passages de 
cables, des conduits d'aérations, des canalisations, etc.  Quelques portes 
fermées à clef donnent on ne sait où.  Deux portes palières donnent sur les 
extrémités nord et sud du couloir.  Il y a aussi une porte marquée "trappe 
d'accès" au milieu du couloir (côté ouest).





>>> n
Vous arrivez dans un petit couloir en forme d'arc de cercle, en béton nu,    // Revenons à la pièce précédente, explorons le nord
assez sale et poussiereux.  Il y a des traces d'infiltration d'eau sur les murs.  
Personne n'a dû venir ici depuis un bon moment.  L'éclairage normal est en 
rade, mais l'éclairage d'urgence fonctionne.  Il y a pas mal de portes qui 
donnent sur des locaux techniques (plomberie, climatisation, courants faibles, 
etc.) mais elles sont toutes verrouillées.  Trois portes donnent sur des galleries 
à l'ouest, au nord et au sud.

Ici se trouve un ascenseur.
Ici se trouve une tourelle de défense inactive (Mk 3).





>>> n
Vous êtes dans un couloir assez obscur, orienté nord-sud.

Ici se trouve une inscription sur le mur.

>>> lire inscription
On dirait qu'elle a été tracé avec le doigt, avec un liquide marron foncé, 
légèrement visqueux mais qui est complètement sec maintenant.  Elle dit :

      DO NOT ACTIVATE THE                                                   // Peut-être "DO NOT ACTIVATE THE LEVER !!!" ?

La dernière phrase est manifestement incomplète.




>>> n
Vous arrivez dans une pièce en forme d'arc de cercle, avec l'éclairage 
d'urgence.  Du texte est peint sur un mur, mais l'inscription est en 
partie effacée :
                              _ __    _   
                                _ \ __  \ 
                               _         |
                                __/ /  _/ 
                             |  _ _| __ _|
Une porte donne sur une gallerie vers le sud.  Une autre porte
est marquée ``DSI DATACENTER 0'' (vers l'est).

Ici se trouve un ascenseur.

>>> utiliser ascenseur
ELEVATOR OFFLINE





>>> e
Vous arrivez dans ce qui est manifestement une salle serveur.  Tout est éteint
et silencieux.  Il y a de l'éclairage de secours et vous distinguez des dizaines
de racks.  Ils ont un système de fermeture donc vous ne pouvez pas accéder aux 
serveurs qu'ils contiennent.  L'un d'entre eux attire particulièrement votre 
attention.  Il y a aussi un bureau dans un coin.

Ici se trouve un rack plus blindé que les autres.
Ici se trouve une inscription sur le mur.
Ici se trouve un terminal d'administration système.
Ici se trouve un clavier.
Ici se trouve un mode d'emploi.

>>> inspecter rack
il porte la mention ``SECURITY ENGINE''.  Il a effectivement l'air... sécurisé.

>>> déchiffrer rack
Mis à part donner un coup de pied dedans, il n'y a rien à faire.  Vu le blindage, 
le risque de fracture n'est pas complètement négligeable.  Vous laissez tomber.

>>> lire inscription
On dirait qu'elle a été tracé avec le doigt, avec un liquide marron foncé, 
légèrement visqueux mais qui est complètement sec maintenant.  Elle dit :
    
      POST-IT PASSWORD: ISECR0XX                                                 // PASSWORD = "ISECR0XX" (c'est un "zéro")

>>> utiliser terminal

                                                                UGLIX v4.0 beta
                                                                SYSTEM STARTING... 

                    ERROR
                    - Corrupted system data structure
                    - Backup user directory unreachable

                                                                RECOVERY... 
                    FAILURE
                    - Recovery data not found

                                                                COLD START... 
                    Enter machine password:     ********                           // J'ai essayé "ISECR0XX" mais ce n'est pas le bon

                    ERROR
                     - Incorrect machine password

                                                                SYSTEM SHUTDOWN --- press any key

>>> inspecter clavier
Un bon vieux modèle 104 touches, AZERTY.  Conçu pour durer il y a 45 ans.
Sans surprise, il y a un post-it en dessous.  Il indique:
U2FsdGVkX1/oM6I8s/PNGYMdvL4xyivWpGpDOv+m8u/hi0N9Qr5fdYR1PsnX7jQG    // Ce ciphertext change à chaque début de nouvelle partie !!!

>>> utiliser clavier
C'est peut-être le terminal qui lui est relié que vous voulez utiliser ?

>>> inspecter mode d'emploi
C'est le guide d'utilisation du terminal d'administration système qui est      // Sur le post-it est écrit le mot de passe chiffré
juste à côté.  Il fait 700 pages, donc vous sautez directement au chapitre 
``Mise en route''.  En gros, il suffit d'appuyer sur le bouton et de se 
laisser guide par l'interface utilisateur ultra-intuitive.  Les administrateurs
sont néanmoins mis en garde face aux risques encourus et ils doivent avoir été
soigneusement formés à l'utilisation des mécanismes de sécurité.  Pour éviter
les risques, un mot de passe est demandé au boot.  Les bonnes pratiques de
gestion des mots de passe sont rappelées : ne pas les mettre sur un post-it
sous le clavier, etc.  En désespoir de cause, il est recommandé de chiffrer
les mots de passe sur les post-it sous les clavier.  Ce serait mieux que rien.

>>> conseil post-it
Il n'y a pas de POST-IT
Essayez de vous connecter au terminal.  N'oubliez pas de regarder
le mode d'emploi, de lire l'inscription au mur et de jeter un coup
d'oeil sous le clavier...  Sachez enfin qu'il y a de la documentation
dans une autre pièce qui se trouve globalement au sud-ouest.




>>> w     // Retournons à la pièce du parchemin trouvé
>>> s
>>> s
>>> s
Vous êtes dans un couloir très sombre, orienté nord-sud.  Sur un des murs 
vous distinguez une rangée de néon éteints, mais l'éclairage d'urgence au 
niveau du sol, lui, est opérationnel.  Au plafond, il y a des passages de 
cables, des conduits d'aérations, des canalisations, etc.  Quelques portes 
fermées à clef donnent on ne sait où.  Deux portes palières donnent sur les 
extrémités nord et sud du couloir.  Il y a aussi une porte marquée "trappe 
d'accès" au milieu du couloir (côté ouest).




>>> s
Vous arrivez dans un petit couloir en forme d'arc de cercle, avec l'éclairage 
d'urgence.  Sur un mur il y a écrit :
                                _   _  _   
                             |_ _  |    |  
                               __) | |  |_ 
                                _ / __   _ 
                             |_ ___|          

Deux portes donnent sur les couloirs au nord et à l'ouest.

Ici se trouve un ascenseur.

>>> utiliser ascenseur
ELEVATOR OFFLINE




>>> w
Vous êtes dans un couloir orienté est-ouest.

Ici se trouve une tourelle de défense inactive (Mk 2).

>>> inspecter tourelle
Une sorte de tourelle statique, manifestement équipé de cameras, d'un LiDAR 
et de divers autres capteurs.  Elle est surmontée d'une sorte de lance-roquette.
Elle est passive et n'a pas l'air alimentée.  Des petits rigolos ont fait des
graphitis dessus : "ELITE BOT", "BORN KILLER", etc.




>>> w
Vous arrivez dans une pièce en forme d'arc de cercle (270°), avec l'éclairage 
d'urgence.  Trois portes donnent sur les couloirs vers l'est, le nord et le sud.

Ici se trouve un ascenseur.

>>> utiliser ascenseur
ELEVATOR OFFLINE





>>> n
Vous êtes dans un couloir orienté nord-sud.  Une porte donne sur une pièce     // Pièce déjà visitée
côté est.





>>> s
Vous arrivez dans une pièce en forme d'arc de cercle (270°), avec l'éclairage     // Retournons à la pièce précédente
d'urgence.  Trois portes donnent sur les couloirs vers l'est, le nord et le sud.  // Allons vers le sud

Ici se trouve un ascenseur.




>>> s
Vous êtes dans un couloir orienté nord-sud.  C'est presque le noir complet.  

Ici se trouve une tourelle de défense inactive (Mk 1).

>>> inspecter tourelle
Une sorte de tourelle statique, manifestement équipé de cameras, d'un LiDAR 
et de divers autres capteurs.  Elle est surmontée d'une sorte de mitrailleuse.
Elle est passive et n'a pas l'air alimentée.  Il y a des graphitis sur la
tôle blindée : "CLEANING CREW", "LÉON", "PRAY", etc.





>>> s
Vous arrivez dans un petit couloir en forme d'arc de cercle, avec l'éclairage 
d'urgence.  Un mur porte l'inscription :
                                _ _     
                               / |    | 
                                      \ 
                               |  _ _  |
                                _|___   
Trois portes conduisent au nord, au sud et à l'est.     // On va continnuer vers le sud

Ici se trouve un ascenseur.
Ici se trouve une baie vitrée.

>>> utiliser ascenseur
ELEVATOR OFFLINE

>>> regarder baie vitrée
Une baie vitrée qui vous sépare d'une autre partie du bâtiment.  Derrière vous 
ne distinguez absolument rien.  Il n'y a aucun éclairage.

>>> casser baie vitrée
vous essayer de griffer la surface avec vos ongles.  Mis à part faire
un bruit désagréable, ça n'a aucun effet.




>>> s
Vous êtes dans un couloir plongé dans l'obscurité, orienté nord-sud.  L'éclairage 
d'urgence ne fonctionne qu'à moitié, donc vous n'y voyez rien du tout.

Ici se trouve un tag sur le mur.

>>> inspecter tag
Malgré l'obscurité, vous parvenez à distinguer la peinture rouge à moitié
effacée :                                                  _ 
     |      _    _ __ | |  _   _          __ _   __     |  
       |/ _ \ \ /     \ |         '_          | '_ \ /    |
          __     /  _ / | |  _    |_) |             | ( |  
     |_  __ |   / \___          | .__    \_  _ _  |_| __  |
                                |_                         
         ___ __   __  _   _ _  __                         
      |  _ _        _| |   |    _    | _   _  _   _ |   __
        |_   | |    _    |     |     '_ \ /        _  |   
      |  _   | | | |       |   |     |_) | (_|     _    < 
      |_    |___  __ |_   _  |_     _ _   \_  _|\   |_  _ 





>>> s
Vous arrivez dans un petit couloir en forme d'arc de cercle, avec l'éclairage 
d'urgence.  Une porte fermée à clef porte un symbole ``livre'' ainsi qu'un panneau 
``accès réservé au personnel''.  Une autre porte, qui elle n'est pas fermée 
indique ``réserve''.  Enfin, une porte est marquée ``gallerie nord''.

Ici se trouve un ascenseur.

>>> utiliser ascenseur
ELEVATOR OFFLINE

>>> pied-de-biche
Vous essayez de forcer la porte de l'ascenseur avec le pied-de-biche, mais vous
n'arrivez à rien, la résistance du métal est trop importante.
Vous brandissez le pied-de-biche devant vous dans une attitude de défi.
Mais rien ne se passe...





>>> réserve
Vous arrivez dans une pièce pleine de livres rangés sur des étagères.  Il fait
vraiment sombre, et vous ne parvenez pas à distinguer les titres des ouvrages,
sauf les quelques-un qui sont juste à côté de l'éclairage "sortie de secours" 
près de la porte.

Ici se trouve un guide OpenSSL (tome I) : chaînes de caractères.
Ici se trouve un guide OpenSSL (tome II) : chiffrement symétrique.
Ici se trouve un guide OpenSSL (tome III) : génération d'une paire de clef.
Ici se trouve un guide OpenSSL (tome IV) : chiffrement à clef publique.
Ici se trouve un guide OpenSSL (tome V) : signature.
Ici se trouve un guide OpenSSL (tome VI) : script d'exemple.

>>> prendre chaînes de caractères
OK

>>> prendre chiffrement symétrique
OK

>>> prendre génération d'une paire de clefs
OK

>>> prendre chiffrement à clef publique
OK

>>> prendre signature
OK

>>> prendre script d'exemple
OK

>>> prendre chiffrement a clef publique
Il est déjà en votre possession.





>>> e     // Retournons à la salle des serveurs
>>> n
>>> n
>>> n
>>> n
>>> n
>>> n
>>> e
>>> e
>>> n
>>> n
>>> e
Vous arrivez dans ce qui est manifestement une salle serveur.  Tout est éteint
et silencieux.  Il y a de l'éclairage de secours et vous distinguez des dizaines
de racks.  Ils ont un système de fermeture donc vous ne pouvez pas accéder aux 
serveurs qu'ils contiennent.  L'un d'entre eux attire particulièrement votre 
attention.  Il y a aussi un bureau dans un coin.

Ici se trouve un rack plus blindé que les autres.
Ici se trouve une inscription sur le mur.
Ici se trouve un terminal d'administration système.
Ici se trouve un clavier.
Ici se trouve un mode d'emploi.





[COMMANDES SUR MON PROPRE TERMINAL]
- Lancer le code tests_encrypt_decrypt.py pour décrypter le ciphertext trouvé sur le post-it avec la commande:
python3 tests_encrypt_decrypt.py
- Voici le retour:
'U2FsdGVkX1/oM6I8s/PNGYMdvL4xyivWpGpDOv+m8u/hi0N9Qr5fdYR1PsnX7jQG'
64
Decrypted plaintext:
breve falls ovate disks bwana     // Ceci est le plaintext associé au ciphertext du post-it
                                  // Il est à entrer dans le terminal de la salle des serveurs





>>> utiliser terminal




                                                                UGLIX v4.0 beta
                                                                SYSTEM STARTING... 

                    ERROR
                    - Corrupted system data structure
                    - Backup user directory unreachable

                                                                RECOVERY... 
                    FAILURE
                    - Recovery data not found

                                                                COLD START... 
                    Enter machine password:     *****************************        



                    - Creating new administrator user account
                    Choose username:            AdrienPanguel                    
                    Choose password:            *********                        
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

[TAPPER "1" dans le terminal ouvert]

>>> utiliser terminal
[security engine] register:52:1|b644c1e209b41a83e9ed72be2f7878f8eb9c34fde9a06f0e9701f5448840e16a  // PREMIER FLAG !!!
>>> 
[security engine - ERROR] corrupted configuration file
[security engine - INFO] enforcing DEFAULT security policy

>>> utiliser terminal
Il ne redémarre plus.





# Partie 2: Rétablir le courant (électricité) [A partir de la SALLE DES SAUVEGARDES]
>>> conseil
Vous ne trouvez pas qu'il fait sombre ?  Essayez de remettre le courant.
Vous devrez aller au sud-est.





>>> w
Vous êtes dans un couloir orienté nord-sud.  Une porte donne sur une pièce
côté est.

Ici se trouve une inscription sur la porte.





>>> s
Vous arrivez dans une pièce en forme d'arc de cercle (270°), avec l'éclairage 
d'urgence.  Trois portes donnent sur les couloirs vers l'est, le nord et le sud.

Ici se trouve un ascenseur.





>>> s
Vous êtes dans un couloir orienté nord-sud.  C'est presque le noir complet.  

Ici se trouve une tourelle de défense inactive (Mk 1).





>>> s
Vous arrivez dans un petit couloir en forme d'arc de cercle, avec l'éclairage 
d'urgence.  Un mur porte l'inscription :
                                _ _     
                               / |    | 
                                      \ 
                               |  _ _  |
                                _|___   
Trois portes conduisent au nord, au sud et à l'est.

Ici se trouve un ascenseur.
Ici se trouve une baie vitrée.





>>> e
Vous êtes dans un couloir orienté est-ouest.  Sur le côté, une porte est 
entrouverte.  Elle donne sur un local de service.

Ici se trouve un extincteur.

>>> prendre extincteur
OK





>>> s
Vous arrivez dans un local exigu, tout noir.  C'est sûrement un vestiaire, en
tout cas il y a des casiers pour le personnel.

Ici se trouve un terminal de service.

>>> ouvrir terminal

                                                                   UGLIX v4.0 beta                                                                   
                                                                 (Service terminal)                                                                  

                    Active user: AdrienPanguel

                                                                      Main menu                                                                      
                                                                      ---------                                                                      



                    1. Manage ID card
                    2. Public Key Infrastructure
                    3. Locksmith Tools
                    4. Exit

>>> n     // Retournons à la salle précédente
>>> e
Vous arrivez dans un petit couloir en forme d'arc de cercle, avec l'éclairage 
d'urgence.  Il y a deux portes qui conduisent au sud et à l'ouest.

Ici se trouve un ascenseur.

>>> utiliser ascenseur
ELEVATOR ONLINE, POWER DOWN





>>> s
Vous êtes dans un couloir orienté nord-sud.

Ici se trouve un tag sur le mur.

>>> lire tag
La peinture rouge est à moitié effacée :
  _        _      _  _ _ _               __    _____                           
  |  |       \     _    __            |     \    _ _|                         
          _        _                  |                            _     _    
  |        __   |              /        |         |       |    _      |     _|
| |  |           __| | | \       _      |_ |   |_ _   |         )       |     
 \  __  _         _    |      _      _ _  _  | __      \ _  |  __    _, | |   
                                                          /                   
                                                        _ _      __ _                                      
 /  (_)                                     
| |_      _   _  _  __      _ _  _      ___ 
|   | | '_   '_   _ \   /\   / _  |        \
  | |      |       | \ V  V /         |  __ 
 _   _|_|    | | |    \_/ _   _  _|    \ __|





>>> s
Vous arrivez dans un petit couloir en forme d'arc de cercle, avec l'éclairage 
d'urgence.  Il y a une inscription à moitié effacée sur le mur :
                              _  _    _   
                              ___     /_  
                               __    '_ \ 
                              / _ /   _   
                             | _  _  ___  
Une porte indique ``local courants forts''.

Ici se trouve un ascenseur.

>>> utiliser ascenseur
ELEVATOR ONLINE, POWER DOWN





>>> e
Vous arrivez dans une pièce plongée dans l'obscurité, avec un peu d'éclairage
de secours.  Vous devinez la présence d'un transformateur électrique de la taille
d'une voiture, sur lequel arrivent de gros cables.  Il y a aussi des armoires 
électriques.  Des autocollants fluorescents ``éclair'' et ``tête de mort''
sont visibles malgré l'obscurité.

Ici se trouve un terminal de contrôle.

>>> utiliser terminal

                                                                   UGLIX v4.0 beta                                                                   
                                                             (Power Controller terminal)                                                             

                    Active user: AdrienPanguel
                                                                    Power status                                                                     
                                                                    ------------                                                                     
                    Power grid           : ONLINE
                    Auxiliary power      : ONLINE
                    Backup generator     : READY
                    Batteries            : FULLY CHARGED

                    Main circuit breaker : OPEN
                    Transformer output   : 0V


                                                                        Menu                                                                         
                                                                        ----                                                                         
                    1. CLOSE main breaker 
                    2. Exit

[Si j'entre "2"]
La pièce est toujours sombre et silencieuse.

[Si j'entre "1"]

                    Le terminal affiche :



                    Le terminal affiche :

                                                                  !!!  WARNING  !!!
                                                  Risk of injury due to insufficient qualification!
                                       Improper use can result in serious personal injury or property damage.
                                       All electric installation and commissioning work as well as repair work
                                   and disassembly have to be carried out by qualified staff (IEC 364 respectively
                                  CENELEC HD384 or DIN VDE0100 and IEC664 or DIN VDE0110 and national safety rules)

                                                       R E A D Y    T O    P R O C E E D ?

                                                             A R E    Y O U    S U R E ?

                                                      R E A L L Y,     R E A L L Y    S U R E ?

                                               Well, just in case, in order to ensure auditability of
                                          electrical operations, you need to perform a digital signature.
     
                                    +--------------------------------------------------------------------------+
                                    | You have no public-key. Upload a public-key on a service terminal first. |
                                    +--------------------------------------------------------------------------+

Le terminal s'est éteint en vous traitant de débutant.





                                                      















