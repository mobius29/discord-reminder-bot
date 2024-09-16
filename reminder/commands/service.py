from discord.ext import commands

from .parser import parser
from .sub import set_reminder, cmd_list, remove_reminders_service


async def execute_reminder(ctx: commands.Context, arguments: list[str]):
    try:
        args = parser.parse_args(arguments)

        if args.help:
            await ctx.send(parser.format_help())
            return

        subcommand = args.subcommand if hasattr(args, "subcommand") else "set"
        if subcommand == "set":
            await set_reminder(ctx, args)

        if subcommand == "list":
            await cmd_list(ctx, args)

        if subcommand == "remove":
            await remove_reminders_service(ctx, args)

    except SystemExit as e:
        await ctx.send(f"An error occurred: {str(e)}")
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")
