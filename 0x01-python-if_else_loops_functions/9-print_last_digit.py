#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        last_digit = number * (-1)
    else:
        last_digit = number
    last_digit = last_digit % 10
    print("{:d}".format(last_digit), end='')
    return(last_digit)
