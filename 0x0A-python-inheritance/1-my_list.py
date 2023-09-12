#!/usr/bin/python3
"""Class MyList that inherits from list"""


class MyList(list):
    """Class MyList"""
    def print_sorted(self):
        """Prints the list"""
        sort_list = sorted(self)
        print(sort_list)
