from interfaces import Observer

class User:
    def __init__(self, user_id: int, name: str, email: str):
        self.user_id = user_id
        self.name = name
        self.email = email

class Reader(User, Observer):
    def update(self, book_title: str) -> None:
        print(f"[Reader UI] {self.name}, гарна новина! У бібліотеці з'явилася книга: '{book_title}'")