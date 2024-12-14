def main():
    import package
    from package.test_calculate  import TestCalculate
    p = package.PARAMS
    
    s = package.calculate([2,4,5,1],"+", p)
    print(s)
    t = TestCalculate()
    t.test_calculate_sum()
    
if __name__ == '__main__':  #'main'
  main()
