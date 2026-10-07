"""R3-09 Signs with AWS KMS keys created in qx-cloud-infra/terraform/aws_kms.tf (referenced only by alias)."""
import boto3

kms = boto3.client("kms", region_name="ap-south-1")


def sign_payment(digest: bytes) -> bytes:
    resp = kms.sign(KeyId="alias/qx-payment-signing", Message=digest,
                    MessageType="DIGEST", SigningAlgorithm="RSASSA_PSS_SHA_256")
    return resp["Signature"]


def sign_settlement(digest: bytes) -> bytes:
    resp = kms.sign(KeyId="alias/qx-settlement-signing", Message=digest,
                    MessageType="DIGEST", SigningAlgorithm="ECDSA_SHA_256")
    return resp["Signature"]
