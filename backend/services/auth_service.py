from sqlalchemy.orm import Session

from models.user import User

from security.password import verify_password



def authenticate_user(

    db: Session,

    username: str,

    password: str

):


    user = (
        db.query(User)
        .filter(
            User.username == username
        )
        .first()
    )



    if not user:

        return None



    if not verify_password(

        password,

        user.password_hash

    ):

        return None



    return user