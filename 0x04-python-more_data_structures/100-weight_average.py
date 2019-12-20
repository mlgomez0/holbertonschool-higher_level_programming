#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)
    my_mul = list(map(lambda ab: ab[1] * ab[0], my_list))
    my_div = [b for (a, b) in my_list]
    average_l = sum(my_mul) / sum(my_div)
    return (average_l)
