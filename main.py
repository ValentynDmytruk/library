# main.py
from library import Library
from book import Book
from user import Reader
from notifications import NotificationService


def main():
    print("=== Запуск модульної системи бібліотеки ===")

    # 1. Отримуємо синглтон бібліотеки
    lib = Library()

    # 2. Створюємо користувачів та сервіси
    valentin = Reader(101, "Валентин", "valentin@nuwm.edu.ua")
    email_notifier = NotificationService()

    # 3. Підписка спостерігачів
    lib.attach(valentin)
    lib.attach(email_notifier)
    print("Статус: Спостерігачі зареєстровані.")

    # 4. Демонстрація роботи подій
    new_book = Book("978-617-12-8114-1", "Чистий код", 5)
    lib.register_book(new_book)

    # 5. Демонстрація відписки
    print("\n--- [Відписка Валентина] ---")
    lib.detach(valentin)

    another_book = Book("978-0134494166", "Clean Architecture", 2)
    lib.register_book(another_book)


if __name__ == "__main__":
    main()