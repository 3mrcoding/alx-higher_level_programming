#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    n = len(sys.argv)
    if n == 2:
        print("{} argument:".format(n-1))
        print("1: {}".format(sys.argv[1]))
    elif n == 1:
        print("0 arguments.")
    else:
        print("{} arguments:".format(n-1))
        for i in range(1, n):
            print("{}: {}".format(i, sys.argv[i]))
