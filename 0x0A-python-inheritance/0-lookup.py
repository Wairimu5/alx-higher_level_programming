#!/usr/bin/python3

"""Provides a function to retrieve all attributes and methods of an object"""


def lookup(obj):
    """Returns a list of all attributes and methods accessible to an object"""
    return dir(obj)
