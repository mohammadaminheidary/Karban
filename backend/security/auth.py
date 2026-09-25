from fastapi import Depends, HTTPException, status
from fastapi.security import (
    HTTPAuthorizationCredentials,
    HTTPBearer
)
from sqlalchemy.orm import Session

from database import get_database
from models.user import User
from security.jwt import decode_access_token


bearer_scheme = HTTPBearer(
    auto_error=False
)


def unauthorized():

    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Authentication required",
        headers={
            "WWW-Authenticate": "Bearer"
        }
    )


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(
        bearer_scheme
    ),
    db: Session = Depends(get_database)
):

    if credentials is None:

        raise unauthorized()


    token = credentials.credentials


    payload = decode_access_token(
        token
    )


    if payload is None:

        raise unauthorized()


    username = payload.get("sub")


    if not username:

        raise unauthorized()


    user = (
        db.query(User)
        .filter(
            User.username == username
        )
        .first()
    )


    if user is None:

        raise unauthorized()


    return user