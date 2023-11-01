#!/usr/bin/python3
"""
Write a function that prints My name is <first name> <last name>
-Prototype: def say_my_name(first_name, last_name=""):
-first_name and last_name must be strings
"""

def say_my_name(first_name, last_name=""):
    """
    Function prints My name is <first name> <last name>
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
