#!/usr/bin/python3
# a function that prints all integers of a list, in reverse order

def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return None
    length = len(my_list) - 1
    while (length >= 0):
        print("{:d}".format(my_list[length]))
        length = length - 1
