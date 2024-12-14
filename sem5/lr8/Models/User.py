from abc import ABC, abstractproperty


class User(ABC):
    """Абстрактный класс, определяющий базовые методы, 
    которые будет необходимо переопределить в дочерних классах"""

    @abstractproperty
    def get_name(self):
        pass
        
    @abstractproperty
    def show_name(self):
        pass
        
    @abstractproperty
    def get_fullname(self):
        pass