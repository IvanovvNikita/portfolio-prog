from __future__ import annotations
import math
import numpy as np
__settings = {'precision': "0.00001"}

def convert_precision(precision = '0.001') -> int:
  if type(precision) is str:
    try:
      precision = float(precision)
      return int(math.fabs(math.log10(precision)))
    except ValueError:
      print('Ошибка в значении точности')
      print('Используется значение по умолчанию {0.00001}')
      precision = 0.00001
      return int(math.fabs(math.log10(precision)))

def InputOperands():
  operands = []
  op = 1
  while op != "":  # while True
        op = input("Введите операнд: ")
    
        if op == "":
            break
        else: 
            op = float(op)
            operands.append(op)
  return operands


def main():
  global __settings
  operands = []
  while True:
    operands = InputOperands()

    action = input('Введите действие для вычисления ')
  
    result = calculate(operands, action,settings = __settings)
    if result == None:
        print('Неверные значения, введите данные заново')
        continue
    print(f'Результат вычисления {result}')
    break
      
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
        Вычисление среднего квадратического отклонения.
    """
    args = np.array(args)
    result = np.std(args)

    return result

def calculate(operands: list, action, settings = __settings):
  """
        Основная вычислительная функция
    """
  #res = None

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
    
  return round(operation,convert_precision(__settings['precision']))





if __name__ == '__main__':  #'main'
  main()






