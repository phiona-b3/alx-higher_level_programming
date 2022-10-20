#!/usr/bin/python3
"""a function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """definition of the function"""
    a = list_of_integers
    if len(a) == 0:
        return

    b = len(a) // 2
    if len(a) > 1:
        if b >= b - 1 and b >= b + 1:
            return b
        if (b == len(a) - 1 or a >= a[b + 1])\
           and (b == 0 or a[b] >= a[b - 1]):
            return a[b]
        if a[0] >= a[1]:
            return a[0]
        if a[-1] >= a[-2]:
            return a[-1]
    return find_peak(a[b:])
