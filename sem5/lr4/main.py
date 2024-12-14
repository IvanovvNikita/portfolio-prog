def fib(n:int):
    """
    Генерирует последовательность Фибоначчи до указанного предела.

    Параметры:
    - n (int): Верхний предел для последовательности Фибоначчи.

    Возвращает:
    - list: Список, содержащий последовательность Фибоначчи до указанного предела.
    """
    if n == 0:
        return [0]
    elif n < 0:
        return []

    bar = [0,1]
    while (bar[-2] + bar[-1]) <= n :
        bar.append(bar[-2] + bar[-1]) 
    return bar


class FibonacchiLst:
    """
    Класс, представляющий итератор по списку, возвращающий только числа Фибоначчи.

    Атрибуты:
    - lst (list): Входной список для итерации.
    - idx (int): Текущий индекс итератора.
    - fibo (list): Последовательность Фибоначчи до максимального значения во входном списке.
    """
    
    def __init__(self,lst):
        """
        Инициализирует экземпляр FibonacchiLst.
        Параметры:
        - lst (list): Входной список для итерации.
        """
        self.lst = lst
        self.idx = 0
        self.fibo = self.__infibo(lst)
    def __iter__(self):
        """
        Делает класс итерируемым.
        Возвращает:
        Объект итератора.
        """
        return self

    def __next__(self):
        """
        Получает следующее число Фибоначчи в итерации.
        Возвращает:
        - int: Следующее число Фибоначчи.
        """
        while True:
            try:
                current = self.lst[self.idx]
            except IndexError:
                raise StopIteration from IndexError
            self.idx += 1
            if current in self.fibo:
                return current
    def __infibo(self,lst):
        """
        Рассчитывает последовательность Фибоначчи до максимального значения во входном списке.
        Параметры:
        - lst (list): Входной список.
        Возвращает:
        - list: Последовательность Фибоначчи до максимального значения во входном списке.
        """
        if lst == []:
            return []
        return fib(max(lst))



def fib_iter(lst):
    """
    Фильтрует список, включая только числа Фибоначчи.
    Параметры:
    - lst (list): Входной список.
    Возвращает:
    - list: Новый список, содержащий только числа Фибоначчи из входного списка.
    """
    if lst == []:
        return []
    fibo = fib(max(lst))
    from itertools import filterfalse
    return list(filterfalse(lambda x: not x in fibo, lst))
    
if __name__ == '__main__':
    #Fibonchi = FibonacchiLst()
    #print(list(Fibonchi))

    print(fib(1))
    print(fib_iter([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1]))