#!/usr/bin/python3
import sys
result = 0
for i in range(1, len(sys.argv)):
    result += int(sys.argv[i])
print("{}".format(result))
