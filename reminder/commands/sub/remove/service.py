from .parser import remove_parser

from argparse import Namespace
import asyncio
import discord
from discord.ext.commands import Context
from reminder.commands.sub.list.service import get_reminder_list
from reminder.notion import notion
from reminder.utils.reminder import make_reminder_table

from reminder.bot import bot


async def remove_reminder_by_page_id(page_id: str):
    try:
        await notion.pages.update(page_id, archived=True)
    except Exception as e:
        print(f"Error: {str(e)}")


async def remove_reminders_service(ctx: Context, args: Namespace):
    try:
        if args._remove_help:
            await ctx.send(remove_parser.format_help())
            return

        reminder_list = await get_reminder_list(
            {
                "property": "생성자",
                "rich_text": {"equals": ctx.author.display_name},
            }
        )

        if len(reminder_list) == 0:
            await ctx.send("삭제할 리마인더가 없습니다.")
            return

        embed_reminder = discord.Embed(
            title="리마인드 목록",
            description=make_reminder_table(reminder_list),
            color=discord.Color.orange(),
        )
        await ctx.send(embed=embed_reminder)

        if args.all:
            await ctx.send("모든 리마인더를 삭제합니다. Y/N")
            try:
                answer = await bot.wait_for(
                    "message",
                    check=lambda m: m.author == ctx.author
                    and m.channel == ctx.channel
                    and m.content in ["Y", "N"],
                    timeout=10,
                )
                if answer == "N":
                    await ctx.send("취소되었습니다.")
                    return

            except asyncio.TimeoutError:
                await ctx.send("시간 초과")
                return

            try:
                for reminder in reminder_list:
                    await remove_reminder_by_page_id(reminder["page_id"])

                await ctx.send("모든 리마인더가 삭제되었습니다.")

            except Exception as e:
                print(f"Error: {str(e)}")
                return

    except Exception as e:
        print(f"Error: {str(e)}")
