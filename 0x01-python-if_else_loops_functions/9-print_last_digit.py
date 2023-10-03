#!/usr/bin/python3
def print_last_digit(number):
    lD = abs(number) % 10
    print("{}".format(lD), end='')
    return (lD)
