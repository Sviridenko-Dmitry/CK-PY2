if __name__ == "__main__":
    class OnlineStore:
        """ Базовый класс интернет-магазина. """
        def __init__(self, type_company: str, industry: str):
            self._type_company = type_company
            self._industry = industry

        @property
        def type_company(self) -> str:
            """ Возвращает тип компании. """
            return self._type_company

        @property
        def industry(self) -> str:
            """ Возвращает отрасль компании. """
            return self._industry

        def is_public_company(self, public_company: str) -> bool:
            """ Проверяет, является ли компания интернет-магазина частной. """
            if not isinstance(public_company, str):
                raise TypeError("Тип компании должен быть типа str")
            return self.type_company == public_company

        def __eq__(self, other) -> bool:
            """ Сравнивает текущий объект с передаваемым. """
            return self.type_company == other.type_company and self.industry == other.industry

        def __str__(self):
            """ Определяет поведение метода str(), вызванного от экземпляра класса OnlineStore. """
            return f"Компания {self.type_company}. Отрасль {self.industry}"

        def __repr__(self):
            """ Определяет поведение метода repr(), вызванного от экземпляра класса OnlineStore. """
            return f"{self.__class__.__name__}(type_company={self.type_company!r}, industry={self.industry!r})"


    class Wildberries(OnlineStore):
        """ Дочерний класс интернет-магазин Wildberries. """
        def __init__(self, type_company: str, industry: str, discount: int):
            super().__init__(type_company, industry)
            self.discount = discount

        @property
        def discount(self) -> int:
            """ Возвращает значение скидки. """
            return self._discount

        @discount.setter
        def discount(self, new_discount: int) -> None:
            """ Устанавливает значение скидки. """
            if not isinstance(new_discount, int):
                raise TypeError("Скидка должна быть типа int")
            if new_discount <= 0 or new_discount >= 27:
                raise ValueError("Скидка должна быть положительным числом и меньше 27 согласно условиям магазина")
            self._discount = new_discount

        def __eq__(self, other) -> bool:
            """ Сравнивает текущий объект с передаваемым.
            Данный метод перегружается, потому что появляются новые атрибуты класса. """
            return self.type_company == other.type_company and self.industry == other.industry and \
                self.discount == other.discount

        def __repr__(self):
            """ Определяет поведение метода repr(), вызванного от экземпляра класса Wildberries.
            Перегружаем метод, поскольку в данном дочернем классе расширился конструктор базового класса.
            Требуется дополнить информацию о добавленных атрибутах"""
            return f"{self.__class__.__name__}(type_company={self.type_company!r}, industry={self.industry!r}, " \
                f"discount={self.discount!r})"


    class OZON(OnlineStore):
        """ Дочерний класс интернет-магазин OZON. """
        def __init__(self, type_company: str, industry: str, points: int):
            super().__init__(type_company, industry)
            self.points = points

        @property
        def points(self) -> int:
            """ Возвращает количество баллов. """
            return self._points

        @points.setter
        def points(self, new_points: int) -> None:
            """ Устанавливает количество баллов. """
            if not isinstance(new_points, int):
                raise TypeError("Количество баллов должно быть типа int")
            if new_points <= 0:
                raise ValueError("Количество баллов должно быть положительным числом")
            self._points = new_points

        def __eq__(self, other) -> bool:
            """ Сравнивает текущий объект с передаваемым.
            Данный метод перегружается, потому что появляются новые атрибуты класса. """
            return self.type_company == other.type_company and self.industry == other.industry and \
                self.points == other.points

        def __repr__(self):
            """ Определяет поведение метода repr(), вызванного от экземпляра класса OZON.
            Перегружаем метод, поскольку в данном дочернем классе расширился конструктор базового класса.
            Требуется дополнить информацию о добавленных атрибутах"""
            return f"{self.__class__.__name__}(type_company={self.type_company!r}, industry={self.industry!r}, " \
                f"points={self.points!r})"
    pass
# Задание выполнено
