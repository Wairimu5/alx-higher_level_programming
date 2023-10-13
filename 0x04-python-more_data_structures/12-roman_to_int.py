#!/usr/bin/python3
def roman_to_int(roman_string):
    ns = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    total = 0
    for i in range(len(roman_string) - 1):
        if ns[roman_string[i]] >= ns[roman_string[i + 1]]:
            total += ns[roman_string[i]]
        else:
            total -= ns[roman_string[i]]
    total += ns[roman_string[-1]]  # Add the value of the last numeral
    return total
