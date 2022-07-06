#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == 0:
        return None
    else:
        new_tuple = (len(sentence), sentence[0])
        return new_tuple
