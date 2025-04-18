import secrets
import os, stat

SECRETS_FILE = "secrets.env"

def create_secrets():
    if os.path.exists(SECRETS_FILE):
        print(f"ERROR: The file {SECRETS_FILE} already exists!")
        print("It is not overwritten.")
        exit

    ## pepper used for password hashing
    pepper = secrets.token_urlsafe()

    with open(SECRETS_FILE, 'w') as file:
        os.chmod(SECRETS_FILE, stat.S_IRUSR | stat.S_IWUSR)
        file.write(f"export PEPPER='{pepper}'\n")


def get_secrets():
    """
    reads secrets from environment variables
    """

    secrets = {"pepper": os.getenv("PEPPER")}

    if not secrets['pepper']:
        raise Error("Secrets missing! Ensure you source secrets.env")

    return secrets


if __name__ == "__main__":
    create_secrets()
