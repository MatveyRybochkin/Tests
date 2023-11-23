import unittest
from main import FactorialCalculator


class TestFactorialCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = FactorialCalculator()

    def test_factorial_of_zero(self):
        result = self.calculator.calculate_factorial(0)
        self.assertEqual(result, 1)

    def test_factorial_of_five_number(self):
        result = self.calculator.calculate_factorial(5)
        self.assertEqual(result, 120)



if __name__ == '__main__':
    unittest.main()