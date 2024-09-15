from discord.ext import commands

from reminder.commands.service import execute_reminder

from .config import DISCORD_BOT_TOKEN
from .bot import bot
from .constants import NO_ARGS


@bot.command()
async def reminder(ctx: commands.Context, *args):
    try:
        if len(args) == 0:
            raise Exception(NO_ARGS)

        await execute_reminder(ctx, list(args))

    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")
        return


def main():
    bot.run(DISCORD_BOT_TOKEN)


if __name__ == "__main__":
    main()
