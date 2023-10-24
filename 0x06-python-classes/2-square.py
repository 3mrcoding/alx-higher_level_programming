#!/usr/bin/python3
""" Working on oop with python """


class Square():
    """Class representing a square"""

    def __init__(self, size=0):
        """ initialize the class

        Args:
           size (int): size of the square
        """
        self.__size = size

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
