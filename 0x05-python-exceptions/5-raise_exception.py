#!/usr/bin/python3
def raise_exception():
    try:
        raise TypeError('Error')
    except TypeError:
        raise
