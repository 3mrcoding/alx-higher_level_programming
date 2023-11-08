#!/usr/bin/python3

"""function file to read a file in the working dir"""


def read_file(filename=""):

    """function reads a file"""

    with open(filename, "r", encoding="UTF8") as file:
        print(file.read())
