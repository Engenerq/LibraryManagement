from typing import TypedDict
from uuid import UUID


class BookDB(TypedDict):
    """
    Типизация книги
    """
    id_book: UUID
    title: str
    author: str
    year: int
    status: bool


class LibDB(TypedDict):
    """
    Типизация библиотеки
    """
    index: dict[str, dict[str, list[UUID]]]
    books: dict[UUID, BookDB]
