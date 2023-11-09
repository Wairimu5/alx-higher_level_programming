#!/usr/bin/python3

"""This module defines a square class"""

from base_geometry import Rectangle


class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size):
        """Initializes a square object"""
        super().validate_integer("size", size)
        super().__init__(size, size)
        self.__size = size
