#!/usr/bin/python3
def max_integer(my_list=[]):
    x = my_list[0]
    if len(my_list) == 0:
        return None
    else:
        for i in range(len(my_list)):
            if my_list[i] > x:
                x = my_list[i]
            else:
                pass
            return x
