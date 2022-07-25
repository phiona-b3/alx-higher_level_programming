#!/usr/bin/python3

"""create a class called square"""
class Square:
    """private class attribute"""
    def __init__(self, size=0):
        self.__size = size


"""property to retrieve size"""
    @property
    def size(self):
        """gets the current size of a square"""
        return self.__size

"""property setter to set it"""
    @size.setter
    def size(self, value):
        """check if value is int"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        """check if value is > 0"""
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

"""getting the area of square"""
    def area(self):
        return self.__size ** 2
