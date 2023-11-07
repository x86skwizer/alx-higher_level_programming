#!/usr/bin/python3
"""Exact same object"""


def is_same_class(obj, a_class):
    """returns True if object is instance of specified class"""
    if type(obj) == a_class:
        return True
    return False
