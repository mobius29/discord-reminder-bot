import re
from argparse import Namespace
from discord.ext import commands

from .parser import set_parser
from ....utils import set_timeout


async def set_reminder(ctx: commands.Context, args: Namespace):
    if args._set_help:
        await ctx.send(set_parser.format_help())
        return

    if args.message is None:
        await ctx.send("Please provide a message.")
        return

    if args.after is not None:
        if args.week is not None or args.date is not None or args.time is not None:
            await ctx.send("--after 옵션은 다른 시간 설정과 함께 사용할 수 없습니다.")
            return

        re_times = re.compile("(\\d+)(h|m|s)$")
        times: list[str] = list(filter(lambda x: len(x) != 0, args.after[0].split(" ")))

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

        await ctx.send(f"{' '.join(time_text)} 후에 리마인더가 발송됩니다.")
        await set_timeout(seconds, ctx.send, f"{args.message[0]}")

        return

    return
