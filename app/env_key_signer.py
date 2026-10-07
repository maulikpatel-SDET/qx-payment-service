"""R3-17 Key AND algorithm come only from environment variables (.env / docker-compose / CI)."""
import os

import jwt

PRIVATE_KEY = os.environ["JWT_PRIVATE_KEY"]
ALGORITHM = os.getenv("JWT_ALG", "RS256")


def issue_merchant_token(merchant_id: str) -> str:
    return jwt.encode({"mid": merchant_id}, PRIVATE_KEY, algorithm=ALGORITHM)
