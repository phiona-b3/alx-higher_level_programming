#!/usr/bin/python3

if __name__ == "__main__":
    """ prints the number of and the list of its arguments"""
import sys

count = len(sys.argv) - 1
if count == 0:
    print("{} arguments.".format(count))
elif count == 1:
    print("{} argument:".format(count))
else:
    print("{} arguments:".format(count))
for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
