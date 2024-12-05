from db import WorkerJson
from model.book import BookDelete
from scenary.base import BaseScenary


class StepDelete(BaseScenary):
    """
    Удаление книги: Пользователь вводит id книги, которую нужно удалить.
    """

    def make_step(self):
        book = BookDelete(
            id_book=self._set_id()
        )
        WorkerJson().delete_book(book)

    def _set_id(self):
        """
        Установка параметра id
        """
        while True:
            id_book = input("Введите Id: ")
            if input(f"Будет установлен {id_book=} [y] -> ") == "y":
                return id_book
