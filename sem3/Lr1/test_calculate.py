from main import calculate


def test_calculate_addition():
  assert calculate(1000, 2, '+') == 1002


def test_calculate_subtraction():
  assert calculate(0, 39, '-') == -39


def test_calculate_multiplication():
  assert calculate(51, 10, '*') == 510


def test_calculate_division_1():
  assert calculate(1, 0, '/') == None


def test_calculate_division_2():
  assert calculate(1, 2, '/') == 0.5

def test_calculate_division_3():
  assert calculate(1, 3, '/') == 0.333333

def test_calculate_division_4():
  assert calculate(0, 3, '/') == 0

def test_calculate_exponentiation1():
  assert calculate(2, 10, '^') == 1024

def test_calculate_exponentiation2():
  assert calculate(2, 0, '^') == 1

def test_calculate_remains():
  assert calculate(40, 31, '%') == 9
