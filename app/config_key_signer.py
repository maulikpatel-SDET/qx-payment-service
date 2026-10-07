"""R3-15 Loads the signing key and algorithm from config/application.yml (PEM inside YAML)."""
import jwt
import yaml

with open("config/application.yml") as fh:
    CFG = yaml.safe_load(fh)["jwt"]


def issue_partner_token(partner: str) -> str:
    return jwt.encode({"partner": partner}, CFG["private-key"], algorithm=CFG["algorithm"])
