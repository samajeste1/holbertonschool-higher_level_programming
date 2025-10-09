#!/usr/bin/python3
"""
Module 2-matrix_divided
Divides all elements of a matrix by a given number.
"""

def matrix_divided(matrix, div):
    """
    Divides each element of the matrix by div.
    Returns a new matrix with results rounded to 2 decimals.
    """
    message = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(message)

    row_length = None
    new_matrix = []

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(message)
        if row_length is None:
            row_length = len(row)
        elif row_length != len(row):
            raise TypeError("Each row of the matrix must have the same size")

        new_row = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(message)
            if not isinstance(div, (int, float)):
                raise TypeError("div must be a number")
            if div == 0:
                raise ZeroDivisionError("division by zero")
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)

    return new_matrix
