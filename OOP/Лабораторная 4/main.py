class Car:
    """
    Базовый класс автомобиля
    """

    def __init__(self, brand: str, number: int):
        """
        Конструктор класса Car
        :param brand: Марка автомобиля,
        :param number: Номер автомобиля
        """
        if not isinstance(brand, str):
            raise TypeError("Марка авто должна быть строкой")
        if not isinstance(number, int):
            raise TypeError("Номер авто должен быть числом")
        self.is_correct_number(number)
        self._brand = brand
        self._number = number
        self._fuel = 100

    @staticmethod
    def is_correct_number(number: int):
        """
        Метод проверки корректности номера автомобиля
        :param number: Предполагаемый номер автомобиля
        :return:
        """
        if number <= 0 or len(str(number)) != 3:
            raise ValueError("Номер авто должен быть трехзначным положительным числом")

    @property
    def brand(self) -> str:
        return self._brand

    @property
    def number(self) -> int:
        return self._number

    def __str__(self):
        return f'Автомобиль марки {self.brand} с номером {self.number}'

    def __repr__(self):
        return f'Car({self.brand!r}, {self.number})'

    def change_number(self, new_number: int) -> None:
        """
        Метод изменения номера автомобиля
        :param new_number: Новый номер автомобиля
        :return:
        """
        self.is_correct_number(new_number)
        self._number = new_number

    def drive(self, km: float) -> str:
        """
        Метод, имитирующий поездку на автомобиле.
        Уменьшает аргумент - количество топлива исходя из дистанции

        :param km: Пройденное расстояние в километрах
        :return: Сообщение о пройденном расстроянии и запас хода
        """
        ...


class Truck(Car):
    """
    Класс рузовых автомобилей - Truck, наследуемый от класса Car
    """

    def __init__(self, brand: str, number: int, lifting_capacity: float):
        """
        Конструктор класса Truck
        :param brand: Марка грузовика
        :param number: Номер грузовика
        :param lifting_capacity: Грузоподъемность грузовика
        """
        super().__init__(brand, number)
        self.lifting_capacity = lifting_capacity

    def __str__(self):
        return super().__str__() + f' - грузовой, грузоподъемность = {self.lifting_capacity}'

    def __repr__(self):
        return f'Truck({self.brand!r}, {self.number}, {self.lifting_capacity})'

    def drive(self, km: int) -> str:
        """
        Перегружаемый метод drive
        Уменьшает аргумент - количество топлива исходя из дистанции и массы грузовика
        Перегрузка необходима для учета массы грузовика в расходе топлива
        :param km:  Пройденное расстояние в километрах
        :return: Сообщение о пройденном расстроянии и запас хода
        """


if __name__ == "__main__":
    car = Car("TOYOTA", 777)
    print(car)
    print(repr(car))
    car.change_number(767)
    print(car)

    print()
    truck = Truck("Volvo", 666, 3000)
    print(truck)
    print(repr(truck))
    truck.change_number(888)
    print(truck)
