#!/usr/bin/python3
"""Only sub class of"""


def inherits_from(obj, a_class):
    """returns True if object is instance of class that inherited from"""
    if type(obj) != a_class and issubclass(type(obj), a_class):
        return True
    return False
