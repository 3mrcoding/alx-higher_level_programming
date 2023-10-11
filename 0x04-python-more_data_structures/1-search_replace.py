#!/usr/bin/python3
def search_replace(my_list, search, replace):
    x = my_list.copy()
    for i in range(len(x)):
        if x[i] == search:
            x[i] = replace
    return x
