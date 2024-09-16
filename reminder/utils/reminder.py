from prettytable import PrettyTable

from reminder.types.reminder import Reminder


def make_reminder_table(reminders: list[Reminder]) -> str:
    table = PrettyTable()
    table.field_names = ["ID", "날짜", "메시지"]

    for reminder in reminders:
        table.add_row([reminder["id"], reminder["date"], reminder["message"]])

    return f"```\n{table}\n```"
