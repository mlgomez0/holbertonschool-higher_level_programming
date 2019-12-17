#!/usr/bin/python3
def max_integer(my_list=[]):
    tem = 0
    if my_list == []:
        return (None)
    for i in my_list:
        if i > tem:
            tem = i
    return (tem)
