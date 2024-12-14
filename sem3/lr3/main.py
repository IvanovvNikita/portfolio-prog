"""
На вход поступает список с целыми числами, в том числе и отрицательными. Необходимо найти самое маленькое произведение 3 чисел из этого массива.

Требования:

- Решение оформить в виде функции.

- Входное значение - list, выходное - int

- В функции предусмотреть неверные входные аргументы.

- Реализовать обработку исключительных ситуаций (например, если, пришел неверный тип данных, то мы поднимаем ValueError)

- Написать параметризованные тесты с помощью пакета pytest.

Усложнение 1. Создать вторую функцию, которая будет принимать n->int - параметр, сколько чисел для произведения нужно искать.
"""

def threemin(numbers : list) -> int:
    if not isinstance(numbers, list):
        raise ValueError("Пришедший аргумент не является списком")
    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("Не все введеные элементы являются целыми числами")
    if len(numbers) < 3:
        raise ValueError("Введено меньше трёх чисел")
    numbers.sort()
    return min(numbers[0] * numbers[1] * numbers[2], numbers[0] * numbers[-2] * numbers[-1])
    
    
def input_numbers():
  """
  Функция для ввода чисел
  """
  numbers = []

  while True:
    op = input("Введите число: ")
    if op == "":
      return numbers
    else:
      try:
        op = int(op)
      except:
        print('Введенные данные некорректны, введите заново.')
      else:
        numbers.append(op)


def main():
    numbers = input_numbers();
    result = threemin(numbers)
    print(result)


if __name__ == "__main__":
   main()
