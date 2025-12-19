from os import getenv

from dotenv import load_dotenv

load_dotenv()

APPLICATION_NAME = getenv("APPLICATION_NAME", "")
POSTGRES_USER = getenv("POSTGRES_USER", "")
POSTGRES_PASSWORD = getenv("POSTGRES_PASSWORD", "")
POSTGRES_DB= getenv("POSTGRES_DB", "")
DATABASE_URL = getenv("DATABASE_URL", "")
APP_PORT = getenv("APP_PORT", "")
