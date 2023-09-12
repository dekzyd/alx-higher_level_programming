#!/usr/bin/python3
'''creates a square class'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''creates a square object'''

    def __init__(self, size):
        '''creates a square with a size'''
        self.__size = size

        Rectangle.integer_validator(self, "size", self.__size)

    def area(self):
        '''gets area of square'''
        return self.__size ** 2

    def __str__(self):
        '''prints'''
        return ("[Square] " + str(self.__size) + "/" + str(self.__size))
