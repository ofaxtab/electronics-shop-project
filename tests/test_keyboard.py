import pytest

from src.keyboard import KeyBoard


def test_keyboard_creation():
    kb = KeyBoard('Dark Project KD87A', 9600, 5)

    assert str(kb) == "Dark Project KD87A"
    assert str(kb.language) == "EN"

    kb.change_lang()
    assert str(kb.language) == "RU"
    # Сделали RU -> EN -> RU
    kb.change_lang().change_lang()
    assert str(kb.language) == "RU"


def test_keyboard_error():
    kb = KeyBoard('Dark Project KD87A', 9600, 5)

    with pytest.raises(AttributeError) as err:
        kb.language = 'CH'
    assert err.value.args[0] == "property 'language' of 'KeyBoard' object has no setter"
