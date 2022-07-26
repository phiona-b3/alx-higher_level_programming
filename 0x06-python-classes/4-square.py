#!/usr/bin/python3

class Square:
    """private class attribute"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """gets the current size of a square"""
        return self.__size

    @size.setter
    def size(self, value):
        """check if value is int"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
            """check if value is > 0"""
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2
