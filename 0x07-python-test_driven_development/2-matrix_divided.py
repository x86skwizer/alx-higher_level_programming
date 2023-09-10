#!/usr/bin/python3
"""
    function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
        All elements of matrix should be divided by div
        Returns a new matrix
    """
    reslt = []
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    sizer = len(matrix[0])
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != sizer:
            raise TypeError("Each row of the matrix must have the same size")
        nwr = []
        for ele in row:
            if not isinstance(ele, int) and not isinstance(ele, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            nwr.append(round(float(ele) / float(div), 2))
        reslt.append(nwr)
    return reslt
