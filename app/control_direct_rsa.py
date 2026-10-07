"""CR-13  CONTROL - RSA generated and used in the SAME repo. Must be flagged."""
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa

key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
sig = key.sign(b"control", padding.PKCS1v15(), hashes.SHA256())
