class Book:
    def __init__(self, title, author, read=False):
        self.__title = title
        self.__author = author
        self.__read = read

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def read(self):
        return self.__read

    def mark_read(self):
        self.__read = True

    def info(self):
        return f"Title: {self.title} | author: {self.author} | status: {self.read}"


class Library:
    def __init__(self, books=None):
        if books is None:
            books = []
        self.__books = books

    @property
    def books(self):
        return self.__books

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        return "All books:\n" + "\n".join([book.info() for book in self.books])

    def show_unread(self):
        return "Unread books:\n" + "\n".join(
            [book.info() for book in self.books if not book.read]
        )


if __name__ == "__main__":
    my_book = Book("War and Peace", "Leo Tolstoy")
    my_library = Library()
    my_library.add_book(my_book)
    my_book.mark_read()
    print(my_library.show_books())
    print(my_library.show_unread())
