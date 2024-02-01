from typing import Union


class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError
        self._name = name

    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, author: str) -> None:
        if not isinstance(author, str):
            raise TypeError
        self._author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, pages: int) -> None:
        if not isinstance(pages, int):
            raise TypeError
        if pages <= 0:
            raise ValueError
        self._pages = pages

    def __str__(self):
        return f'{super().__str__()}. Количество страниц {self.pages}'

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> Union[int, float]:
        return self._duration

    @duration.setter
    def duration(self, duration: Union[int, float]) -> None:
        if not isinstance(duration, (int, float)):
            raise TypeError
        if duration <= 0:
            raise ValueError
        self._duration = duration

    def __str__(self):
        return f'{super().__str__()}. Длительность {self.duration}'

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"


paper_book = PaperBook("abc", "Smith", 30)
print(paper_book)
print(repr(paper_book))
paper_book2 = PaperBook(name='abc', author='Smith', pages=30)
print(paper_book2)
print()

audio_book = AudioBook("def", "Jones", 50.6)
print(audio_book)
print(repr(audio_book))
audio_book2 = AudioBook(name='def', author='Jones', duration=50.6)
print(audio_book2)
