from argparse import Namespace
from discord.ext import commands

from .parser import list_parser


async def cmd_list(ctx: commands.Context, args: Namespace):
    if args._list_help:
        await ctx.send(list_parser.format_help())
        return

    return
