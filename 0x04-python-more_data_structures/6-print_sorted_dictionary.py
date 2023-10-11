#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    x = a_dictionary.copy()
    x = dict(sorted(a_dictionary.items()))
    for i, y in x.items():
        print(f"{i}: {y}")
