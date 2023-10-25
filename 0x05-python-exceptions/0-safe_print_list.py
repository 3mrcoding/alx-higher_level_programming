#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    k = 0
    len = 0
    for k in my_list:
        k += 1
        len += 1

    try:
        if x > len:
            x = len
        if len == 0:
            return 0
        elif x == 0:
            print(f"{my_list[0]}", end="")
        for i in range(0, x):
            print(f"{my_list[i]}", end="")
        print("")
        return (i + 1)

    except ValueError:

        if x < 0 and type(x) != int:
            return 0
