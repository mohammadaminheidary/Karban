from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)

from sqlalchemy.orm import Session

from database import get_database

from models.user import User

from schemas.auth_schema import (
    LoginRequest,
    LoginResponse,
)

from services.auth_service import authenticate_user

from security.jwt import create_access_token

from security.auth import get_current_user


router = APIRouter(
    prefix="/api",
    tags=["Authentication"],
)


@router.post(
    "/login",
    response_model=LoginResponse,
)
def login(
    data: LoginRequest,
    db: Session = Depends(get_database),
):

    user = authenticate_user(
        db,
        data.username,
        data.password,
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="نام کاربری یا رمز عبور اشتباه است",
        )

    token = create_access_token(
        {
            "sub": user.username,
        }
    )

    return {
        "success": True,
        "token": token,
        "user": {
            "id": user.id,
            "username": user.username,
        },
    }


@router.get("/auth/me")
def get_me(
    current_user: User = Depends(get_current_user),
):

    return {
        "success": True,
        "user": {
            "id": current_user.id,
            "username": current_user.username,
        },
    }