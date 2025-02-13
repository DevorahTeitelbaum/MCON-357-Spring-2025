import unittest
from exercises.calculate_factorial import factorial_recursive, handle_input


class Test_Factorial(unittest.TestCase):

    def test_basic_factorial_case(self):
        self.assertEqual(factorial_recursive(5),120)

    def test_large_number_factorial(self):
        self.assertEqual(factorial_recursive(11),39916800)

    def test_factorial_of_zero_is_one(self):
        self.assertEqual(factorial_recursive(0),1)

    def test_factorial_of_one_is_one(self):
        self.assertEqual(factorial_recursive(0),1)

    def test_input_of_negative_number(self):
        self.assertEqual((None, "Number cannot be negative"), handle_input(str(-1)))

    def test_input_of_fraction (self):
        self.assertEqual((None, "Number must be an integer"), handle_input(str(.56)))


