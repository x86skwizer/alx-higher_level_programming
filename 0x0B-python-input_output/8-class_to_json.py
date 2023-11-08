#!/usr/bin/python3
"""function returns dictionary description with simple data structure"""


def class_to_json(obj):
    """returns dictionary description with simple data structure"""
    result = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (str, int, bool, list, dict)):
            result[key] = value
    return result
