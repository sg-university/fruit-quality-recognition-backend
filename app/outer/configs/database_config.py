import os

from pydantic import BaseSettings


class DatabaseSettings(BaseSettings):
    DIALECT = os.getenv("APP_DB_DIALECT", "postgresql")
    HOST = os.getenv("APP_DB_HOST", "localhost")
    PORT = os.getenv("APP_DB_PORT", 5432)
    USER = os.getenv("APP_DB_USER", "default")
    PASSWORD = os.getenv("APP_DB_PASSWORD", "default")
    DATABASE = os.getenv("APP_DB_NAME", "fruit-quality-recognition")

    if DIALECT == "sqlite":
        URL = f"{DIALECT}:///{DATABASE}.sqlite3"
    else:
        URL = f"{DIALECT}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

    class Config:
        env_file = ".env"


database_settings = DatabaseSettings()
