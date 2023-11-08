#!/usr/bin/python3
"""Define func writes an object to text file using JSON"""
import json


def save_to_json_file(my_obj, filename):
    """writes Object to text file using JSON represent"""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
