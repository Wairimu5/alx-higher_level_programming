#!/usr/bin/python3
"""
Contains the "class_to_json" function
"""


def class_to_json(obj):
    """Returns a simple dict description for JSON serialization."""

    return obj.__dict__
