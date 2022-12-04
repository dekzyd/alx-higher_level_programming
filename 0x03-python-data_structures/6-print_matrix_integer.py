#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for ele in matrix:
            for ment in ele:
                last_in_list = len(ele)
                if ele.index(ment) == last_in_list - 1:
                    print("{:d}".format(ment))
                    continue
                print("{:d}".format(ment), end=" ")
