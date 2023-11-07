#!/usr/bin/python3
"""Function writes string to text file and returns number of characters written"""


def write_file(filename="", text=""):
    """writes string to text file and returns number of characters written"""
    len = 0
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
