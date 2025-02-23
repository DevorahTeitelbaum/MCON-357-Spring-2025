import math
import sys
import unittest
from exercises.calculate_factorial import factorial_recursive, handle_input, factorial_iterative


class Test_Factorial(unittest.TestCase):

    # test cases for the recursive factorial calculator method
    def test_basic_factorial_case_rec(self):
        self.assertEqual(factorial_recursive(5), 120)

    def test_large_number_factorial_rec(self):
        self.assertEqual(factorial_recursive(11), math.factorial(11))

    def test_factorial_of_zero_is_one_rec(self):
        self.assertEqual(factorial_recursive(0), 1)

    def test_factorial_of_one_is_one_rec(self):
        self.assertEqual(factorial_recursive(0), 1)

    # test cases for the iterative factorial calculator method
    def test_basic_factorial_case_iter(self):
        self.assertEqual(factorial_iterative(5), 120)

    def test_large_number_factorial_iter(self):
        self.assertEqual(factorial_iterative(11), math.factorial(11))

    def test_factorial_of_zero_is_one_iter(self):
        self.assertEqual(factorial_iterative(0), 1)

    def test_factorial_of_one_is_one_iter(self):
        self.assertEqual(factorial_iterative(1), 1)

    # test cases for input handling
    def test_input_of_negative_number(self):
        self.assertEqual((None, "Number cannot be negative"), handle_input(str(-1)))

    def test_input_of_fraction(self):
        self.assertEqual((None, "Number must be an integer"), handle_input(str(.56)))

    #tests for the recursion limit
    def test_recursion_under_limit(self):
        self.assertEqual(factorial_recursive(984), math.factorial(984))
        #greatest number without triggering recursion error

    def test_recursion_over_limit(self):
        recursion_limit = sys.getrecursionlimit()

        # Test recursive function exceeding recursion limit
        with self.assertRaises(RecursionError):
            factorial_recursive(recursion_limit)

        # Test iterative function throws no error
        self.assertEqual(factorial_iterative(recursion_limit), math.factorial(recursion_limit))  # Replace with expected result
