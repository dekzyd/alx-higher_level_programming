#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for ele in matrix:
            print(" ".join("{:d}".format(i) for i in ele))
