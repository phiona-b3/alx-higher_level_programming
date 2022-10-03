#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        c = a / b
        print("{} / {} = {}".format(a, b, c))
    except ValueError:
        print("inside result: {}".format())
    except ZeroDivisionError:
        print("inside result: {}".format())
    finally:
        print("inside result: {}".format(c))
