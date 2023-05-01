import pytest

from src.phone import Phone
from src.item import Item

def test_phone_create():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    assert phone.name == "iPhone 14"
    assert phone.price == 120_000
    assert phone.quantity == 5
    assert phone.number_of_sim == 2


def test_pohone_str():
    phone = Phone("iPhone 13", 100_000, 2, 1)
    assert str(phone) == 'iPhone 13'


def test_phone_repr():
    phone = Phone("iPhone 13", 100_000, 2, 1)
    assert repr(phone) == "Phone('iPhone 13', 100000, 2, 1)"

def test_phone_add():
    phone1 = Phone("iPhone 13", 100_000, 5, 1)
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10

def test_phone_set_sim_number():
    phone1 = Phone("iPhone 13", 100_000, 5, 1)
    phone1.number_of_sim = 2
    assert phone1.number_of_sim == 2

    with pytest.raises(ValueError) as err:
        phone1.number_of_sim = 0
    assert err.value.args[0] == 'Количество физических SIM-карт должно быть целым числом больше нуля.'