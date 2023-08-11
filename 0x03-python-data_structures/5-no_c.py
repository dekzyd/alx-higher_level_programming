#!/usr/bin/python3
def no_c(my_string):
    new_str = list(my_string[:])
    idx = []
    for i in range(len(new_str)):
        if new_str[i] == 'c' or new_str[i] == 'C':
            idx.append(i)
    idx.reverse()
    for i in range(len(idx)):
        new_str.pop(idx[i])
    return "".join(new_str)
