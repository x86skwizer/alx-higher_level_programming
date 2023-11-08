#!/usr/bin/python3
"""Defines func returns object represented by JSON"""
import json


def from_json_string(my_str):
    """return an object"""
    return json.loads(my_str)
