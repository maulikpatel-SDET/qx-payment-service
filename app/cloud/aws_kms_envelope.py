"""R3-10 CONTROL (safe): AES-256 envelope encryption with the symmetric KMS key."""
import boto3

kms = boto3.client("kms", region_name="ap-south-1")


def new_data_key():
    return kms.generate_data_key(KeyId="alias/qx-card-data", KeySpec="AES_256")
