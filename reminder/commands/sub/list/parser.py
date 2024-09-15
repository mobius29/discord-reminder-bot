from ..parser import sub_parser

list_parser = sub_parser.add_parser(
    "list",
    help="리마인더 목록을 출력합니다.",
    add_help=False,
)

list_parser.add_argument(
    "-h",
    "--help",
    action="store_true",
    dest="_list_help",
    help="도움말을 출력합니다.",
)

list_parser.add_argument(
    "--author",
    dest="author",
    help="리마인더 목록을 출력할 사용자를 지정합니다.",
)
