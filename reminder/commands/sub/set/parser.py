from ..parser import sub_parser

set_parser = sub_parser.add_parser(
    "set",
    help="리마인더를 설정합니다.",
    add_help=False,
)

set_parser.add_argument(
    "-h",
    "--help",
    action="store_true",
    dest="_set_help",
    help="도움말을 출력합니다.",
)

set_parser.add_argument(
    "-m",
    "--message",
    dest="message",
    nargs="+",
    help="리마인더 메시지를 입력하세요.",
)

set_parser.add_argument(
    "-w",
    "--week",
    dest="week",
    nargs="+",
    help="요일을 설정합니다. 기본적으로 모든 평일로 설정합니다.",
)

set_parser.add_argument(
    "-d",
    "--date",
    dest="date",
    nargs="+",
    help="날짜를 설정합니다. 기본적으로 오늘로 설정합니다.",
)

set_parser.add_argument(
    "-t",
    "--time",
    dest="time",
    nargs="+",
    help="시간을 설정합니다. 기본적으로 09:00:00로 설정합니다.",
)
set_parser.add_argument(
    "--after",
    dest="after",
    nargs="+",
    help="리마인더를 설정한 시간 이후로 설정합니다. 이는 다른 시간 설정과 함께 사용할 수 없습니다.",
)
