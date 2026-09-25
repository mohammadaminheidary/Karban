from pathlib import Path


APP_DATA_DIR = (
    Path.home()
    / ".karbon"
)


APP_DATA_DIR.mkdir(
    parents=True,
    exist_ok=True
)


DATABASE_PATH = (
    APP_DATA_DIR
    / "karbon.db"
)


DATABASE_URL = (
    f"sqlite:///{DATABASE_PATH.as_posix()}"
)