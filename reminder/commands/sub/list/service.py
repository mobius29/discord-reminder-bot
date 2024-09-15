from typing import TypedDict
from argparse import Namespace
from discord.ext import commands

from reminder.config import NOTION_REMINDERS_DB_ID
from reminder.notion import notion
from .parser import list_parser


class NotionDatabase(TypedDict):
    object: str
    id: str
    created_time: str
    last_edited_time: str
    title: list[dict[str, str]]


async def cmd_list(ctx: commands.Context, args: Namespace):
    if args._list_help:
        await ctx.send(list_parser.format_help())
        return

    response = await notion.databases.query(database_id=NOTION_REMINDERS_DB_ID)

    for result in response["results"]:
        print(result)
