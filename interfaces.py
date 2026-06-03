from abc import ABC, abstractmethod

# Інтерфейс для отримання сповіщень про події в системі
class Observer(ABC):
    @abstractmethod
    def update(self, book_title: str) -> None:
        """Метод, який викликається суб'єктом для сповіщення"""
        pass

# Інтерфейс для об'єктів, що генерують події (Суб'єкт)
class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """Реєстрація нового спостерігача"""
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """Видалення спостерігача зі списку"""
        pass

    @abstractmethod
    def notify(self, book_title: str) -> None:
        """Сповіщення всіх підписаних об'єктів"""
        pass