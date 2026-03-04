import json
import time
import secrets
import os
from jose import jwt

USERS_FILE = os.path.join(os.path.dirname(__file__), "../data/users.json")
JWT_SECRET = os.getenv("JWT_SECRET", "dev_secret")

LOGIN_TOKENS = {}

DEFAULT_MAX_USAGE = 10
COOLDOWN_SECONDS = 60


def load_users():
    with open(USERS_FILE, "r") as f:
        return json.load(f)


def save_users(data):
    with open(USERS_FILE, "w") as f:
        json.dump(data, f, indent=4)


def find_user(email):

    data = load_users()

    for user in data["users"]:
        if user["email"] == email:
            return user

    return None


def create_user(email):

    data = load_users()

    user = {
        "email": email,
        "created_at": int(time.time()),
        "last_login": None,
        "usage_count": 0,
        "max_usage": DEFAULT_MAX_USAGE,
        "last_request_time": None
    }

    data["users"].append(user)
    save_users(data)

    return user


def update_last_login(email):

    data = load_users()

    for user in data["users"]:
        if user["email"] == email:
            user["last_login"] = int(time.time())

    save_users(data)


def generate_login_token(email):

    token = secrets.token_urlsafe(32)

    LOGIN_TOKENS[token] = {
        "email": email,
        "expires": time.time() + 600
    }

    return token


def verify_login_token(token):

    if token not in LOGIN_TOKENS:
        return None

    data = LOGIN_TOKENS[token]

    if time.time() > data["expires"]:
        del LOGIN_TOKENS[token]
        return None

    email = data["email"]

    del LOGIN_TOKENS[token]

    return email


def generate_jwt(email):

    payload = {
        "email": email,
        "iat": int(time.time())
    }

    return jwt.encode(payload, JWT_SECRET, algorithm="HS256")


def check_usage_allowed(email):

    data = load_users()

    for user in data["users"]:

        if user["email"] == email:

            if user["usage_count"] >= user["max_usage"]:
                return False, "Usage limit reached"

            if user["last_request_time"]:

                elapsed = time.time() - user["last_request_time"]

                if elapsed < COOLDOWN_SECONDS:
                    remaining = int(COOLDOWN_SECONDS - elapsed)
                    return False, f"Wait {remaining}s before next request"

            return True, None

    return False, "User not found"


def record_usage(email):

    data = load_users()

    for user in data["users"]:
        if user["email"] == email:

            user["usage_count"] += 1
            user["last_request_time"] = int(time.time())

    save_users(data)
