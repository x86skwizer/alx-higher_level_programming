#!/usr/bin/python3
"""
Class Rectangle that defines a rectangle by:
-Private instance attribute: width
-Private instance attribute: height
-Instantiation with optional width and height
"""


class Rectangle:
    """class Rectangle that defines a rectangle."""
    def __init__(self, width=0, height=0):
        """Instantiation."""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """The width property."""
        return self.__width

    @width.setter
    def width(self, value):
        """The width setter."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """The height property."""
        return self.__height

    @height.setter
    def height(self, value):
        """The height setter."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
