"""CR-12  Second consumer of the SAME RSA key from qx-key-service (verify side)."""
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

from app.key_paths import RSA_PUBLIC_KEY


def verify_receipt(receipt: bytes, signature: bytes) -> bool:
    with open(RSA_PUBLIC_KEY, "rb") as fh:
        pub = serialization.load_pem_public_key(fh.read())
    pub.verify(signature, receipt, padding.PSS(mgf=padding.MGF1(hashes.SHA256()),
                                                salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())
    return True
