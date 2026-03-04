import os
import resend

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from auth.utils import (
    find_user,
    create_user,
    generate_login_token,
    verify_login_token,
    generate_jwt,
    update_last_login
)

from auth.email_validator import validate_email_domain


router = APIRouter()

resend.api_key = os.getenv("RESEND_API_KEY")


class EmailRequest(BaseModel):
    email: str


@router.post("/request-login")
async def request_login(data: EmailRequest):

    email = data.email.strip().lower()

    if not email:
        raise HTTPException(400, "Email required")

    if not validate_email_domain(email):
        raise HTTPException(
            400,
            "Please use Gmail, Outlook, Apple, or another major provider"
        )

    user = find_user(email)

    if not user:
        user = create_user(email)

    token = generate_login_token(email)

    frontend = os.getenv("FRONTEND_URL", "http://localhost:5173")

    login_link = f"{frontend}/verify?token={token}"

    resend.Emails.send({
        "from": "newsCheck <login@yourdomain.com>",
        "to": email,
        "subject": "Login to NewsCheck",
        "html": f"""
        <h2>Login to NewsCheck</h2>
        <p>Click below to login:</p>
        <a href="{login_link}">{login_link}</a>
        <p>This link expires in 10 minutes.</p>
        """
    })

    return {"message": "Login link sent"}


@router.get("/verify")
async def verify_login(token: str):

    email = verify_login_token(token)

    if not email:
        raise HTTPException(400, "Invalid or expired token")

    update_last_login(email)

    jwt_token = generate_jwt(email)

    return {
        "token": jwt_token,
        "email": email
    }