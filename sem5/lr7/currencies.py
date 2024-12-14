import csv
import io
import json
from datetime import datetime
from decimal import Decimal

import requests


class Currencies():

    def get_currencies(self):
        pass

    def get_currencies_ids_lst(self):
        pass

    def __getitem__(self, id):
        pass

    def select_valute(self):
        pass

    def get_last_update(self):
        pass


def singleton(cls):
    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return getinstance


@singleton
class CurrenciesLst(Currencies):

    def __init__(self):
        self.__currencies_ids_lst = []
        self.__cur_lst = []
        self.__req_time = None

    def get_currencies(self) -> list:
        from xml.etree import ElementTree as ET

        cur_res_str = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')

        self.__req_time = datetime.now()
        self.__cur_lst = []
        root = ET.fromstring(cur_res_str.content)
        valutes = root.findall("Valute")
        for _v in valutes:
            valute_id = _v.get('ID')
            valute = {}
            if (str(valute_id) in self.__currencies_ids_lst):
                valute_cur_name = _v.find('Name').text
                valute_cur_val = Decimal(
                    _v.find('Value').text.replace(',', '.'))
                valute_charcode = _v.find('CharCode').text

                valute[valute_charcode] = (valute_cur_name, valute_cur_val)

                self.__cur_lst.append(valute)

        return self.__cur_lst

    def __get_valute(self, id: str) -> dict:
        for valute in self.__cur_lst:
            if id in valute:
                return valute[id]
        return {id: None}

    def __getitem__(self, id):
        return self.__get_valute(id)

    def select_valute(self, id: str) -> None:
        self.__currencies_ids_lst.append(id)

    def get_currencies_ids_lst(self) -> list:
        return self.__currencies_ids_lst

    def get_last_update(self):
        return self.__req_time

    def visualize_currencies(self):
        import matplotlib.pyplot as plt

        fig, ax = plt.subplots()
        currencies = []
        values = []

        for curr in self.__cur_lst:
            for c, v in curr.items():
                currencies.append(c)
                values.append(v[1])

        bars = ax.bar(currencies, values)
        plt.xticks(rotation=-45)

        ax.bar_label(bars)
        ax.set_ylabel('Значение')
        ax.set_title('Курсы валют')

        plt.savefig('currencies.jpg')

    def __del__(self):
        del self.__currencies_ids_lst
        del self.__cur_lst
        del self.__req_time


class CurrenciesDecorator(Currencies):

    def __init__(self, component) -> None:
        self._component = component

    def component(self):
        return self._component

    def get_currencies(self):
        return self._component.get_currencies()

    def __getitem__(self, item):
        return self._component[item]

    def get_currencies_ids_lst(self):
        return self._component.get_currencies_ids_lst()

    def select_valute(self, id):
        return self._component.select_valute(id)

    def get_last_update(self):
        return self.get_last_update()


class CurrenciesDecoratorJSON(CurrenciesDecorator):

    def to_JSON(self, value):
        return json.dumps(value, ensure_ascii=False, default=str)

    def get_currencies(self):
        return self.to_JSON(self.component().get_currencies())

    def get_currencies_ids_lst(self):
        return self.to_JSON((self.component().get_currencies_ids_lst()))

    def __getitem__(self, id):
        return self.to_JSON(self.component()[id])

    def select_valute(self):
        return self.to_JSON(self.component().select_valute())

    def get_last_update(self):
        return self.to_JSON(self.get_last_update())


class CurrenciesDecoratorCSV(CurrenciesDecorator):

    def to_CSV(self, values):
        output = io.StringIO()
        writer = csv.writer(output, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(["ID", "Код", "Значение"])

        for val in values:
            for c, v in val.items():
                writer.writerow([c, v[0], v[1]])

        return output.getvalue()

    def get_currencies(self):
        return self.to_CSV(self.component().get_currencies())

    def get_currencies_ids_lst(self):
        return self.to_CSV((self.component().get_currencies_ids_lst()))

    def __getitem__(self, id):
        return self.to_CSV(self.component()[id])

    def select_valute(self):
        return self.to_CSV(self.component().select_valute())

    def get_last_update(self):
        return self.to_CSV(self.get_last_update())
