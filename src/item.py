import csv
import os

from src.exceptions import InstantiateCSVError

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    _csv_filename = 'items.csv'
    _csv_file_directory = os.path.join(f'..', 'src')


    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)



    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.name}"

    def __add__(self, other):
        if not issubclass(other.__class__, self.__class__):
            raise TypeError(f'Невозможно произвести сложение с объектом {other} класса {other.__class__}.')
        return self.quantity + other.quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if len(value) > 10:
            raise ValueError('Имя товара не может быть длиннее 10 символов')
        self.__name: str = value

    @classmethod
    def instantiate_from_csv(cls):
        try:
            with open(os.path.join(cls._csv_file_directory, cls._csv_filename),
                      'r', newline='') as csvfile:
                try:
                    data = csv.DictReader(csvfile)
                    for row in data:
                        cls(row['name'], row['price'], row['quantity'])
                except Exception:
                    raise InstantiateCSVError(f'Файл {cls._csv_filename} поврежден')

        except FileNotFoundError:
            raise FileNotFoundError(f'Отсутствует файл {cls._csv_filename}')

    @staticmethod
    def string_to_number(number: str) -> int:
        return int(float(number))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return float(self.price * self.quantity)

    def apply_discount(self):
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate
