from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import engine, Base
from routes.auth import router as auth_router


# ایجاد برنامه FastAPI
app = FastAPI(
    title="Karbon API",
    version="1.0.0"
)


# ساخت جدول‌های دیتابیس
Base.metadata.create_all(
    bind=engine
)


# تنظیم CORS برای اتصال Frontend
app.add_middleware(

    CORSMiddleware,

    allow_origins=[

        # Live Server VS Code
        "http://127.0.0.1:5501",
        "http://localhost:5501",

        # در صورت استفاده از پورت 5500
        "http://127.0.0.1:5500",
        "http://localhost:5500"

    ],

    allow_credentials=True,

    allow_methods=[

        "*"

    ],

    allow_headers=[

        "*"

    ]

)


# ثبت Route های احراز هویت
app.include_router(
    auth_router
)



# تست سلامت Backend
@app.get("/")
def home():

    return {

        "status": "running",

        "message": "Karbon Backend is running"

    }