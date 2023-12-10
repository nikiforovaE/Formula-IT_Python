from typing import Union


class BankAccount:
    def __init__(self, number: int, amount: Union[int, float] = 0):

        """
        Создание и подготовка к работе объекта "Банковский счет"

        :param number: Номер банковского счета
        :param amount: Сумма денег на счету

        Примеры:
        >>> bank_account = BankAccount(12345, 100)  # инициализация экземпляра класса

        """
        if not isinstance(number, int):
            raise TypeError("Номер банковского счета должен быть целым числом")
        if not isinstance(amount, Union[int, float]):
            raise TypeError("Сумма денег на счету должна быть числом")

        self.number = number
        self.amount = amount

    def put_money(self, amount: Union[int, float]):
        """
        Положить деньги на счет

        :param amout: Сумма денег, которую хотим положить на счет

        :raise ValueError: Если сумма денег, которую хотим положить на счет отрицательна или равна нулю,
         то вызываем ошибку

        Примеры:
        >>> bank_account = BankAccount(12345, 100)
        >>> bank_account.put_money(200)
        """
        if not isinstance(amount, Union[int, float]):
            raise TypeError("Сумма денег должна быть числом")
        if amount <= 0:
            raise ValueError("Положить на счет можно только положительную сумму денег")
        ...

    def get_amount(self) -> Union[int, float]:
        """
        Функция, которая возвращает сумму денег на счету

        :return: Сумма денег на счету

        Примеры:
        >>> bank_account = BankAccount(12345, 100)
        >>> bank_account.get_amount()
        """
        ...


class Box:

    def __init__(self, material: str, capacity: int, count_of_things: int = 0):
        """
        Создание и подготовка к работе объекта "Коробка"

        :param capacity: Максимальное количество вмещаемых в коробку вещей
        :param count_of_things: Количество вещей в коробке

        Примеры:
        >>> box = Box("Картон", 10, 1)  # инициализация экземпляра класса
        """
        if not isinstance(material, str):
            raise TypeError("Материал должен быть строкой")
        if not isinstance(capacity, int):
            raise TypeError("Максимальное количество вмещаемых вещей должено быть целым числом")
        if not isinstance(count_of_things, int):
            raise TypeError("Количество вещей в коробке должно быть целым числом")
        if count_of_things > capacity:
            raise ValueError(
                "Количество вещей в коробке не может быть больше максимального вместимого количества вещей")
        self.material = material
        self.capacity = capacity
        self.count_of_things = count_of_things

    def get_count_of_things(self) -> int:
        """
        Функция которая возващает сколько вещей лежит в коробке

        :return: Сколько вещей в коробке

        Примеры:
        >>> box = Box("Картон", 10, 1)
        >>> box.get_count_of_things()
        """
        ...

    def put_thing(self, count: int) -> None:
        """
        Добавление вещи в коробку.
        :param count: Количество вещей, которое кладем в коробку

        :raise ValueError: Если количество добавляемых вещей превышает свободное место в коробке, то вызываем ошибку

        Примеры:
        >>> box = Box("Картон", 10, 1)
        >>> box.put_thing(2)
        """
        if not isinstance(count, int):
            raise TypeError("Количество вещей которые можно положить в коробку должно быть целым числом")
        if self.count_of_things + count > self.capacity:
            raise ValueError(
                "Количество вещей в коробке не может быть больше максимального вместимого количества вещей")
        ...

    def get_thing(self, count: int) -> None:
        """
        Извлечение вещей из коробки.

        :param count: Количество извлекаемых вещей из коробки
        :raise ValueError: Если количество извлекаемых вещей превышает количество вещей в коробке,
        то возвращается ошибка.

        Примеры:
        >>> box = Box("Картон", 10, 1)
        >>> box.get_thing(1)
        """
        if not isinstance(count, int):
            raise TypeError("Количество извлекаемых вещей должно быть целым числом")
        if count > self.count_of_things:
            raise ValueError("Невозможно достать вещей из коробки больше, чем в ней находится")
        ...


class Notebook:
    def __init__(self, pages: int, covered_pages: int = 0):
        """
        Создание и подготовка к работе объекта "Блокнот"

        :param pages: Количество страниц в блокноте
        :param covered_pages: Количество исписанных страниц в блокноте

        Примеры:
        >>> notebook = Notebook(48, 2)  # инициализация экземпляра класса
        """
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if not isinstance(covered_pages, int):
            raise TypeError("Количество исписанных страниц должно быть целым числом")
        if covered_pages > pages:
            raise ValueError("Количество исписанных страниц не может быть больше общего количества страниц")
        self.pages = pages
        self.covered_pages = covered_pages

    def write_pages(self, count_pages: int) -> None:
        """
        Функция, которая позволяет исписать страницу
        :param count_pages: Количество страниц, которые нужно исписать

        :raise ValueError: Если количество страниц, которые нужно исписать превышает свободное место в блокноте,
        то вызываем ошибку

        Примеры:
        >>> notebook = Notebook(48, 2)
        >>> notebook.write_pages(5)
        """
        if not isinstance(count_pages, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if count_pages > self.pages - self.covered_pages:
            raise ValueError("В блокноте нет столько свободных страниц")
        ...

    def tear_away_pages(self, count_pages: int) -> None:
        """
        Функция вырывания страниц из блокнота

        :param count_pages: Количество страниц, которые нужно вырвать

        :raise ValueError: Если количество страниц, которые нужно вырвать превышает количествос страниц в блокноте,
        то вызываем ошибку

        Примеры:
        >>> notebook = Notebook(48, 2)
        >>> notebook.tear_away_pages(1)
        """
        if not isinstance(count_pages, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if count_pages > self.pages:
            raise ValueError("В блокноте нет столько страниц")
        ...

    def get_count_of_available_ages(self) -> int:
        """
        Функция, возвращающая количество свободных страниц

        :return: Количество свободных страниц

        Примеры:
        >>> notebook = Notebook(48, 2)
        >>> notebook.tear_away_pages(2)
        """
        ...


if __name__ == "__main__":
    import doctest

    doctest.testmod()
