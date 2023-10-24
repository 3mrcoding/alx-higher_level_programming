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

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Method returns area of square"""

        return self.__size ** 2

    def my_print(self):
        """Method prints area of square"""

        i = self.__size
        if i > 0:
            while i > 0:
                print(f"{'#' * self.__size}")
                i -= 1
        elif self.__size == 0:
            print("")
