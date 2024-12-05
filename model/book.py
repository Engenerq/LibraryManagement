from dataclasses import dataclass, asdict, field
from uuid import uuid4, UUID


@dataclass
class BookCreate:
    """
    Создание книги
    """
    title: str
    author: str
    year: int
    status: str = "в наличии"
    id_book: UUID = field(default_factory=uuid4)

    def to_dict(self) -> dict[str, ...]:
        return asdict(self)


@dataclass
class BookDelete:
    """
    Удаление книги
    """
    id_book: str


@dataclass
class BookSearcher:
    """
    Поиск книги
    """
    title: str | None = None
    author: str | None = None
    year: int | None = None


@dataclass
class BookEditStatus:
    """
    Изменение статуса книги
    """
    id_book: str
    status: str
