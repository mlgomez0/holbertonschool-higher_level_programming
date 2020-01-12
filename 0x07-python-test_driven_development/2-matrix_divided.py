#!/usr/bin/python3
"""This module has one function matrix_divided"""


def matrix_divided(matrix, div):
    """
    Function matrix_divided:

    Args:
        matrix (matrix): The first parameter.
        div (int or float): The second parameter

    Returns:
        matrix: The return value is a matrix
    """

    str1 = "matrix must be a matrix (list of lists)"
    str2 = "of integers/floats"
    my_matrix = []
    my_row = []
    if ((isinstance(matrix[0], list) is False) or div is None):
        raise TypeError(str1 + " " + str2)

    if (div == 0):
        raise ZeroDivisionError("division by zero")
    a = len(matrix[0])
    for row in matrix:
        if (len(row) != a):
            raise TypeError("Each row of the matrix must have the same size")
        a = len(row)
        for x in row:
            if (type(x) != int and type(x) != float):
                raise TypeError(str1 + " " + str2)
            my_row.append(round((x / div), 2))
        my_matrix.append(my_row)
        my_row = []
    return (my_matrix)
