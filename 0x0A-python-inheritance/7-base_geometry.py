#!/usr/bin/python3
"""class of basegeometry"""


class BaseGeometry:
    """representation of base geometry"""
    def area(self):
        """public instance method
        raises and error message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """raises type and value error"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
