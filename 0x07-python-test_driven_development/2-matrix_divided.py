#!/usr/bin/python3
"""
Write a function that divides all elements of a matrix.
-Prototype: def matrix_divided(matrix, div):
-matrix must be a list of lists of integers or floats
"""


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix.
    """
    tyerror = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(tyerror)
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(tyerror)
    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [x for row in matrix for x in row]):
        raise TypeError(tyerror)
    if not all(len(matrix[0]) == len(row) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    return [[round(x / div, 2) for x in row] for row in matrix]
