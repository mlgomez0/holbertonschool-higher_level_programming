#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = {k : 2 * v for (k, v) in a_dictionary.items()}
    return (new_dic)
