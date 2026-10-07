"""CR-05  Calls the shared library only. RSA is hidden inside qx-shared-crypto-lib."""
from qx_crypto import sign_payload, verify_payload


def authorise_payment(payment: bytes) -> bytes:
    signature = sign_payload(payment)
    verify_payload(payment, signature)
    return signature
