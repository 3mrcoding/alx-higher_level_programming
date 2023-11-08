#!/usr/bin/python3

"""function to write to a file"""


def write_file(filename="", text="", encoding="utf-8"):

    """function to write to a file"""

    with open(filename, "w") as file:
        return file.write(text)
