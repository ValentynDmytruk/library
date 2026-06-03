from interfaces import Subject, Observer
from book import Book

class Library(Subject):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._observers = []
            cls._instance.books = []
        return cls._instance

    def attach(self, observer: Observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, book_title: str):
        for obs in self._observers:
            obs.update(book_title)

    def register_book(self, book: Book):
        self.books.append(book)
        print(f"\n--- [Система]: Книгу '{book.title}' успішно додано ---")
        self.notify(book.title)