#!/usr/bin/python3
"""Function returns list of available attributes and methods of object"""

def lookup(obj):
    """Return a list of object's attributes and methods"""
    return dir(obj)
