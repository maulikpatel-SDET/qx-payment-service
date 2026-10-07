"""CR-11  Key size comes from a constant defined in ANOTHER repo (value 1024)."""
from cryptography.hazmat.primitives.asymmetric import rsa
from qx_crypto.constants import DEFAULT_KEY_SIZE


def make_session_key():
    return rsa.generate_private_key(public_exponent=65537, key_size=DEFAULT_KEY_SIZE)
