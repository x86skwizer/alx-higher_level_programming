#!/usr/bin/python3
"""Improve Geometry"""


class BaseGeometry:
    """class BaseGeometry"""

    def area(self):
        """instance method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
