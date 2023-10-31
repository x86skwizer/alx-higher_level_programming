#!/usr/bin/python3
"""
Class Rectangle that defines a rectangle by:
-Private instance attribute: width
-Private instance attribute: height
-Instantiation with optional width and height
-Public instance method: def area(self)
-Public instance method: def perimeter(self)
-print() and str() should print rectangle with character #
"""


class Rectangle:
    """class Rectangle that defines a rectangle."""
    def __init__(self, width=0, height=0):
        """Instantiation."""
        self.height = height
        self.width = width

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

    def area(self):
        """Returns the rectangle area."""
        return (self.height * self.width)

    def perimeter(self):
        """Returns the rectangle perimeter."""
        if self.height == 0 or self.width == 0:
            return (0)
        return (2 * (self.height + self.width))

    def __str__(self):
        """Print the rectangle with the character #."""
        if self.width == 0 or self.height == 0:
            return ""
        return ''.join("#" * self.width + "\n"
                       for i in range(self.height - 1)) + ("#" * self.width)
