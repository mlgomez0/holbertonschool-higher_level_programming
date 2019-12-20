#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    if not matrix:
        return (None)

    def squ_root(a_list=[]):
        return([x * x for x in a_list])
    return(list(map(squ_root, matrix)))
