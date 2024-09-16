from argparse import Namespace

import discord
from discord.ext import commands

from datetime import datetime

from reminder.config import NOTION_REMINDERS_DB_ID
from reminder.notion import notion
from reminder.types.reminder import Reminder
from reminder.utils.reminder import make_reminder_table
from reminder.utils.time import parse_notion_time_format

from .parser import list_parser


async def get_reminder_list(filter) -> list[Reminder]:
    response = await notion.databases.query(
        database_id=NOTION_REMINDERS_DB_ID,
        filter=filter,
        sorts=[
            {"property": "날짜", "direction": "ascending"},
        ],
    )

    reminders: list[Reminder] = []
    for page in response["results"]:
        properties = page["properties"]

        page_id: str = page["id"]
        id: int = properties["ID"]["unique_id"]["number"]
        creator: str = properties["생성자"]["rich_text"][0]["plain_text"]
        message: str = properties["메시지"]["title"][0]["plain_text"]
        date: str = properties["날짜"]["date"]["start"]
        date: str = datetime.strftime(parse_notion_time_format(date), "%Y-%m-%d %H:%M")

        reminder = Reminder(
            page_id=page_id,
            id=id,
            date=date,
            creator=creator,
            message=message,
        )
        reminders.append(reminder)

    return reminders


async def cmd_list(ctx: commands.Context, args: Namespace):
    if args._list_help:
        await ctx.send(list_parser.format_help())
        return

    reminders = await get_reminder_list(
        filter={
            "property": "생성자",
            "rich_text": {"equals": ctx.author.display_name},
        },
    )
    embed_reminder = discord.Embed(
        title="리마인드 목록",
        description=make_reminder_table(reminders),
        color=discord.Color.orange(),
    )

    await ctx.send(embed=embed_reminder)
