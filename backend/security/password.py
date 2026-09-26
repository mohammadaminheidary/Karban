import bcrypt



def hash_password(password: str):

    password_bytes = password.encode(
        "utf-8"
    )


    hashed = bcrypt.hashpw(
        password_bytes,
        bcrypt.gensalt()
    )


    return hashed.decode(
        "utf-8"
    )




def verify_password(
    password: str,
    password_hash: str
):

    password_bytes = password.encode(
        "utf-8"
    )


    if len(password_bytes) > 72:
        return False


    try:

        return bcrypt.checkpw(
            password_bytes,
            password_hash.encode("utf-8")
        )

    except ValueError:

        return False