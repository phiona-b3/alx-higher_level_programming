#!/usr/bin/python3
"""rectangle inherits from basegeometry"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Representation of rectangle"""
    def __init__(self, width, height):
        """Instantiation and validation"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
