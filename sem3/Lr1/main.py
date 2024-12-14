def main():
  """
        Основная запускающая функция. Задачи: 
        принять от пользователя операнды, действие (+, -, *, / ) и запустить на вычисление
        функцию calculate, передав эти аргументы, 
        вывести значение результата на экран
        вычисляем с точность до 10^-6
    """
  operand1 = float(input('Введите первый операнд '))
  operand2 = float(input('Введите второй операнд '))
  action = input('Введите действие для вычисления ')

  result = calculate(operand1, operand2, action)

  print(f'Результат вычисления {result}')

  # return result


def calculate(op1, op2, action):
  """
        Основная вычислительная функция
    """
  res = None

  if action == '+':
    res = op1 + op2
  elif action == '-':
    res = op1 - op2
  elif action == '*':
    res = op1 * op2
  elif action == '/':
    if op2 != 0:
      res = round(op1 / op2,6)
  elif action == '^':
    res = op1**op2
  elif action == '%':
    res = op1 % op2
  return res


if __name__ == '__main__':  # 'main'
  main()
