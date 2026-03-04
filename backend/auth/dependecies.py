from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from jose import jwt
import os

JWT_SECRET = os.getenv("JWT_SECRET", "dev_secret")

security = HTTPBearer()


def get_current_user(token=Depends(security)):

    try:
        payload = jwt.decode(
            token.credentials,
            JWT_SECRET,
            algorithms=["HS256"]
        )

        return payload["email"]

    except Exception:
        raise HTTPException(401, "Invalid authentication")