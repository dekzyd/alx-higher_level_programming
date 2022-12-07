#!/usr/bin/python3
def roman_to_int(roman_string):
    r_num = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
    total = 0
    if roman_string:
        for char in roman_string:
            if char in r_num:
                total += r_num[char]

    return total
