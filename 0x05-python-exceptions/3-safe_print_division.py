#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            value = my_list[i]
            if isinstance(value, int):
                print("{:d}".format(value))
                count += 1
        except (ValueError, TypeError, IndexError):
            break
    return count
