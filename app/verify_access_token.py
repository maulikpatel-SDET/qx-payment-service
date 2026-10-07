"""R3-01 VERIFY side: payment-service verifies the RS256 JWT issued by qx-key-service."""
import jwt

from app.key_paths import RSA_PUBLIC_KEY


def verify_access_token(token: str) -> dict:
    with open(RSA_PUBLIC_KEY, "rb") as fh:
        public_pem = fh.read()
    return jwt.decode(token, public_pem, algorithms=["RS256"], issuer="qx-key-service")
