#!/usr/bin/python3
def safe_print_integer(value):
    if value == int:
        try:
            print("{:d}". format(value))
        except not int:
            print("{}". format())
