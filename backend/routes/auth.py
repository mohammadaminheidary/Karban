from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from database import get_database

from schemas.auth_schema import LoginRequest

from services.auth_service import authenticate_user

from security.jwt import create_access_token



router = APIRouter(

    prefix="/api",

    tags=["Authentication"]

)



@router.post("/login")
def login(

    data: LoginRequest,

    db: Session = Depends(get_database)

):


    user = authenticate_user(

        db,

        data.username,

        data.password

    )



    if not user:


        return {

            "success": False,

            "message":
            "نام کاربری یا رمز عبور اشتباه است"

        }



    token = create_access_token({

        "sub": user.username

    })



    return {

        "success": True,

        "token": token,

        "user": {

            "id": user.id,

            "username": user.username

        }

    }