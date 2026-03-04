ALLOWED_DOMAINS = {
    "gmail.com",
    "outlook.com",
    "hotmail.com",
    "icloud.com",
    "me.com",
    "mac.com",
    "yahoo.com",
    "proton.me",
    "protonmail.com"
}


def validate_email_domain(email: str) -> bool:
    """
    Ensures email belongs to trusted providers.
    """

    if "@" not in email:
        return False

    domain = email.split("@")[-1].lower()

    return domain in ALLOWED_DOMAINS