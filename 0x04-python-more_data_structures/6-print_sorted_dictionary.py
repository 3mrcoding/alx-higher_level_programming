#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    x = a_dictionary.copy()
    x = sorted(a_dictionary.items())
    for i in range(len(x)):
        print("{}".format(x[i]))
