from __future__ import annotations
import math

__all__ = ['calculate']

actions = ["+", "-", "/", "*", "^", "%", "std_dev"]


def convert_precision(precision='0.001') -> int:
    """
  Функция, конвертирующая точность в целочисленный тип
  """
    if type(precision) is str:
        try:
            precision = float(precision)
            return int(math.fabs(math.log10(precision)))
        except ValueError:
            print('Ошибка в значении точности')
            print('Используется значение по умолчанию {0.00001}')
            precision = 0.00001
            return int(math.fabs(math.log10(precision)))


def div(*args: tuple | list) -> float:
    res = args[0]
    if 0 in args[1:]:
        return
    for _el in args[1:]:
        res /= _el
    return res


def minus(*args: tuple | list) -> float | int:
    res = args[0]
    for _el in args[1:]:
        res -= _el
    return res


def mulp(*args: tuple | list) -> float | int:
    res = args[0]
    for _el in args[1:]:
        res *= _el
    return res


def pow(*args: tuple | list) -> float | int:
    res = args[0]
    for _el in args[1:]:
        res **= _el
    return res


def rem(*args: tuple | list) -> float | int:
    res = args[0]
    for _el in args[1:]:
        res %= _el
    return res


def std_dev(*args) -> float:
    """
        Вычисление среднего квадратического отклонения
    """
    partial_sum = sum(args) / len(args)
    partial_sum_squares = sum([(i - partial_sum)**2 for i in args]) / len(args)
    result = partial_sum_squares**0.5

    return result


def calculate(operands: list, action, params=None):
    """
        Основная вычислительная функция
    """
    
    
    if action == '+':
        operation = sum(operands)
    elif action == '-':
        operation = minus(*operands)
    elif action == '*':
        operation = mulp(*operands)
    elif action == '/':
        operation = div(*operands)
    elif action == '^':
        operation = pow(*operands)
    elif action == '%':
        operation = rem(*operands)
    elif action == 'std_dev':
        operation = std_dev(*operands)

    if operation == None:
        return

    if params is not None:
        output_type = params.get('output_type')
        precision = params.get('precision')
        return round(output_type(operation), convert_precision(precision))
    else:
        return float(operation)
