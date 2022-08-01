#!/usr/bin/python3
"""writing a class with a public instance method"""


class BaseGeometry:
    def area(self):
        """raise an exception with message"""
        raise Exception("area() is not implemented")
