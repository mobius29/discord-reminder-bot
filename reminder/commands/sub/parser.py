from ..parser import parser

sub_parser = parser.add_subparsers(
    dest="subcommand",
    help="리마인더 명령어를 입력하세요.",
)
