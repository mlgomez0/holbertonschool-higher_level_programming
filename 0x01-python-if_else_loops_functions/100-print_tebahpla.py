#!/usr/bin/python3
flag = 1;
for i in range(122, 96, -1):
    if flag == -1:
        m = i - 32
    else:
        m = i
    print("{:c}".format(m), end='')
    flag = flag * (-1)
