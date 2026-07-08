import os

from dotenv import load_dotenv


load_dotenv()


DISCORD_TOKEN = os.getenv(
    "DISCORD_TOKEN"
)


DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite+aiosqlite:///calendar.db"
)


DEFAULT_TIMEZONE = os.getenv(
    "DEFAULT_TIMEZONE",
    "UTC"
)