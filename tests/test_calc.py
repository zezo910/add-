import unittest

from calc import calc


class TestCalculator(unittest.TestCase):
#fdfsa
    # Addition tests
    def test_addition_positive_numbers(self):
        self.assertEqual(calc("+",5, 3), 8)
    def test_addition_positive_numbers(self):
        self.assertEqual(calc("+",5, 3), 8)

    def test_addition_negative_numbers(self):
        self.assertEqual(calc("+",-5, -3), -8)

    def test_addition_positive_and_negative(self):
        self.assertEqual(calc("+",-5, 3), -2)
