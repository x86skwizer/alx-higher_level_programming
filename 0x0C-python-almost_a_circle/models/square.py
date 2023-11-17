#!/usr/bin/python3
"""Define class Square inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Representative string of Square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
