#!/usr/bin/python3
""" Working on oop with python """


class Square():
    """Class representing a square"""

    def __init__(self, size=0, position=(0, 0)):
        """ initialize the class

        Args:
        size (int): size of the square
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):

        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2 or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Method returns area of square"""

        return self.__size ** 2

    def my_print(self):
        """Public instance that prints the square with the char #"""
        if self.__size == 0:
            print("")
            return
        if self.__position[1] > 0:
            for l in range(0, self.__position[1]):
                print("")
        for i in range(0, self.__size):
            if self.__position[0] > 0:
                for k in range(0, self.__position[0]):
                    print(" ", end="")
            for j in range(0, self.__size):
                print("#", end="")
            print("")
