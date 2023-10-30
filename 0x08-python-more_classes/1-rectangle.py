#!/usr/bin/python3

"""python class file"""


class Rectangle:
    """class of a rectangle"""
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """getter method of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter method of width"""
        if value < 0:
            raise ValueError("width must be >= 0")
        elif not isinstance(value, int):
            raise TypeError("width must be an integer")
        else:
            self.__width = value

    @property
    def height(self):
        """getter method of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter method for height"""
        if value < 0:
            raise ValueError("height must be >= 0")
        elif not isinstance(value, int):
            raise TypeError("height must be an integer")
        else:
            self.__height = value
