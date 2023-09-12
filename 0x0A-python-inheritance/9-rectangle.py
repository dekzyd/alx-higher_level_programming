#!/usr/bin/python3
'''Rectangle class'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''inherits from BaseGeometry'''

    def __init__(self, width, height):
        super().integer_validator("width", width)
        BaseGeometry.integer_validator(self, "height", height)

        self.__width = width
        self.__height = height

    def area(self):
        '''gives the area of the rectangle'''
        return self.__width * self.__height

    def __str__(self):
        """ print """
        return ("[Rectangle] " + str(self.__width) + "/" + str(self.__height))
