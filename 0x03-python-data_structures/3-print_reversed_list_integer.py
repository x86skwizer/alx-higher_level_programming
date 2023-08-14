#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = 0
    while i < len(my_list):
        item = my_list[(i + 1) * (-1)]
        print("{:d}".format(item))
        i += 1
