#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return None
    for i in sentence:
        return (len(sentence), i)
