import doctest
import string


class Phone:
    def __init__(self, number: int, volume: int):
        """
        Создание и подготовка к работе объекта "Телефон"
        :param number: Номер телефона
        :param volume: Громкость воспроизведения звука в процентах
        Примеры:
        >>> phone = Phone(79288369254, 50)  # инициализация экземпляра класса
        """
        if not isinstance(volume, int):
            raise TypeError("Громкость звука должна быть типа int")
        if volume <= 0 or volume >= 100:
            raise ValueError("Громкость может принимать только значения от 0 до 100")
        self.volume = volume

        if not isinstance(number, int):
            raise TypeError("Номер телефона должен быть типа int")
        if number < 0 or number > 100000000000:
            raise ValueError("Номер телефона должен быть в пределах от 0 до 100000000000")
        self.number = number

    def call(self, number) -> bool:
        """
        Функция, которая осуществляет звонок на другой номер
        :param  number: Номер, на который будет осуществляться звонок
        :raise ValueError: Если номер телефона звонящего и адресата совпадают, то вызываем ошибку
        :return: Удалось ли осуществить звонок
        Примеры:
        >>> phone = Phone(79288369254, 50)
        >>> phone.call(76488639291)
        """
        if number == self.number:
            raise ValueError("Нельзя позвонить на свой же номер")
        if not isinstance(number, int):
            raise TypeError("Номер телефона должен быть типа int")
        if number < 0 or number > 100000000000:
            raise ValueError("Номер телефона должен быть в пределах от 0 до 100000000000")
        ...

    def add_volume(self, added_volume: int) -> int:
        """
        Функция добавления громкости в телефоне.
        :param added_volume: Значение в процентах добавляемой громкости
        :raise ValueError: Если в итоге громкость на телефоне превышает 100, то возвращается ошибка
        :return: Новая громкость на телефоне
        Примеры:
        >>> phone = Phone(79288369254, 50)
        >>> phone.add_volume(10)
        """
        if not isinstance(added_volume, int):
            raise TypeError("Добавляемая громкость должна быть типа int")
        if added_volume < 0:
            raise ValueError("Добавляемая громкость должна быть положительным числом")
        if added_volume + self.volume > 100:
            raise ValueError("Суммарная громкость не должна превышать 100")
        ...

    def turn_down_the_volume(self, reduced_volume: int) -> int:
        """
        Функция убавления громкости в телефоне.
        :param reduced_volume: Значение в процентах убавляемой громкости
        :raise ValueError: Если итоговая громкость на телефоне меньше 0, то возвращается ошибка
        :return: Новая громкость на телефоне
        Примеры:
        >>> phone = Phone(79288369254, 50)
        >>> phone.turn_down_the_volume(20)
        """
        if not isinstance(reduced_volume, int):
            raise TypeError("Уменьшаемая громкость должна быть типа int")
        if reduced_volume < 0:
            raise ValueError("Уменьшаемая громкость должна быть положительным числом")
        if self.volume - reduced_volume < 0:
            raise ValueError("Итоговая громкость не должна быть меньше 0")
        ...


class Film:
    def __init__(self, duration_film: int, current_minute_film: int, is_pause_film: bool):
        """
        Создание и подготовка к работе объекта "Фильм"
        :param duration_film: Продолжительность фильма в минутах
        :param current_minute_film: Данная минута в фильме
        :param is_pause_film: Пауза фильма
        Примеры:
        >>> film = Film(120, 50, False)  # инициализация экземпляра класса
        """
        if not isinstance(duration_film, int):
            raise TypeError("Продолжительность фильма должна быть типа int")
        if duration_film <= 0:
            raise ValueError("Продолжительность фильма должна быть положительным числом")
        self.duration_film = duration_film

        if not isinstance(current_minute_film, int):
            raise TypeError("Данная минута в фильме должна быть типа int")
        if current_minute_film <= 0:
            raise ValueError("Данная минута в фильме должна быть положительным числом")
        if current_minute_film > duration_film:
            raise ValueError("Данная минута фильма не может быть больше продолжительности фильма")
        self.current_minute_film = current_minute_film

        self.is_pause_film = is_pause_film

    def is_film_stop(self) -> bool:
        """
        Функция которая проверяет поставлен ли фильм на паузу
        :return: Стоит ли фильм на паузе или нет
        Примеры:
        >>> film = Film(120, 50, False)
        >>> film.is_film_stop()
        """
        ...

    def fast_forward_film(self, added_duration: int) -> int:
        """
        Функция перематывания фильма вперёд
        :param added_duration: Значение в минутах добавляемого времени
        :raise ValueError: Если количество добавляемых минут превышает продолжительность фильма, то вызываем ошибку
        :return: Данная минута в фильме после перемотки
        Примеры:
        >>> film = Film(120, 50, False)
        >>> film.fast_forward_film(30)
        """
        if not isinstance(added_duration, int):
            raise TypeError("Добавляемое время должно быть типа int")
        if added_duration < 0:
            raise ValueError("Добавляемое время должно быть положительным числом")
        ...


class Book:
    def __init__(self, number_of_pages: int, current_page: int):
        """
        Создание и подготовка к работе объекта "Книга"
        :param number_of_pages: Количестов страниц в книге
        :param current_page: Страница, на которой остановились
        Примеры:
        >>> book = Book(103, 1)  # инициализация экземпляра класса
        """
        if not isinstance(number_of_pages, int):
            raise TypeError("Количество страниц в книге должно быть типа int")
        self.number_of_pages = number_of_pages

        if not isinstance(current_page, int):
            raise TypeError("Страница, на которой остановились должна быть типа int")
        if current_page <= 0 or current_page > number_of_pages:
            raise ValueError("Страница, на которой остановились должна быть в пределах страниц книги")
        self.current_page = current_page

    def open_page(self, need_page: int) -> string:
        """
        Функция, которая открыввает страницу в книге
        :param need_page: Страница, которую  нужно открыть
        :raise ValueError: Если таокй страницы нет в книге, то возвращается ошибка
        :return: Содержимое страницы
        Примеры:
        >>> book = Book(103, 1)
        >>> book.open_page(3)
        """
        if not isinstance(need_page, int):
            raise TypeError("Страница должна быть типа int")
        if need_page < 1 or need_page > self.number_of_pages:
            raise ValueError("Страница, которую хотите открыть должна быть в пределах страниц книги")
        ...

    def volume_of_the_book(self) -> int:
        """
        Определение объёма книги.
        :return: Количество слов в книге
        Примеры:
        >>> book = Book(103, 1)
        >>> book.volume_of_the_book()
        """
        ...

    def turn_the_page(self) -> None:
        """
        Перелестнуть страницу.
        :raise ValueError: Если следующей страницы нет, то возвращается ошибка
        Примеры:
        >>> book = Book(103, 1)
        >>> book.turn_the_page()
        """
        if self.current_page + 1 > self.number_of_pages:
            raise ValueError("Достигнут конец книги")
        ...


if __name__ == "__main__":
    doctest.testmod()
# Задание выполнено
