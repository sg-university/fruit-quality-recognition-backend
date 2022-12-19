import os

from pydantic import BaseSettings


class DatabaseSettings(BaseSettings):
    DIALECT = os.getenv("DIALECT", "postgresql")
    HOST = os.getenv("DB_HOST", "localhost")
    PORT = os.getenv("DB_PORT", 5432)
    USER = os.getenv("DB_USER", "default")
    PASSWORD = os.getenv("DB_PASSWORD", "default")
    DATABASE = os.getenv("DB_DATABASE", "default")

    if DIALECT == "sqlite":
        URL = f"{DIALECT}:///{DATABASE}.sqlite3"
    else:
        URL = f"{DIALECT}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"


database_settings = DatabaseSettings()
