"""R3-14 Loads a PEM private key from AWS Secrets Manager (secret defined in qx-cloud-infra) and signs webhooks."""
import boto3
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec

secrets = boto3.client("secretsmanager", region_name="ap-south-1")


def sign_webhook(body: bytes) -> bytes:
    pem = secrets.get_secret_value(SecretId="qx/payment/webhook-signing-key")["SecretString"]
    key = serialization.load_pem_private_key(pem.encode(), password=None)
    return key.sign(body, ec.ECDSA(hashes.SHA256()))
