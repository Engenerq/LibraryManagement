from db import WorkerJson
from scenary.base import BaseScenary


class StepAll(BaseScenary):
    """
    Отображение всех книг: выводит список всех книг с их id, title, author, year и status.
    """

    def make_step(self):
        WorkerJson().get_all_books()
