"""CR-07  Verifies tokens with the JWKS published by qx-key-service (RS256)."""
import json

import jwt

from app.key_paths import JWKS_FILE


def verify(token: str) -> dict:
    with open(JWKS_FILE) as fh:
        jwk = json.load(fh)["keys"][0]
    public_key = jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(jwk))
    return jwt.decode(token, public_key, algorithms=[jwk["alg"]])
