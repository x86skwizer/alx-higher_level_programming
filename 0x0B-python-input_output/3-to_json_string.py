#!/usr/bin/python3
"""Defines func returns JSON representation of object"""
import json


def to_json_string(my_obj):
    """returns JSON representation of object"""
    return json.dumps(my_obj)
