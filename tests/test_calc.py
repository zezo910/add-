import unittest

from calc import calculate


class TestCalculator(unittest.TestCase):

    # Addition tests
    def test_addition_positive_numbers(self):
        self.assertEqual(calculate(5, 3, "+"), 8)