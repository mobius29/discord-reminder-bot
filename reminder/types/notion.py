from typing import Literal, TypedDict


class Sort(TypedDict):
    property: str
    direction: Literal["ascending", "descending"]
