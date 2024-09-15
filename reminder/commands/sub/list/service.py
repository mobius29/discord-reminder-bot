from argparse import Namespace
from discord.ext import commands
from datetime import datetime

from reminder.config import NOTION_REMINDERS_DB_ID
from reminder.notion import notion
from .parser import list_parser


async def cmd_list(ctx: commands.Context, args: Namespace):
    if args._list_help:
        await ctx.send(list_parser.format_help())
        return

    response = await notion.databases.query(database_id=NOTION_REMINDERS_DB_ID)
    pages = response["results"]

    for page in pages:
        properties = page["properties"]
        id = properties["ID"]["unique_id"]["number"]
        date = properties["날짜"]["date"]["start"]
        creator = properties["생성자"]["created_by"]["name"]
        message = properties["메시지"]["title"][0]["text"]["content"]

        date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f%z")
        date = datetime.strftime(date, "%Y-%m-%d %H:%M")
        await ctx.send(f"{id}\t{date}\t{message}\t{creator}")
