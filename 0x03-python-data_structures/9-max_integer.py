#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == " ":
        return "None"
    else:
        my_list.sort()
        print("Max: {}".format(my_list[-1]))

        max_value = 0
        for num in my_list:
            if num > max_value:
                max_value = num
        return max_value
