#!/usr/bin/python3
def max_integer(my_list=[]):
    tem = 0
    if my_list:
        for i in my_list:
            if i > tem:
                tem = i
        return (tem)
    else:
        return (None)
