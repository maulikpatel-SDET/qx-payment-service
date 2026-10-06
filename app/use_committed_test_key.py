"""CR-09  Loads the private key file that is COMMITTED in qx-key-service."""
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec

from app.key_paths import TEST_EC_KEY


def sign_test(data: bytes) -> bytes:
    with open(TEST_EC_KEY, "rb") as fh:
        key = serialization.load_pem_private_key(fh.read(), password=None)
    return key.sign(data, ec.ECDSA(hashes.SHA256()))
