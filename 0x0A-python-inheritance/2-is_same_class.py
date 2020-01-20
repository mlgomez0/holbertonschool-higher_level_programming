#!/usr/bin/python3
"""This module determines if a object is and instance
of a given class.

The module has the function is_same_class.
"""


def is_same_class(obj, a_class):
    """function is_same_class.
    It returns True or False pending if the given object
    is an instance of a given class.

    """
    return type(obj) == a_class
