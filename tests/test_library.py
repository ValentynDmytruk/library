import unittest
from unittest.mock import Mock, patch
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from library import Library
from book import Book
from interfaces import Observer


class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.library = Library()
        self.mock_observer1 = Mock(spec=Observer)
        self.mock_observer2 = Mock(spec=Observer)
        self.book = Book("978-0134494166", "Clean Architecture", 3)

    def tearDown(self):
        Library._instance = None
        if hasattr(Library, '_observers'):
            Library._observers = []

    def test_singleton_instance(self):
        library_second_call = Library()
        self.assertIs(self.library, library_second_call)

    def test_attach_observer(self):
        self.library.attach(self.mock_observer1)
        self.assertIn(self.mock_observer1, self.library._observers)

    def test_detach_observer(self):
        self.library.attach(self.mock_observer1)
        self.library.detach(self.mock_observer1)
        self.assertNotIn(self.mock_observer1, self.library._observers)

    @patch('builtins.print')
    def test_add_book_notifies_observers(self, mock_print):
        self.library.attach(self.mock_observer1)
        self.library.attach(self.mock_observer2)

        self.library.add_book(self.book)

        self.assertIn(self.book, self.library.books)
        self.mock_observer1.update.assert_called_once_with("Clean Architecture")
        self.mock_observer2.update.assert_called_once_with("Clean Architecture")


if __name__ == '__main__':
    unittest.main()
