#!/usr/bin/python3
def best_score(a_dictionary):
    x = a_dictionary.copy()
    x = list(x.values())
    if len(x) == 0:
        return None
    x.sort(reverse=True)
    return x[0]
