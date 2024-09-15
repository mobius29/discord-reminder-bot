import argparse
import re

from datetime import datetime
from discord.ext import commands

from .config import DISCORD_BOT_TOKEN
from .bot import bot
from .utils import set_timeout

@bot.command()
async def reminder(ctx: commands.Context, *args):
    if len(args) == 0:
        await ctx.send("""
최소 1개의 인자가 필요합니다.

도움이 필요하다면 다음과 같이 입력하세요.
`$reminder -h` 또는 `$reminder --help`
""")
        return

    parser = argparse.ArgumentParser(description="Discord Reminder Bot", add_help=False)
    parser.add_argument("-h", "--help", action="store_true", dest="_help", help="도움말을 출력합니다.")

    subparsers = parser.add_subparsers(dest="subcommand", help="리마인더 명령어를 입력하세요.")

    set_parser = subparsers.add_parser("set", help="리마인더를 설정합니다.", add_help=False)
    set_parser.add_argument("-h", "--help", action="store_true", dest="_set_help", help="도움말을 출력합니다.")
    set_parser.add_argument("-m", "--message", dest="message", nargs="+", help="리마인더 메시지를 입력하세요.")
    set_parser.add_argument("-w", "--week", dest="week", nargs="+", help="요일을 설정합니다. 기본적으로 모든 평일로 설정합니다.")
    set_parser.add_argument("-d", "--date", dest="date", nargs="+", help="날짜를 설정합니다. 기본적으로 오늘로 설정합니다.")
    set_parser.add_argument("-t", "--time", dest="time", nargs="+", help="시간을 설정합니다. 기본적으로 09:00:00로 설정합니다.")
    set_parser.add_argument("--after", dest="after", nargs="+", help="리마인더를 설정한 시간 이후로 설정합니다. 이는 다른 시간 설정과 함께 사용할 수 없습니다.")

    list_parser = subparsers.add_parser("list", help="리마인더 목록을 출력합니다.", add_help=False)
    list_parser.add_argument("-h", "--help", action="store_true", dest="_list_help", help="도움말을 출력합니다.")
    list_parser.add_argument("--author", dest="author", help="리마인더 목록을 출력할 사용자를 지정합니다.")

    me = ctx.me
    channel = ctx.channel
    channel_name = channel.name # type: ignore 

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

            retMessage = f"{channel_name} 채널에 {me.name}님의 리마인더가 설정되었습니다."
            if arguments.after is not None:
                if arguments.week is not None or arguments.date is not None or arguments.time is not None:
                    await ctx.send("--after 옵션은 다른 시간 설정과 함께 사용할 수 없습니다.")
                    return

                re_times = re.compile('(\\d+)(h|m|s)$')
                times: list[str] = list(filter(lambda x: len(x) != 0, arguments.after[0].split(" ")))

                time_text = []
                seconds = 0
                for time in times:
                    time = re_times.match(time)
                    if time == None:
                        raise Exception("Invalid time format")

                    (value, unit) = time.groups()
                    value = int(value)

                    if unit == 'h':
                        time_text.append(f"{value}시간")
                        seconds += value * 3600
                    if unit == 'm':
                        time_text.append(f"{value}분")
                        seconds += value * 60
                    if unit == 's':
                        time_text.append(f"{value}초")
                        seconds += value

                await ctx.send(retMessage)
                await ctx.send(f"{' '.join(time_text)} 후에 리마인더가 발송됩니다.")
                await set_timeout(seconds, ctx.send, f"{arguments.message[0]}")

                return


            date = arguments.date[0] if arguments.date is not None else datetime.now().strftime("%Y-%m-%d")
            time = arguments.time[0] if arguments.time is not None else "09:00:00"

            date_time = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M:%S")

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
