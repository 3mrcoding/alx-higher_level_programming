#!/usr/bin/python3
def best_score(a_dictionary):
    x = a_dictionary.copy()
    x = list(x.values())
    x.sort(reverse=True)
    return x[0]
