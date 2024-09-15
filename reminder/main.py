import re

from datetime import datetime
from discord.ext import commands

from .config import DISCORD_BOT_TOKEN
from .bot import bot
from .utils import set_timeout
from .parser import parser, set_parser, list_parser
from .constants import NO_ARGS


@bot.command()
async def reminder(ctx: commands.Context, *args):
    if len(args) == 0:
        await ctx.send(NO_ARGS)
        return

    me = ctx.me
    channel_name: str | None = getattr(ctx.channel, "name", None)
    if not channel_name:
        await ctx.send("채널이 아닌 곳에는 보낼 수 없습니다.")
        return

    try:
        arguments = parser.parse_args(list(args))

        if arguments._help:
            await ctx.send(parser.format_help())
            return

        if arguments.message is None:
            await ctx.send("리마인더 메시지를 입력하세요.")
            return

        if arguments.subcommand == "set":
            if arguments._set_help:
                await ctx.send(set_parser.format_help())
                return

            retMessage = (
                f"{channel_name} 채널에 {me.name}님의 리마인더가 설정되었습니다."
            )
            if arguments.after is not None:
                if (
                    arguments.week is not None
                    or arguments.date is not None
                    or arguments.time is not None
                ):
                    await ctx.send(
                        "--after 옵션은 다른 시간 설정과 함께 사용할 수 없습니다."
                    )
                    return

                re_times = re.compile("(\\d+)(h|m|s)$")
                times: list[str] = list(
                    filter(lambda x: len(x) != 0, arguments.after[0].split(" "))
                )

                time_text = []
                seconds = 0
                for time in times:
                    time = re_times.match(time)
                    if time is None:
                        raise Exception("Invalid time format")

                    (value, unit) = time.groups()
                    value = int(value)

                    if unit == "h":
                        time_text.append(f"{value}시간")
                        seconds += value * 3600
                    if unit == "m":
                        time_text.append(f"{value}분")
                        seconds += value * 60
                    if unit == "s":
                        time_text.append(f"{value}초")
                        seconds += value

                await ctx.send(retMessage)
                await ctx.send(f"{' '.join(time_text)} 후에 리마인더가 발송됩니다.")
                await set_timeout(seconds, ctx.send, f"{arguments.message[0]}")

                return

            date = (
                arguments.date[0]
                if arguments.date is not None
                else datetime.now().strftime("%Y-%m-%d")
            )
            time = arguments.time[0] if arguments.time is not None else "09:00:00"

            date_time = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M:%S")
            if date_time < datetime.now():
                await ctx.send("현재 시간 이후로 설정해주세요.")
                return

            await ctx.send(date_time.ctime())

            return

        if arguments.subcommand == "list":
            if arguments._list_help:
                await ctx.send(list_parser.format_help())
                return

            return

        if arguments.subcommand is None:
            await ctx.send("리마인더 명령어를 입력하세요.")
            await ctx.send(parser.format_help())
            return

    except SystemExit as e:
        await ctx.send(parser.format_help())
        return


def main():
    bot.run(DISCORD_BOT_TOKEN)


if __name__ == "__main__":
    main()
