#!/usr/bin/python3
def raise_exception_msg(message=""):
    try:
        print(message)
    except NameError:
        print(message)
