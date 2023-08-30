#!/usr/bin/python3
"""Creat class Square"""


class Square:
    """A class representing a square.

    Attributes:
        size (int): The size of the square's sides.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Creates a Square instance with a specified size.

        Args:
            size (int, optional): The size of the square's sides.
            Defaults to 0.
            position: Coordination of the square

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """int: The position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square.

        Args:
            value (int): The new position value.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is negative.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        x, y = value
        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif x < 0 or y < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #."""
        if self.__size:
            for k in range(self.position[1]):
                print()
            for i in range(self.__size):
                for s in range(self.position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print("")
        else:
            print("")
