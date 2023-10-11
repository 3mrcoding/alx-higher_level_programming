#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    x = a_dictionary.copy
    for value in x:
        x[value] *= 2
    return x
