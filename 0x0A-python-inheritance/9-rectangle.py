#!/usr/bin/python3

"""Defines a rectangle class"""

from base_geometry import BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle"""

    def __init__(self, width, height):
        """Initializes a rectangle object"""
        super().__init__()
        super().validate_integer("height", height)
        super().validate_integer("width", width)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string representation of the rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
