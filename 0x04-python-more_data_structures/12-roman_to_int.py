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
    i = 0
    total = 0
    if roman_string.isalpha():
        for i in range(len(roman_string - 1)):
            if r_num[roman_string[i]] >= r_num[roman_string[i + 1]]:
                total += r_num[roman_string[i]]
            else:
                total -= r_num[roman_string[i]]
            i += 1
        return total
    else:
        return 0
