from database import Base, engine, SessionLocal

from models.user import User

from security.password import hash_password



# ساخت جدول‌ها
Base.metadata.create_all(bind=engine)



db = SessionLocal()



user = User(

    username="admin",

    password_hash=hash_password("123456")

)



db.add(user)

db.commit()

db.close()



print("User created")