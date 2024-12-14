
import pytest
from main import fib, FibonacchiLst, fib_iter


def test_fibonacci_list():
    assert fib(0) == [0]
    assert fib(1) == [0, 1, 1]
    assert fib(10) == [0, 1, 1, 2, 3, 5, 8]

def test_FibonacchiLst_iterator():
    fib_lst = FibonacchiLst([0, 1, 2, 3, 5, 8, 13, 21])
    result = list(iter(fib_lst))
    assert result == [0, 1, 2, 3, 5, 8, 13, 21]

def test_fib_iter():
    assert fib_iter([]) == []
    assert fib_iter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 5, 8]