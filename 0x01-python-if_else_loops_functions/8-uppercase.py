#!/usr/bin/python3
def uppercase(str):
    newstr = ""
    for i in str:
        if str(ord([i])) >= 97 and str(ord([i])) <= 122:
            upper = chr((ord(str[i] - 32)))
        else:
            upper = str[i]
        newstr += upper
        print("{}".format(newstr))
