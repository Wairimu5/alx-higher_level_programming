#!/usr/bin/python3
"""
Contains the class "Student"
"""


class Student:
    """Represents a student"""
    def __init__(self, first_name, last_name, age):
        """Initializes the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary with specified or all attributes"""
        if attrs is None:
            return self.__dict__

        new_dict = {}
        for a in attrs:
            try:
                new_dict[a] = self.__dict__[a]
            except KeyError:
                pass

        return new_dict

    def reload_from_json(self, json):
        """Replace all attributes from a provided dictionary"""
        for key in json:
            try:
                setattr(self, key, json[key])
            except KeyError:
                pass
