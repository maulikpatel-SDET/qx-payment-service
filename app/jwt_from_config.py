"""CR-06  Algorithm name comes from qx-infra-config (signing.yaml -> env var SIGNING_ALG = ES256)."""
import os

import jwt
from cryptography.hazmat.primitives import serialization

from app.key_paths import EC_SIGNING_KEY

SIGNING_ALG = os.environ["SIGNING_ALG"]


def issue_token(claims: dict) -> str:
    with open(EC_SIGNING_KEY, "rb") as fh:
        key = serialization.load_pem_private_key(fh.read(), password=None)
    return jwt.encode(claims, key, algorithm=SIGNING_ALG)
