from typing import TypedDict
from uuid import UUID


class BookDB(TypedDict):
    id: UUID
    title: str
    author: str
    year: int
    status: bool


class LibDB(TypedDict):
    books: list[BookDB]
