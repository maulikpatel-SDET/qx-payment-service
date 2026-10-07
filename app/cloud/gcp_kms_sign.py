"""R3-12 Signs with the GCP KMS key defined in qx-cloud-infra/terraform/gcp_kms.tf. Algorithm only in Terraform."""
from google.cloud import kms

KEY_VERSION = ("projects/qx-test-project/locations/asia-south1/keyRings/qx-test-ring/"
               "cryptoKeys/qx-refund-signing/cryptoKeyVersions/1")


def sign_refund(digest_sha256: bytes) -> bytes:
    client = kms.KeyManagementServiceClient()
    resp = client.asymmetric_sign(request={"name": KEY_VERSION, "digest": {"sha256": digest_sha256}})
    return resp.signature
