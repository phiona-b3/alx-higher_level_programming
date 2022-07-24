#!/usr/bin/python3
"""prints size values which are integers and are
equal to or greater than 0"""


class Square:
    """defines aa class called Square"""
    def __init__(self, size=0):
        self.__size = size
        """Check for the type of value in size"""
        if type(size) is not int:
            raise TypeError("Size must be an integer")
        """Check for the value of size"""
        if size < 0:
            raise ValueError("Size must be >= 0")
