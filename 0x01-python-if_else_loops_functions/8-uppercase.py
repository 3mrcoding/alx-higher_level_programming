#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) in range(65, 91):
            print("{}".format(c), end='')
        elif ord(c) in range(97, 123):
            print("{}".format(chr(ord(c) + 32)), end='')
