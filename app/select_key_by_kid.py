"""R3-08 CONSUMER of rotation: picks the verification key by kid from qx-key-service's rotation manifest."""
import json

import jwt
from cryptography.hazmat.primitives import serialization

from app.key_paths import KEY_SERVICE_DIR


def verify_with_rotated_key(token: str) -> dict:
    kid = jwt.get_unverified_header(token)["kid"]
    with open(f"{KEY_SERVICE_DIR}/keys/rotation_manifest.json") as fh:
        entry = next(k for k in json.load(fh)["keys"] if k["kid"] == kid)
    with open(f"{KEY_SERVICE_DIR}/keys/{entry['file']}", "rb") as fh:
        pub = serialization.load_pem_public_key(fh.read())
    return jwt.decode(token, pub, algorithms=[entry["alg"]])
