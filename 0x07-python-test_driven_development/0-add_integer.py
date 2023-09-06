#!/usr/bin/python3
"""
    Write a function that adds 2 integers.
    a and b must be integers or floats
    otherwise raise a TypeError exception
"""


def add_integer(a, b=98):
    """
        Add two numbers and return the result as an integer.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
