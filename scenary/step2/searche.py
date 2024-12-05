from scenary.base import BaseScenary
from scenary.step3.searche import SearchTitle, SearchAuthor, SearchYear


class StepSearcher(BaseScenary):
    """
    Поиск книги:
    Пользователь может искать книги по title, author или year.
    """
    naming = {
        "1": "title",
        "2": "author",
        "3": "year",
    }

    def make_step(self):
        input_param_search = input((
            "Выберите один параметр для поиска:\n"
            "\t[1] title\n"
            "\t[2] author\n"
            "\t[3] year\n"
            "-> ")
        )

        if input(f"Ищем по {self.naming.get(input_param_search, input_param_search)} [y] -> ") != "y":
            return self
        match input_param_search:
            case "title" | "1":
                return SearchTitle()
            case "author" | "2":
                return SearchAuthor()
            case "year" | "3":
                return SearchYear()
            case _:
                print(f"{self.naming.get(input_param_search, input_param_search)} такого параметра нет")
                return self
