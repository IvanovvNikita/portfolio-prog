from .User import User


class IvanovNikita(User):

    def __init__(self):
        self.__second_name = "Иванов"
        self.__first_name = "Никита"
        self.__fathers_name = "Русланович"
        self.__favorite_movie = "1+1"
    def get_name(self):
        return self.__first_name

    def get_second_name(self):
        return self.__second_name
        
    def show_name(self):
        print(
            f"{self.__second_name} {self.__first_name} {self.__fathers_name}")
        
    def get_favorite_movie(self):
        return self.__favorite_movie
    
    def get_fullname(self):
        return {
            'second_name': self.__second_name,
            'first_name': self.__first_name,
            'fathers_name': self.__fathers_name
        }