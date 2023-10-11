#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    x = a_dictionary.copy()
    x = list(x.values())
    x.sort(reverse=True)
    return x[0]
