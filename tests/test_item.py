"""Здесь надо написать тесты с использованием pytest для модуля item."""
import os

import pytest

from src.item import Item
from src.exceptions import InstantiateCSVError


def test_item_creation():
    instance = Item("Смартфон", 10000, 20)
    assert instance.name == "Смартфон"
    assert instance.price == 10000
    assert instance.quantity == 20


def test_calculate_total_price():
    instance = Item("Телефон", 900, 10)
    assert isinstance(instance.calculate_total_price(), float) is True
    assert instance.calculate_total_price() == 9000


def test_apply_discount():
    instance = Item("Смартфон", 10000, 20)
    assert instance.pay_rate == 1.0

    Item.pay_rate = 0.7
    instance.apply_discount()
    assert instance.pay_rate == 0.7
    assert instance.price == 7000


def test_repr():
    item = Item('Смартфон', 900, 5)
    assert repr(item) == "Item('Смартфон', 900, 5)"


def test_str():
    item = Item('Смартфон', 900, 5)
    assert str(item) == 'Смартфон'


def test_name_setter_error():
    with pytest.raises(ValueError) as err:
        Item('СуперСмартфон', 900, 5)
    assert 'Имя товара не может быть длиннее 10 символов' == err.value.args[0]


def test_instantiate_from_csv():
    Item.all = []
    Item.instantiate_from_csv()
    assert len(Item.all) == 5

    with pytest.raises(FileNotFoundError) as err:
        Item._csv_filename = 'file-is-not-exists.csv'
        Item.instantiate_from_csv()
    assert err.value.args[0] == 'Отсутствует файл file-is-not-exists.csv'

    with pytest.raises(InstantiateCSVError) as err:
        Item._csv_filename = 'broken-file.csv'
        Item._csv_file_directory = os.path.join('..', 'tests', 'testfiles')
        Item.instantiate_from_csv()
    assert err.value.args[0] == 'Файл broken-file.csv поврежден'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_add_raises():
    item = Item('Смартфон', 900, 5)
    with pytest.raises(TypeError) as err:
        item + 9
    assert err.value.args[0] == "Невозможно произвести сложение с объектом 9 класса <class 'int'>."
