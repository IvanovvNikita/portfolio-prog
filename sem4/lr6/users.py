import re
from datetime import datetime


class User():

    def __init__(self, id, height, name, deleted, created):
        self.__id = id
        self.__height = height
        self.__name = name
        self.__deleted = deleted
        self.__created = created

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise TypeError("ID должен быть целым числом")
        elif value < 0:
            raise ValueError("ID не может быть отрицательным")
        else:
            self.__id = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Рост должен быть числом")
        elif value <= 0:
            raise ValueError("Рост должен быть положительным")
        else:
            self.__height = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Имя не может быть пустым")
        elif re.match(r"^\d", value):
            raise ValueError("Имя не должно начинаться с цифры")
        else:
            self.__name = value

    @property
    def deleted(self):
        return self.__deleted

    @deleted.setter
    def deleted(self, value):
        if not isinstance(value, bool):
            raise TypeError("Флаг удаления должен быть логическим значением")
        else:
            self.__deleted = value

    @property
    def created(self):
        return self.__created

    @created.setter
    def created(self, value):
        self.__created = value

    def tuple(self):
        return (
            self.__id,
            self.__name,
            self.__height,
            self.__deleted,
            self.__created
        )


if __name__ == '__main__':
    print(__doc__)

    u1 = User(1, 1.72, 'Nikita', False, '10-05-2023 17:44:25')

    print(u1)
