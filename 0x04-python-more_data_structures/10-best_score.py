#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return (None)
    my_list = sorted(a_dictionary.items(), key=lambda kv: (kv[1], kv[0]))
    k, v = my_list[-1]
    return (k)
