from typing import TypedDict


class Reminder(TypedDict):
    page_id: str
    id: int
    creator: str
    message: str
    date: str
