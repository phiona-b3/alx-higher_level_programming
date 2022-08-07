#!/usr/bin/python3
import sys

sum = 0
for i in range(0, len(sys.argv)):
    sum += int(sys.argv[i])
print("{}".format(sum))
