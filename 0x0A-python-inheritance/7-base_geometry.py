#!/usr/bin/python3
"""class called basegeometry"""


class BaseGeometry:
    """public instance method area"""
    def area(self):
        """raise an error message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """publice instance method that raise type and value error"""
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
