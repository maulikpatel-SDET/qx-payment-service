# qx-payment-service  (Repo 3 of 4)

Consumer service. It does NOT generate keys and mostly does NOT name algorithms.
Keys come from qx-key-service, crypto from qx-shared-crypto-lib, algorithm names
from qx-infra-config.

Deployment layout (all repos side by side):
    /opt/qx/qx-key-service/keys/...
    /opt/qx/qx-payment-service/...
