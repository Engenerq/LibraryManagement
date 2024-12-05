from db import WorkerJson
from model.book import BookSearcher
from scenary.base import BaseScenary


class SearchTitle(BaseScenary):

    def make_step(self):
        param = BookSearcher(
            **self._set_title()
        )
        WorkerJson().search_book(param)

    def _set_title(self):
        """
        Установка параметра title
        """
        while True:
            title = input("Введите title: ")
            if input(f"Будет установлен {title}[y] -> ") == "y":
                return {
                    "title": title,
                }


class SearchAuthor(BaseScenary):

    def make_step(self):
        param = BookSearcher(
            **self._set_author()
        )
        WorkerJson().search_book(param)

    def _set_author(self):
        """
        Установка параметра author
        """
        while True:
            author = input("Введите Author: ")
            if input(f"Будет установлен {author} [y] -> ") == "y":
                return {
                    "author": author,
                }


class SearchYear(BaseScenary):

    def make_step(self):
        param = BookSearcher(
            **self._set_year()
        )
        WorkerJson().search_book(param)

    def _set_year(self):
        """
        Установка параметра year
        """
        while True:
            year = input("Введите Year: ")
            if input(f"Будет установлен {year} [y] -> ") == "y":
                return {
                    "year": year,
                }
