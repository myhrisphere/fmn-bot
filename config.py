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
    "Europe/Warsaw"
)


LOG_LEVEL = os.getenv(
    "LOG_LEVEL",
    "INFO"
)


if not DISCORD_TOKEN:

    raise RuntimeError(
        "DISCORD_TOKEN is missing from .env"
    )