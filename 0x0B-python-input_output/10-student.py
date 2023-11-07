#!/usr/bin/python3
"""
student clasis
"""


class Student:
    """Representation of a student"""

    def __init__(self, first_name, last_name, age):
        """Creates a new Student"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a Student dict with specified attributes."""

        if attrs is None:
            return self.__dict__

        new_dict = {}
        for a in attrs:
            try:
                new_dict[a] = self.__dict__[a]
            except KeyError:
                pass

        return new_dict
