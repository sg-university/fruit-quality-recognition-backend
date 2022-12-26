import os

from pydantic import BaseSettings


class DatabaseSettings(BaseSettings):
    DIALECT = os.getenv("WEB_DB_DIALECT", "postgresql")
    HOST = os.getenv("WEB_DB_HOST", "localhost")
    PORT = os.getenv("WEB_DB_PORT", 5432)
    USER = os.getenv("WEB_DB_USER", "default")
    PASSWORD = os.getenv("WEB_DB_PASSWORD", "default")
    DATABASE = os.getenv("WEB_DB_NAME", "default")

    if DIALECT == "sqlite":
        URL = f"{DIALECT}:///{DATABASE}.sqlite3"
    else:
        URL = f"{DIALECT}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"


database_settings = DatabaseSettings()
