import asyncio
from datetime import datetime

from reminder.constants.notion import NOTION_DATE_FORMAT, NOTION_DATE_TIME_FORMAT


async def set_timeout(seconds: int, callback, *args, **kwargs):
    await asyncio.sleep(seconds)
    await callback(*args, **kwargs)


def parse_notion_time_format(notion_date_time: str, show_time: bool = True) -> datetime:
    if show_time:
        return datetime.strptime(notion_date_time, NOTION_DATE_TIME_FORMAT)

    return datetime.strptime(notion_date_time, NOTION_DATE_FORMAT)
