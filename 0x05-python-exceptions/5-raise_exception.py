#!/usr/bin/python3

def raise_exception():
    try:
        x = "5" + 5
    except TypeError:
        raise TypeError("Type exception raised")
