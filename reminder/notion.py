from notion_client import AsyncClient

from reminder.config import NOTION_API_TOKEN

notion = AsyncClient(auth=NOTION_API_TOKEN)
