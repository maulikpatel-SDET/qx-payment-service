"""R3-13 Signs through HashiCorp Vault transit (key type set in qx-cloud-infra/terraform/vault_transit.tf)."""
import base64

import hvac

client = hvac.Client(url="https://vault.qx.example.com")


def sign_payout(payload: bytes) -> str:
    resp = client.secrets.transit.sign_data(
        name="qx-payout-signing",
        hash_input=base64.b64encode(payload).decode(),
        hash_algorithm="sha2-256",
        signature_algorithm="pss",
    )
    return resp["data"]["signature"]
