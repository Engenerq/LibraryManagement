from db import WorkerJson
from model.book import BookEditStatus
from scenary.base import BaseScenary


class StepEdit(BaseScenary):
    """
    Изменение статуса книги:
    Пользователь вводит id книги и новый статус (“в наличии” или “выдана”).
    """

    def make_step(self):
        book = BookEditStatus(
            id_book=self._set_id_book(),
            status=self._set_status(),
        )
        WorkerJson().edit_status(book)

    def _set_id_book(self):
        """
        Установка параметра id
        """
        while True:
            id_book = input("Введите id: ")
            if input(f"Будет установлен {id_book=}[y] -> ") == "y":
                return id_book

    def _set_status(self):
        """
        Установка параметра status
        """
        while True:
            status = input("Введите Status: ")
            if input(f"Будет установлен {status=} [y] -> ") == "y":
                return status
