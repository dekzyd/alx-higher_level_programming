#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        new_dict = sorted([v for k, v in a_dictionary.items()])
        for key, value in a_dictionary.items():
            if value == new_dict[-1]:
                return key
        else:
            return None
