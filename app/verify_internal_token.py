"""R3-03 VERIFY side: HS256 token from qx-key-service, secret from qx-infra-config."""
import os

import jwt


def verify_internal_token(token: str) -> dict:
    return jwt.decode(token, os.environ["JWT_HMAC_SECRET"], algorithms=[os.environ.get("JWT_HMAC_ALG", "HS256")])
