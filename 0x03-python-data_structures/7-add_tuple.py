#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    result = []
    for i in range(2):
        result.append(a[i] + b[i])
    return tuple(result)
