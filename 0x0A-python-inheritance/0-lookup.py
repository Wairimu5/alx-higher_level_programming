#!/usr/bin/python3
"""Provides a function to get all object's properties"""


def lookup(obj):
    """Gets accessible attributes and methods of an object"""

    lst = list()
    lst = dir(obj)
    return lst
