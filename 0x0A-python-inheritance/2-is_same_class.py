#!/usr/bin/python3
"""
Write a function that returns:
True if the object is exactly an instance of the specified class
Otherwise False
"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is instance of specified class
    otherwise False
    """
    return True if type(obj) == a_class else False