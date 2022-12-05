#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        length = len(my_list)
        if length >= 1:
            for i in range(length - 1):
                if my_list[i + 1] < my_list[i]:
                    my_list[i + 1], my_list[i] = my_list[i], my_list[i + 1]
            return my_list[length - 1]
