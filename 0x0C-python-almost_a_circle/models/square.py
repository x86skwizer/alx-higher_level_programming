#!/usr/bin/python3
"""Define class Square inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """The size property."""
        return self.width

    @size.setter
    def size(self, value):
        """The size setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """Representative string of Square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
