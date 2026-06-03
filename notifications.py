from interfaces import Observer

class NotificationService(Observer):
    def update(self, book_title: str) -> None:
        print(f"[Email Service] Надсилаємо лист: До каталогу додано книгу '{book_title}'")