#!/usr/bin/python3
"""
Function that returns True if object is instance of class inherited
Otherwise False
"""


def inherits_from(obj, a_class):
    """
    Returns True if object is instance of class inherited 
    Otherwise False
    """
    return True if type(obj) != a_class else False
