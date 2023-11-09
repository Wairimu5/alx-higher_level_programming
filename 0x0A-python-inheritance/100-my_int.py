#!/usr/bin/python3

"""Defines a subclass of int"""


class MyInt(int):
    """Represents a rebellious integer"""

    def __init__(self, value):
        """Initializes a MyInt object"""
        self.__value = value
        super().__init__()

    def __eq__(self, other):
        """Overrides the '=' operator to compare values in the opposite way"""
        return self.__value != other

    def __ne__(self, other):
        """Overrides the '!=' operator to compare values in the opposite way"""
        return self.__value == other
