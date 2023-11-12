#!/usr/bin/python3
"""Unit testing class Base"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """Test class Base"""

    def setUp(self):
        self.base1 = Base()
        self.base2 = Base()
        self.base3 = Base(12)
        self.base4 = Base()
        self.base5 = Base(-6)

    def test_id(self):
        self.assertEqual(self.base1.id, 1)
        self.assertEqual(self.base2.id, 2)
        self.assertEqual(self.base3.id, 12)
        self.assertEqual(self.base4.id, 3)
        self.assertEqual(self.base5.id, -6)
