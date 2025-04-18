import os
## should not be set on productive deployments
DEBUG = os.getenv("DEBUG") == "true"


import sys
sys.path.append("../example")

import db_statements
import api

app = api.app


## HTTPBasic-Auth

from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.responses import RedirectResponse

security = HTTPBasic()


## Enforce https (or localhost)

@app.middleware("https")
async def redirect_to_https(request, call_next):
    if request.url.scheme != "https" and not str(request.url).startswith("http://localhost"):
        print("Site should only be accessed via https or on localhost")
        url = request.url.replace(scheme="https", port=443)
        return RedirectResponse(url, status_code=301)
    return await call_next(request)


## password-hash validation

from passlib.hash import argon2
import secrets_handling
pepper = secrets_handling.get_secrets()['pepper']


@app.get("/demo/basicauth")
def basicauth(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    ## the credentials object contains username and password
    return {"username": credentials.username, "password": credentials.password}



@app.get("/login")
def login(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    """
    Example implementation of a simple login via HTTPBasic-Auth + hashed passwords from a database.
    For better security a counter of failed logins should be added.
    """

    iban = credentials.username
    password = credentials.password

    ## We should return the same, when either username or password is incorrect
    ## Warning: this implementation is still vulnerable against timing attacks
    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
    )

    cur = db_statements.get_cursor()
    cur.execute("SELECT password_hash from logins WHERE iban = ?", (iban,))
    result = cur.fetchone()

    if not result:
        if DEBUG:
            print(f"Attempt to login as not existing user {iban}")
        raise exception

    password_hash = result[0]
    if DEBUG:
        print(f"Hash found in database: {password_hash}")

    if not argon2.verify(pepper + password, password_hash):
        if DEBUG:
            print("Hash not matching for pepper+password")
        raise exception

    ## we could now create a login-token or save a session
    return "Login Successful"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
