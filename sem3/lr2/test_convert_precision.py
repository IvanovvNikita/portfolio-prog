from main import convert_precision


def test_convert_precision_1():
  assert convert_precision('0.0001') == 4

def test_convert_precision_2():
  assert convert_precision('InvalidValue') == 5

def test_convert_precision_3():
  assert convert_precision() == 3
