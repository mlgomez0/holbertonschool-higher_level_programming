#!/usr/bin/python3
def uniq_add(my_list=[]):
    set_of_list = set(my_list)
    new_list = list(set_of_list)
    return(sum(new_list))
