#!/usr/bin/python3
"""if the object is an instance of, or if the object is an
instance of a class that inherited from, the specified
class ; otherwise False"""


def is_kind_of_class(obj, a_class):
    """checking for the above condition"""
    return isinstance(obj, a_class)
