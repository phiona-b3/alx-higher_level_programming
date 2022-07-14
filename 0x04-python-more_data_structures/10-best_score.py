#!/usr/bin/python3
def best_score(a_dictionary):
    max_value = 0
    max_key = ""
    if a_dictionary is None:
        return None
    for key in a_dictionary.keys():
        if a_dictionary[key] > max_val:
            max_val = a_dictionary[key]
            max_key = key
