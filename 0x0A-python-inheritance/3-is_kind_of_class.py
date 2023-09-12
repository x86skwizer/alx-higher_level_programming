#!/usr/bin/python3
"""
Function that returns: 
True if object is instance of, or is instance of class inherited from
Otherwise False
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if object is an instance of, or is instance of class inherited from
    Otherwise False
    """
    return isinstance(obj, a_class)
