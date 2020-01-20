#!/usr/bin/python3
"""This module determines if a object is and instance
of a given class.

The module has the function is_kind_of_class.
"""


def is_kind_of_class(obj, a_class):
    """function is_kind_of_class.
    It returns True or False pending if the given object
    is an instance of a given class.

    """
    return isinstance(obj, a_class)
