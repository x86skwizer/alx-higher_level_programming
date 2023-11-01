#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Test function.
    """
    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 2, 0, 5]), 5)

    def test_duplicate_numbers(self):
        self.assertEqual(max_integer([1, 2, 2, 1]), 2)


if __name__ == '__main__':
    """
    Main function.
    """
    unittest.main()
