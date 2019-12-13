#!/usr/bin/python3
import magic_calculation_102
import dis
def magic_calculation(a, b):
       if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        if argv[2] == "+":
            c = cal.add(a, b)
            print("{:d} + {:d} = {:d}".format(a, b, c))
        elif argv[2] == "-":
            c = cal.sub(a, b)
            print("{:d} - {:d} = {:d}".format(a, b, c))
        elif argv[2] == "*":
            c = cal.mul(a, b)
            print("{:d} * {:d} = {:d}".format(a, b, c))
        elif argv[2] == "/":
            c = cal.div(a, b)
            print("{:d} / {:d} = {:d}".format(a, b, c))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
