#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    else:
        my_list.sort()
        return my_list[len(my_list) - 1]
