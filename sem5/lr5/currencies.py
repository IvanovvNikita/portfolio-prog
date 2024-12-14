from datetime import datetime
from decimal import Decimal

import requests


class CurrenciesLst():

    """
    Класс для работы с курсами валют.
    Методы:
    - get_currencies(): Получает курсы валют с сайта Центрального Банка России.
    - __get_valute(id: str) -> dict: Возвращает информацию о валюте по ее идентификатору.
    - __getitem__(id): Возвращает информацию о валюте по ее идентификатору.
    - select_valute(id: str) -> None: Выбирает валюту для отслеживания.
    - get_currencies_ids_lst() -> list: Возвращает список идентификаторов отслеживаемых валют.
    - get_last_update(): Возвращает время последнего обновления информации о валютах.
    - visualize_currencies(): Визуализирует курсы валют и сохраняет график в файл currencies.jpg.
    """
    
    def __init__(self):
        """
        Инициализирует объект CurrenciesLst.
        """
        self.__currencies_ids_lst = []
        self.__cur_lst = []
        self.__req_time = None
    
    def get_currencies(self) -> list:
        """
        Получает курсы валют с сайта Центрального Банка России.
        Возвращает:
        - list: Список словарей с информацией о валютах.
        """
        from xml.etree import ElementTree as ET
    
        cur_res_str = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
        self.__req_time = datetime.now()
        root = ET.fromstring(cur_res_str.content)
        valutes = root.findall("Valute")
        for _v in valutes:
            valute_id = _v.get('ID')
            valute = {}
            if (str(valute_id) in self.__currencies_ids_lst):
                valute_cur_name  = _v.find('Name').text
                valute_cur_val = Decimal(_v.find('Value').text.replace(',', '.'))
                valute_charcode = _v.find('CharCode').text
                
                valute[valute_charcode] = (valute_cur_name, valute_cur_val)
                
                self.__cur_lst.append(valute)

        return self.__cur_lst

    def __get_valute(self, id: str) -> dict:
        """
        Возвращает информацию о валюте по ее идентификатору.
        Параметры:
        - id (str): Идентификатор валюты.
        Возвращает:
        - dict: Информация о валюте.
        """
        for valute in self.__cur_lst:
            if id in valute:
                return valute[id]
        return { id: None }

    def __getitem__(self, id):
        """
        Возвращает информацию о валюте по ее идентификатору.
        Параметры:
        - id: Идентификатор валюты.
        Возвращает:
        - dict: Информация о валюте.
        """
        return self.__get_valute(id)
    
    def select_valute(self, id: str) -> None:
        """
        Выбирает валюту для отслеживания.
        Параметры:
        - id (str): Идентификатор валюты.
        Возвращает:
        - None
        """
        self.__currencies_ids_lst.append(id)

    def get_currencies_ids_lst(self) -> list:
        """
        Возвращает список идентификаторов отслеживаемых валют.
        Возвращает:
        - list: Список идентификаторов валют.
        """
        return self.__currencies_ids_lst
    
    def get_last_update(self):
        """
        Возвращает время последнего обновления информации о валютах.
        Возвращает:
        - datetime: Время последнего обновления.
        """
        return self.__req_time
    
    def visualize_currencies(self):
        """
        Визуализирует курсы валют и сохраняет график в файл currencies.jpg.
        Возвращает:
        - None
        """
        import matplotlib.pyplot as plt
        
        fig, ax = plt.subplots()
        currencies = []
        values = []
        
        for curr in self.__cur_lst:
            for c, v in curr.items():
                currencies.append(c)
                values.append(v[1])

        bars = ax.bar(currencies, values)
        ax.bar_label(bars)
        ax.set_ylabel('Значение') 
        ax.set_title('Курсы валют')
    
        plt.savefig('currencies.jpg')

    def __del__(self):
        """
        Деструктор объекта CurrenciesLst.
        Освобождает ресурсы, связанные с объектом.
        """
        del self.__currencies_ids_lst
        del self.__cur_lst
        del self.__req_time