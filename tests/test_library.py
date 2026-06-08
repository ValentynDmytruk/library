# library.py
from interfaces import Observer
from book import Book

class Library:
    _instance = None
    _observers = []

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Library, cls).__new__(cls, *args, **kwargs)
            cls._instance.books = []  # Список для збереження книг
        return cls._instance

    def attach(self, observer: Observer):
        """Реєстрація нового спостерігача"""
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer):
        """Видалення спостерігача зі списку"""
        if observer in self._observers:
            self._observers.remove(observer)

    def add_book(self, book: Book):
        """Додавання книги та автоматичне сповіщення всіх спостерігачів"""
        self.books.append(book)
        for observer in self._observers:
            observer.update(book.title)git add .