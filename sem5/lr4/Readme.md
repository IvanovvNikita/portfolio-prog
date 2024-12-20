# Лабораторная работа №4: Создание итератора по ряду Фибоначчи.
> Автор: *Иванов Никита Русланович*

### Цель работы:
Целью данной лабораторной работы является изучение работы с последовательностью Фибоначчи, а также использование итераторов для фильтрации чисел Фибоначчи из произвольного списка. В ходе работы будут реализованы функции и класс для вычисления последовательности Фибоначчи и работы с ней.

## Описание решения:

### 1. Функция `fib(n)`
Функция генерирует последовательность чисел Фибоначчи до указанного предела `n`. Если значение `n` меньше или равно нулю, возвращается пустой список или список с единственным числом [0]. Для положительных значений `n` функция генерирует числа Фибоначчи, пока не достигнет предела.

### 2. Класс `FibonacchiLst`
Класс `FibonacchiLst` представляет собой итератор, который фильтрует числа в списке и возвращает только те числа, которые входят в последовательность Фибоначчи, до максимального значения в данном списке.

- Атрибуты:
  - `lst` — входной список для итерации.
  - `idx` — индекс текущего элемента в списке.
  - `fibo` — последовательность Фибоначчи, рассчитанная до максимального значения во входном списке.
  
Методы:
- `__init__(self, lst)` — инициализирует объект, генерирует последовательность Фибоначчи до максимального элемента в списке.
- `__iter__(self)` — делает объект итерируемым.
- `__next__(self)` — возвращает следующее число из списка, если оно принадлежит последовательности Фибоначчи.

### 3. Функция `fib_iter(lst)`
Эта функция фильтрует переданный список, включая в него только те элементы, которые являются числами Фибоначчи. В отличие от класса, она использует стандартные функции Python, такие как `filterfalse` из модуля `itertools`, чтобы исключить все числа, которые не входят в последовательность Фибоначчи.