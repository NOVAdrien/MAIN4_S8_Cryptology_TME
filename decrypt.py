# decrypt.py
import subprocess

# en cas de problème, cette exception est déclenchée
class OpensslError(Exception):
    pass

# Il vaut mieux être conscient de la différence entre str() et bytes()

def decrypt(ciphertext, passphrase, cipher='aes-128-cbc', decode_utf8=True):
    """invoke the OpenSSL library (through the openssl executable which must be
       present on your system) to decrypt content using a symmetric cipher.

       - passphrase: str (unicode)
       - ciphertext: str or bytes (base64 text produced by encrypt())
       - output: str by default (decode_utf8=True), otherwise bytes

       # decryption use
       >>> message = "texte avec caractères accentués"
       >>> c = encrypt(message, 'foobar')
       >>> p = decrypt(c, 'foobar')
    """
    # prépare les arguments à envoyer à openssl
    # -d : déchiffrement
    # -base64 : l'entrée est en base64
    # -pbkdf2 : même dérivation de clé/IV que dans encrypt()
    # -A : base64 "sur une ligne" (plus robuste si le base64 n'a pas de retours)
    pass_arg = 'pass:{}'.format(passphrase)
    args = [
        'openssl', 'enc',
        '-d', '-' + cipher,
        '-base64',
        '-pass', pass_arg,
        '-pbkdf2',
        '-A'
    ]

    # si ciphertext est de type str, on est obligé de l'encoder en bytes pour
    # pouvoir l'envoyer dans le pipeline vers openssl
    if isinstance(ciphertext, str):
        ciphertext = ciphertext.encode('utf-8')

    # ouvre le pipeline vers openssl. envoie ciphertext sur le stdin de openssl, récupère stdout et stderr
    #    affiche la commande invoquée
    #    print('debug : {0}'.format(' '.join(args)))
    result = subprocess.run(args, input=ciphertext, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # gestion robuste des erreurs : on utilise le code de retour
    if result.returncode != 0:
        # attention, sur stderr on récupère des bytes(), donc on convertit
        err = result.stderr.decode('utf-8', errors='replace').strip()
        if err == '':
            err = 'OpenSSL failed but did not provide an error message.'
        raise OpensslError(err)

    # OK, openssl a envoyé le clair sur stdout (bytes)
    plaintext_bytes = result.stdout

    # Par défaut on suppose que le clair est du texte UTF-8 (cas classique avec encrypt() ci-dessus)
    if decode_utf8:
        return plaintext_bytes.decode('utf-8')

    # Sinon, on renvoie les bytes bruts
    return plaintext_bytes
