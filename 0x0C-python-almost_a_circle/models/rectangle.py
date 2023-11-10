#!/usr/bin/python3
"""Defines class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """The width property."""
        return self._width

    @width.setter
    def width(self, value):
        """The width setter."""
        self._width = value

    @property
    def height(self):
        """The height property."""
        return self._height

    @height.setter
    def height(self, value):
        """The height setter."""
        self._height = value

    @property
    def x(self):
        """The x property."""
        return self._x

    @x.setter
    def x(self, value):
        """The x setter."""
        self._x = value

    @property
    def y(self):
        """The y property."""
        return self._y

    @y.setter
    def y(self, value):
        """The y setter."""
        self._y = value
