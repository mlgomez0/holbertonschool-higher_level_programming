#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    if not matrix:
        return (None)
    def my_func(matrix=[]):
        return([[x * x for x in y] for y in matrix])
    return(list(map(my_func, matrix)))
