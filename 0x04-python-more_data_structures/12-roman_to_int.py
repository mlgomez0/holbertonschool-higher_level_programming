#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return (0)
    sum_num = 0
    tem = 0
    dir_roman = {'M': 1000, 'D': 500,
                 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    for i in roman_string:
        for k, v in dir_roman.items():
            if i == k and (tem >= v or tem == 0):
                sum_num += v
                tem = v
            elif i == k and tem < v:
                sum_num = sum_num - (2 * tem) + v
    return(abs(sum_num))
