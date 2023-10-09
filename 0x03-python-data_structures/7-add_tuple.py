#!/usr/bin/python3

# a function that adds 2 tuples

def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)

    sum_0 = a[0] + b[0]
    sum_1 = a[1] + b[1]

    return (sum_0, sum_1)
