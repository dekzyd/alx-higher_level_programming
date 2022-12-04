#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for ele in matrix:
        for ment in ele:
            print("{:d}".format(ment), end=" ")
        print()
