import argparse

parser = argparse.ArgumentParser(description="Discord Reminder Bot", add_help=False)
parser.add_argument(
    "-h",
    "--help",
    action="store_true",
    dest="help",
    help="도움말을 출력합니다."
)
