"""Where this service finds keys produced by qx-key-service."""
import os

KEY_SERVICE_DIR = os.environ.get("QX_KEY_SERVICE_DIR", "/opt/qx/qx-key-service")
RSA_SIGNING_KEY = f"{KEY_SERVICE_DIR}/keys/rsa_signing_private.pem"
RSA_PUBLIC_KEY = f"{KEY_SERVICE_DIR}/keys/rsa_signing_public.pem"
EC_SIGNING_KEY = f"{KEY_SERVICE_DIR}/keys/ec_signing_private.pem"
TEST_EC_KEY = f"{KEY_SERVICE_DIR}/keys/test_ec_private.pem"
JWKS_FILE = f"{KEY_SERVICE_DIR}/jwks.json"
