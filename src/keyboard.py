from src.item import Item


class MixinKeyboard:
    def __init__(self, name: str, price: float, quantity: int, language: str):
        super().__init__(name, price, quantity)
        self._language = language

    def change_lang(self):
        if self._language == 'RU':
            self._language = 'EN'
        else:
            self._language = 'RU'
        return self

    @property
    def language(self):
        return self._language

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if len(value) > 20:
            raise ValueError('Имя товара не может быть длиннее 20 символов')
        self.__name: str = value




class KeyBoard(MixinKeyboard, Item):
    def __init__(self, name: str, price: float, quantity: int, language: str = 'EN'):
        super().__init__(name, price, quantity, language)
