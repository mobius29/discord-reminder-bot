from ..parser import sub_parser

remove_parser = sub_parser.add_parser(
    "remove",
    help="리마인더를 제거합니다.",
    add_help=False,
)

remove_parser.add_argument(
    "-h",
    "--help",
    action="store_true",
    dest="_remove_help",
    help="도움말을 출력합니다.",
)

remove_parser.add_argument(
    "-a",
    "--all",
    action="store_true",
    dest="all",
    help="본인이 설정한 모든 리마인더를 제거합니다.",
)
