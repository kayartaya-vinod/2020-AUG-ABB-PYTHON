import unittest
from ex18 import factorial, fibonacci as fibo


class Ex18TestCases(unittest.TestCase):

    def test_factorial_1(self):
        # assertions --> expectations vs actuals
        expected = 120
        actual = factorial(5)
        self.assertEqual(expected, actual)

    def test_factorial_2(self):
        actual = factorial(10)
        self.assertEqual(3628800, actual)

    def test_fibo_1(self):
        self.assertEqual(0, fibo(0))
        self.assertEqual(1, fibo(1))
        self.assertEqual(1, fibo(2))
        self.assertEqual(2, fibo(3))