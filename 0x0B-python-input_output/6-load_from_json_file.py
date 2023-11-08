#!/usr/bin/python3
"""Define func creates Object from JSON file"""
import json


def load_from_json_file(filename):
    "creates an Object from a JSON file"
    with open(filename, 'r') as file:
        return json.load(file)
