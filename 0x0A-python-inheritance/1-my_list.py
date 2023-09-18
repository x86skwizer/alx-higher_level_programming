#!/usr/bin/python3
"""Class MyList that inherits from list"""


class MyList(list):
    """Class MyList inherits from list"""
    def print_sorted(self):
        """Prints the list"""
        print(sorted(self))