from main import std_dev

def test_std_dev_1():
  assert std_dev([35, 33, 35 ,33]) == 1.0

def test_std_dev_2():
  assert std_dev([50, 50, 50 ,50]) == 0.0

def test_std_dev_3():
  assert std_dev([15, 59, 41 ,132]) == 43.47053599853584