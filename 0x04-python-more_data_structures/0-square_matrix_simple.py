#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_new = [[]]
    matrix_new = [[x * x for x in y] for y in matrix]
    return (matrix_new)
