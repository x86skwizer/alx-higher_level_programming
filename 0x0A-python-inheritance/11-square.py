#!/usr/bin/python3
"""Define class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square"""

    def __init__(self, size):
        """Constractor"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
