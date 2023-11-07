#!/usr/bin/python3
"""Function writes string to text file and returns nbr of chars written"""


def write_file(filename="", text=""):
    """writes string to text file and returns number of characters written"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
