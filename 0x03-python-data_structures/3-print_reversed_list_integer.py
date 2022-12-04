#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    ln = len(my_list) - 1
    if my_list:
        for idx in range(ln, -1, -1):
            print("{:d}".format(my_list[idx]))
