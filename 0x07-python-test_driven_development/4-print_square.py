#!/usr/bin/python3
"""
Write a function that prints a square with the character #.
-Prototype: def print_square(size):
-size is the size length of the square
"""


def print_square(size):
    """
    Function prints square with character #.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for j in range(size):
        for i in range(size):
            print("#", end="")
        print("")
