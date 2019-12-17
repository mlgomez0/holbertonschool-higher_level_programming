#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_copy = []
    for i in my_list:
        if i % 2 == 0:
            list_copy.append(True)
        else:
            list_copy.append(False)
    return (list_copy)
