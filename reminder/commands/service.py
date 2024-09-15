from discord.ext import commands

from .parser import parser
from .sub import set_reminder, cmd_list


async def execute_reminder(ctx: commands.Context, arguments: list[str]):
    args = parser.parse_args(arguments)

    if args.help:
        await ctx.send(parser.format_help())
        return

    if args.subcommand == "set":
        await set_reminder(ctx, args)

    if args.subcommand == "list":
        await cmd_list(ctx, args)
