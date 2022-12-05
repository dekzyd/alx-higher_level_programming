#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        new_table = [True if elem % 2 == 0 else False for elem in my_list]
        return new_table
