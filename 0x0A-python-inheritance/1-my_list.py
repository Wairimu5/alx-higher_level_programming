#!/usr/bin/python3
"""Provides a custom list class"""


class MyList(list):
    """Extends the list class"""

    def __init__(self):
        """Creates a new instance"""
        super().__init__()

    def print_sorted(self):
        """Displays the object in sorted order"""
        self.sort()
        print(self)
