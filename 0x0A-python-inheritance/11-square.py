#!/usr/bin/python3

"""Defines a square class and its methods"""

from base_geometry import Rectangle


class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size):
        """Initializes a square object"""
        super().validate_integer("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculates the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """Returns a string representation of the square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
