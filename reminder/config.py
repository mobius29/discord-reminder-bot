import os

from dotenv import load_dotenv

load_dotenv()

def get_env(key: str) -> str:
    value = os.getenv(key)
    if value is None:
        raise ValueError(f"{key} is not set in the environment variables")
    return value

DISCORD_BOT_TOKEN = get_env("DISCORD_BOT_TOKEN")
NOTION_API_TOKEN = get_env("NOTION_API_TOKEN")
NOTION_REMINDERS_DB_ID = get_env("NOTION_REMINDERS_DB_ID")
