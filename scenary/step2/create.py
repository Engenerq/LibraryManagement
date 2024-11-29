from db import db
from model.book import Book
from scenary.base import BaseScenary


class StepCreate(BaseScenary):
    """
    Добавление книги: Пользователь вводит title, author и year,
    после чего книга добавляется в библиотеку с уникальным id и статусом “в наличии”.
    """

    def make_step(self):
        Book(
            title=self._set_title(),
            author=self._set_author(),
            year=self._set_year(),
        ).dump_file(db)

    def _set_title(self):
        while True:
            title = input("Введите Title: ")
            if input(f"Будет установлен {title=}[y]") == "y":
                return title

    def _set_author(self):
        while True:
            author = input("Введите Author: ")
            if input(f"Будет установлен {author=}[y]") == "y":
                return author

    def _set_year(self):
        while True:
            year = int(input("Введите Year: "))
            if input(f"Будет установлен {year=}[y]") == "y":
                return year
