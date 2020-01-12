#!/usr/bin/python3
"""This module has the function print_square"""


def print_square(size):
    """
    Function print_square:

    Args:
        size (int): To stablish the size of the square of #s

    Returns:
        No return
    """

    if (type(size) != int or size is None):
        raise TypeError("size must be an integer")
    elif (size < 0):
        raise ValueError("size must be >= 0")
    else:
        a = (size * "#") + "\n"
        print(size * a, end= "")
