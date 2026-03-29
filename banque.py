import json
import binascii
from datetime import datetime, timezone

from cryptography import x509
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec, rsa, ed25519, padding
from cryptography.x509.oid import NameOID
from cryptography.x509.oid import NameOID, ExtensionOID

def load_cert(pem: str):
    return x509.load_pem_x509_certificate(pem.encode())


def subject_cn(cert):
    attrs = cert.subject.get_attributes_for_oid(NameOID.COMMON_NAME)
    return attrs[0].value if attrs else None


def verify_cert_signature(child, issuer):
    pub = issuer.public_key()

    if isinstance(pub, rsa.RSAPublicKey):
        pub.verify(
            child.signature,
            child.tbs_certificate_bytes,
            padding.PKCS1v15(),
            child.signature_hash_algorithm,
        )
    elif isinstance(pub, ec.EllipticCurvePublicKey):
        pub.verify(
            child.signature,
            child.tbs_certificate_bytes,
            ec.ECDSA(child.signature_hash_algorithm),
        )
    elif isinstance(pub, ed25519.Ed25519PublicKey):
        pub.verify(
            child.signature,
            child.tbs_certificate_bytes,
        )
    else:
        raise Exception(f"Type de clé émetteur non supporté: {type(pub)}")

def verify_tx_signature(card_cert, data_str, sig_hex):
    pub = card_cert.public_key()
    sig = binascii.unhexlify(sig_hex)

    if isinstance(pub, ec.EllipticCurvePublicKey):
        pub.verify(sig, data_str.encode(), ec.ECDSA(hashes.SHA256()))
    elif isinstance(pub, rsa.RSAPublicKey):
        pub.verify(sig, data_str.encode(), padding.PKCS1v15(), hashes.SHA256())
    elif isinstance(pub, ed25519.Ed25519PublicKey):
        pub.verify(sig, data_str.encode())
    else:
        raise Exception(f"Type de clé carte non supporté: {type(pub)}")


def is_time_valid(cert):
    now = datetime.now(timezone.utc)
    return cert.not_valid_before_utc <= now <= cert.not_valid_after_utc


def verify_transaction(tx, ca_cert):
    try:
        data_str = tx["data"]
        data = json.loads(data_str)

        card = tx["card"]
        bank = card["bank"]

        card_cert = load_cert(card["certificate"])
        bank_cert = load_cert(bank["certificate"])

        # cohérence data <-> objets externes
        if data["card-number"] != card["number"]:
            return False
        if data["bank-name"] != bank["name"]:
            return False

        # cohérence CN
        if subject_cn(card_cert) != card["number"]:
            return False
        if subject_cn(bank_cert) != bank["name"]:
            return False

        # dates
        if not is_time_valid(card_cert):
            return False
        if not is_time_valid(bank_cert):
            return False
        if not is_time_valid(ca_cert):
            return False

        # chaîne de certificats
        verify_cert_signature(bank_cert, ca_cert)
        # la banque doit être autorisée à signer d'autres certificats
        bc = bank_cert.extensions.get_extension_for_oid(
            ExtensionOID.BASIC_CONSTRAINTS
        ).value
        if not bc.ca:
            return False
        verify_cert_signature(card_cert, bank_cert)

        # signature transaction
        verify_tx_signature(card_cert, data_str, tx["signature"])

        return True

    except (InvalidSignature, ValueError, KeyError, TypeError):
        return False
    except Exception:
        return False


def main():
    with open("./JavaScriptObjectNotation/mon_batch.json", "r", encoding="utf-8") as f:
        obj = json.load(f)

    with open("./Certificates/certificate_banque.csr.pem", "rb") as f:
        ca_cert = x509.load_pem_x509_certificate(f.read())

    batch = obj["batch"]
    results = [verify_transaction(tx, ca_cert) for tx in batch["transactions"]]

    print("identifier =", batch["identifier"])
    print(results)
    print(json.dumps(results))


if __name__ == "__main__":
    main()