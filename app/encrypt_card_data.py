"""R3-06 ENCRYPT side: payment-service encrypts card data with the public key published by qx-key-service."""
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

from app.key_paths import KEY_SERVICE_DIR

ENCRYPTION_PUBLIC_KEY = f"{KEY_SERVICE_DIR}/keys/rsa_encryption_public.pem"


def encrypt_card(pan: bytes) -> bytes:
    with open(ENCRYPTION_PUBLIC_KEY, "rb") as fh:
        pub = serialization.load_pem_public_key(fh.read())
    return pub.encrypt(pan, padding.OAEP(mgf=padding.MGF1(hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
