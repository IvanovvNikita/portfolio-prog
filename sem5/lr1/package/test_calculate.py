from .calculator import calculate
import unittest

__all__ = ['TestCalculate']


class TestCalculate(unittest.TestCase):

    params = {
        'precision': 0.00001,
        'output_type': float,
        'possible_types': None,
        'dest': None
    }

    def test_calculate_sum(self):
        self.assertEqual(calculate([1000, 2], '+', self.params), 1002)

    def test_calculate_minus(self):
        self.assertEqual(calculate([0, 39], '-', self.params), -39)

    def test_calculate_mulp(self):
        self.assertEqual(calculate([51, 10], '*', self.params), 510)

    def test_calculate_division(self):
        self.assertIsNone(calculate([1, 0], '/', self.params))
        self.assertEqual(calculate([0, 3], '/', self.params), 0.0)
        self.assertEqual(calculate([3, 1], '/'), self.params, 3.0)

    def test_calculate_pow(self):
        self.assertEqual(calculate([2, 10], '^', self.params), 1024.0)
        self.assertEqual(calculate([2, 0], '^', self.params), 1.0)

    def test_calculate_rem(self):
        self.assertEqual(calculate([40, 31], '%', self.params), 9.0)

    def test_calculate_std_dev(self):
        self.assertEqual(calculate([35, 33, 35, 33], 'std_dev', self.params),
                         1.0)
        self.assertEqual(calculate([50, 50, 50, 50], 'std_dev', self.params),
                         0.0)
        self.assertEqual(calculate([15, 59, 41, 132], 'std_dev', self.params),
                         43)


if __name__ == '__main__':
    unittest.main()
