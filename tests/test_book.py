# tests/test_book.py
import unittest
import sys
import os

# Налаштування шляху для імпорту модулів із кореня проєкту
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from book import Book

class TestBook(unittest.TestCase):

    def setUp(self):
        """Ініціалізація об'єкта книги перед кожним тестом """
        self.book = Book("978-0134494166", "Clean Architecture", 3)

    def test_initial_state(self):
        """1. Перевірка правильності початкового стану нової книги """
        self.assertEqual(self.book.isbn, "978-0134494166")
        self.assertEqual(self.book.title, "Clean Architecture")
        self.assertEqual(self.book.available_copies, 3)

    def test_decrease_available_success(self):
        """2. Перевірка успішного зменшення кількості книг при видачі """
        self.book.decrease_available()
        self.assertEqual(self.book.available_copies, 2)

    def test_decrease_available_zero(self):
        """3. Перевірка обмеження: кількість копій не може стати меншою за 0 """
        self.book.available_copies = 0
        self.book.decrease_available()
        self.assertEqual(self.book.available_copies, 0)

    def test_increase_available(self):
        """4. Перевірка успішного збільшення доступних копій при поверненні книги"""
        self.book.increase_available()
        self.assertEqual(self.book.available_copies, 4)

    def test_multiple_operations(self):
        """5. Перевірка коректності серії послідовних операцій видачі та повернення """
        self.book.decrease_available()
        self.book.decrease_available()
        self.book.increase_available()
        self.assertEqual(self.book.available_copies, 2)

if __name__ == '__main__':
    unittest.main()




