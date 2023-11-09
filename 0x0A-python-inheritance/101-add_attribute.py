#!/usr/bin/python3

"""Provides a function to add an attribute to an object"""


def add_attribute(obj, attribute, value):
    """Adds an attribute to an object if it doesn't already exist"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("Object cannot have new attributes added")
    if not hasattr(obj, attribute):
        setattr(obj, attribute, value)

