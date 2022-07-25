#!/usr/bin/python3

"""Define a class called Square"""


class Square:
    """create a private instance attribute"""
    area = 0
    def __init__(self, size=0):
        self.__size = size
        """ check for the type of value in size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        """check for the value in size"""
        if size < 0:
            raise ValueError("size must be >= 0")


"""define a function called area"""


@classmethod
def area(self):
    """return the area"""
    return self.__size ** 2
