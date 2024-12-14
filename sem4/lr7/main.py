"""
Иванов Никита 1.1
Лабораторная работа 7.
Работа с JSON
"""

import json


def open_json(file_name):
    import os
    import stat
    """
    Функция для открытия json файла и извлечения данных
    :param file_name: Имя файла для чтения данных
    :return: Список словарей данных или None, если файл не найден или данные не могут быть прочитаны
    """
    # Проверяем права доступа к файлу
    try:
        if not os.access(file_name, os.R_OK):
            # Если нет прав на чтение, запросить права доступа
            os.chmod(file_name, stat.S_IRWXU)
    except PermissionError as e:
        print(f"Ошибка доступа к файлу: {e}")
        return None

    try:
        with open(file_name, 'r') as f:
            data = json.load(f)
    except FileNotFoundError as e:
        print(f"Файл {file_name} не найден: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Неверный формат данных в файле: {e}")
        return None
    except Exception as e:
        print(f"Не удалось прочитать данные из файла: {e}")
        return None

    if not data:
        print("Нет данных")
        return None

    return data
  
def select_fields(data, fields):
    """
    Функция для выборки нужных данных из общего набора данных
    :param data: Набор данных
    :param fields: Объект, содержащий названия и типы полей для выборки
    :return: Список словарей данных или None, если данные не могут быть выбраны
    """
    if not data:
        return None

    result = []
    for d in data:
        new_d = {}
        for key, value_type in fields.items():
            value = d.get(key)
            if value is None:
                print(f"Поле '{key}' отсутствует в данных")
                break
            elif not isinstance(value, value_type):
                print(f"Неверный тип данных для поля '{key}': ожидается {value_type.__name__}, получен {type(value).__name__}")
                break
            else:
                new_d[key] = value
        else:
            result.append(new_d)

    if not result:
        print("Нет данных, соответствующих заданной схеме")

    return result
  
def add_data(data, fields):
    """
    Функция для добавления данных с клавиатуры
    :param data: Список словарей данных
    :param fields: Объект, содержащий поля для ввода данных
    :return: Обновленный список словарей данных
    :raises ValueError: если введенное значение не соответствует ожидаемому типу данных
    """
    while True:
        add_new_data = input("Хотите добавить новые данные? (да/нет): ")
        if add_new_data.lower() not in ["да", "нет"]:
            print("Неверный ввод. Пожалуйста, введите 'да' или 'нет'.")
        else:
            break

    while add_new_data.lower() == "да":
        new_data = {}
        for field, data_type in fields.items():
            while True:
                try:
                    value = input(f"Введите значение для поля '{field}': ")
                    if data_type == list:
                        new_data[field] = value.split(',')
                    else:
                        new_data[field] = data_type(value)
                    break
                except ValueError:
                    raise ValueError(f"Неверный тип данных для поля '{field}'. Ожидается {data_type.__name__}")

        data.append(new_data)

        while True:
            add_more_data = input("Хотите добавить еще данные? (да/нет): ")
            if add_more_data.lower() not in ["да", "нет"]:
                print("Неверный ввод. Пожалуйста, введите 'да' или 'нет'.")
            else:
                break

        if add_more_data.lower() == "нет":
            break

    return data
  


def print_data(data):
  import pprint
  """
  Функция для вывода данных с помощью pprint

  :param data: Данные для вывода
  """
  pprint.pprint(data,sort_dicts=False)

def save_to_json(data, filename):
    """
    Функция для сохранения списка словарей в файл в формате JSON

    :param data: Список словарей данных
    :param filename: Имя файла для сохранения данных
    :return: True, если данные успешно сохранены, и False в противном случае
    :raises IOError: если не удалось сохранить данные в файл
    """
    try:
        with open(filename, 'w') as f:
            json.dump(data, f)
            return True
    except Exception as e:
        raise IOError(f"Не удалось сохранить данные в файл {filename}: {e}")


if __name__ == '__main__':
    
    fields = {
        "name": str,
        "gender": str,
        "email": str,
        "phone": str,
        "address": str,
        "friends": list
    }
    all_data = open_json('data.json')
    data = select_fields(all_data,fields)
    new_data = add_data(data,fields)
    print_data(new_data)
    save_to_json(new_data,'clients_data.json')