#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 2:
        x = tuple_a[0]
        y = tuple_a[1]
    elif len(tuple_a) == 1:
        x = tuple[0]
        y = 0
    else:
        x = y = 0
    if len(tuple_b) >= 2:
        z = tuple_b[0]
        w = tuple_b[1]
    elif len(tuple_b) == 1:
        z = tuple_b[0]
        w = 0
    else:
        z = w = 0
    m = x + z
    n = y + w
    t = (m, n)
    return (t)
