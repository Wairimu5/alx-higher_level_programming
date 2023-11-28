#!/usr/bin/python3
"""
Unittests for the max_integer function.
"""

import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer_with_valid_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_integer_with_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_max_integer_with_mixed_list(self):
        self.assertEqual(max_integer([-1, 0, 1, -10]), 1)
        self.assertEqual(max_integer([-1, "hello", 1, -10]), "hello")

    def test_max_integer_with_floats(self):
        self.assertEqual(max_integer([1.5, 2.3, 0.7, -1.2]), 2.3)
        self.assertEqual(max_integer([-1.5, -2.3, -0.7, -1.2]), -0.7)

    def test_max_integer_with_single_element_list(self):
        self.assertEqual(max_integer([42]), 42)

    def test_max_integer_with_negative_numbers(self):
        self.assertEqual(max_integer([-5, -2, -8, -1]), -1)
        self.assertEqual(max_integer([-5, -2, -8, -1.5]), -1.5)

if __name__ == "__main__":
    unittest.main()
