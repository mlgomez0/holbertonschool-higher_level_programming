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

    if (isinstance(matrix[0], list) == False):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    a = len(matrix[0])
    for row in matrix:
        if (len(row) != a)
            raise TypeError("Each row of the matrix must have the same size")
        a = len(row)
        for x in row:
            if (type(x) != int and type(x) != float)


    return(list(map(lambda x:  list(map(lambda x: x / div if (type(x) == int or type(x) == float) else raise TypeError("matrix must be a matrix (list of lists) of integers/floats"), x)), matrix)))
