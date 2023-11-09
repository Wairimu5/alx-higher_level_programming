#!/usr/bin/python3

"""Checks if an object belongs to a class"""


def is_same_class(obj, a_class):
    """Determines if an object is an instance of a class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
