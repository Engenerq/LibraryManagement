from model.book import Book


class CRUDBook:
    def __init__(self):
        ...

    def add_book(self, title: str, author: str, year: int):
        new_book = Book(
            title=title,
            author=author,
            year=year,
        )

    def delete_book(self):
        ...

    def search_book(self):
        ...

    def update_book_status(self):
        ...

    def display_book(self):
        ...

