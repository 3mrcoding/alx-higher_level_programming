#!/usr/bin/python3
def uniq_add(my_list=[]):
    y = 0
    x = my_list.copy()
    x = list(set(x))
    print(x)
    for i in range(len(x)):
        y += x[i]
    return y
