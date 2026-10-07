"""CR-01  Uses the RSA key GENERATED in qx-key-service.

No "RSA" word in this file. The key type is only known from the key file
that qx-key-service/keygen/generate_rsa_key.py created.
"""
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

from app.key_paths import RSA_SIGNING_KEY


def sign_invoice(invoice: bytes) -> bytes:
    with open(RSA_SIGNING_KEY, "rb") as fh:
        key = serialization.load_pem_private_key(fh.read(), password=None)
    return key.sign(invoice, padding.PSS(mgf=padding.MGF1(hashes.SHA256()),
                                         salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())
