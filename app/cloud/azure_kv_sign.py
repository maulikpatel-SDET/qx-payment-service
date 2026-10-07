"""R3-11 Signs with the Azure Key Vault key defined in qx-cloud-infra/terraform/azure_key_vault.tf."""
from azure.identity import DefaultAzureCredential
from azure.keyvault.keys.crypto import CryptographyClient, SignatureAlgorithm

KEY_ID = "https://qx-test-kv.vault.azure.net/keys/qx-invoice-signing"


def sign_invoice_digest(digest: bytes) -> bytes:
    client = CryptographyClient(KEY_ID, credential=DefaultAzureCredential())
    return client.sign(SignatureAlgorithm.rs256, digest).signature
