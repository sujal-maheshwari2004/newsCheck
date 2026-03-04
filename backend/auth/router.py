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
        "from": "NewsCheck <onboarding@resend.dev>",
        "to": email,
        "subject": "Your NewsCheck login link",
        "html": f"""
        <h2>Login to NewsCheck</h2>

        <p>
        Click below to log in:
        </p>

        <p>
        <a href="{login_link}">
        {login_link}
        </a>
        </p>

        <p>This link expires in 10 minutes.</p>

        <hr/>

        <p>
        Thanks for checking out <b>NewsCheck</b> — the idea is simple:
        take long news videos and compress them into five useful points
        so you don’t have to sit through 20 minutes of dramatic anchor music.
        </p>

        <p>
        Under the hood it downloads the audio, transcribes it,
        and runs the transcript through an LLM summarization pipeline.
        Basically: YouTube → audio → transcript → AI summary.
        </p>

        <p>
        Occasionally a request may fail because YouTube’s bot detection
        is extremely enthusiastic about protecting its videos from
        suspiciously curious cloud servers.
        </p>

        <p>
        If you’re curious about how everything works, here’s the repo:
        </p>

        <p>
        <b>GitHub:</b><br>
        <a href="https://github.com/sujal-maheshwari2004/newsCheck">
        github.com/sujal-maheshwari2004/newsCheck
        </a>
        </p>

        <p>
        And if you'd like to see more of my work:
        </p>

        <p>
        <b>Resume:</b><br>
        <a href="https://drive.google.com/file/d/1EommcS3MihfPd-LvcarG4Z3WvAarZMZO/view">
        View Resume
        </a>
        </p>

        <p>
        If you'd like a quick walkthrough of the project,
        feel free to reply — happy to demo it.
        </p>

        <p>
        Best,<br>
        Sujal Maheshwari<br>
        sujalmaheshwari07@gmail.com
        </p>

        <p><i>
        P.S. If your video processes perfectly on the first try,
        congratulations — you may have just defeated YouTube’s
        bot detection for the day.
        </i></p>
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
