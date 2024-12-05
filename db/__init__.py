import json
from pathlib import Path
from pprint import pprint

from custom_types.lib_db import LibDB
from model.book import BookCreate, BookDelete, BookEditStatus, BookSearcher
from serialize.json import json_serialize


class WorkerJson:
    db = Path(__file__).parent.joinpath("db.json")

    def __init__(self):
        if self.db.exists() and self.db.stat().st_size > 0:
            self.data: LibDB = json.loads(self.db.read_text(encoding="utf-8"))
        else:
            self.data = {
                "index": {
                    "author": {},
                    "title": {},
                    "year": {},
                },
                "books": {},
            }
        self.index = self.data["index"]

    def _add_index(self, book: BookCreate) -> None:
        """
        Добавление индекса
        :param book: модель создания книги
        """
        for key in self.index:
            index_key = self.index[key]
            book_attr = getattr(book, key)
            lib_book = [book.id_book]
            try:
                index_key[str(book_attr)].extend(lib_book)
            except KeyError:
                index_key[book_attr] = lib_book

        self._save()

    def dump_file(self, book: BookCreate) -> None:
        """
        Сохранение добавленной книги
        :param book: модель создания книги
        """
        self._add_index(book)
        self.data["books"][str(book.id_book)] = book.to_dict()
        self._save()

    def delete_book(self, book: BookDelete) -> None:
        """
        Удаление книги
        :param book: модель удаления книги
        """
        id_book = str(book.id_book)
        try:

            delete_data = self.data["books"].pop(id_book)

            for key, value in self.index.items():
                value.pop(delete_data[key], None)

        except KeyError:
            print(f"Книги с {book.id_book} не существует")
            return

        self._save()

    def search_book(self, params: BookSearcher) -> None:
        """
        Поиск книги
        :param params: модель поиска книги
        """
        # поиск производиться на основе приходящих данных autor yaer id
        # по id мы вытаскиваем сразу из books
        # в остальных случаях мы лезем в index находим книгу(и) и выплевывем их

        if params.title:
            key = "title"

        elif params.author:
            key = "author"

        elif params.year:
            key = "year"

        else:
            raise AttributeError()

        books = self.index[key][str(getattr(params, key))]
        data_books = self.data["books"]
        data = [data_books[book] for book in books]
        pprint(data, indent=4)

    def get_all_books(self) -> None:
        """
        Выдать все книги
        """
        pprint(self.data["books"])

    def edit_status(self, book: BookEditStatus) -> None:
        """
        Изменить статус книги
        :param book: модель изменения статуса книги
        """
        self.data["books"][book.id_book]["status"] = book.status
        self._save()

    def _save(self) -> None:
        with self.db.open("w", encoding="utf-8") as file_write:
            json.dump(self.data,
                      file_write,
                      ensure_ascii=False,
                      indent=4,
                      default=json_serialize)


__all__ = ["WorkerJson"]
