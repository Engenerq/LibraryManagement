from db import WorkerJson
from model.book import BookCreate
from scenary.base import BaseScenary


class StepCreate(BaseScenary):
    """
    Добавление книги: Пользователь вводит title, author и year,
    после чего книга добавляется в библиотеку с уникальным id и статусом “в наличии”.
    """

    def make_step(self):
        book = BookCreate(
            title=self._set_title(),
            author=self._set_author(),
            year=self._set_year(),
        )
        WorkerJson().dump_file(book)

    def _set_title(self):
        """
        Установка параметра title
        """
        while True:
            title = input("Введите Title: ")
            if input(f"Будет установлен {title}[y] -> ") == "y":
                return title

    def _set_author(self):
        """
        Установка параметра author
        """
        while True:
            author = input("Введите Author: ")
            if input(f"Будет установлен {author} [y] -> ") == "y":
                return author

    def _set_year(self):
        """
        Установка параметра year
        """
        while True:
            year = int(input("Введите Year: "))
            if input(f"Будет установлен {year}[y] -> ") == "y":
                return year
