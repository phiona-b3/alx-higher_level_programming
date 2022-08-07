#!/usr/bin/python3
"""checks if object is an exact instance of the specified class"""


def is_same_class(obj, a_class):
    """returns true if the above condition is satisfied else false"""
    return type(obj) == a_class
