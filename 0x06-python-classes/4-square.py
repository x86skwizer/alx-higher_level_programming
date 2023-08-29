#!/usr/bin/python3
"""Creat class Square"""


class Square:
    """A class representing a square.

    Attributes:
        size (int): The size of the square's sides.
    """

    def __init__(self, size=0):
        """Creates a Square instance with a specified size.

        Args:
            size (int, optional): The size of the square's sides.
            Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        self.size = size

    @property
    def size(self):
        """int: The size of the square's sides."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square's sides.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
