#!/usr/bin/python3
"""Determine one peak in agiven array"""
def find_peak(list_of_integers):
    """returns one peak in a given array"""
    i = 0
    if list_of_integers == None or len(list_of_integers) == 0:
        return None
    for i in range(len(list_of_integers)):
        if i == 0 and list_of_integers[1] <= list_of_integers[0]:
            return list_of_integers[0]
        elif list_of_integers[i] >= list_of_integers[i + 1] and list_of_integers[i] >= list_of_integers[i - 1]:
            return list_of_integers[i]
        i += 1
    return list_of_integers[i - 1]
