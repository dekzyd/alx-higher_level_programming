#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        best_mark = 0
        best = 0

        for k in a_dictionary:
            if a_dictionary[k] > best_mark:
                best_mark = a_dictionary[k]
                best = k
        return best
    return None
