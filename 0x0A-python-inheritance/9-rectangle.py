#!/usr/bin/python3
'''Rectangle class'''


BaseGeometry = __import__(7-base_geometry).BaseGeometry


class Rectangle(BaseGeometry):
    '''inherits from BaseGeometry'''

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.width = width
        self.height = height

    def area(self):
        '''gives the area of the rectangle'''
        return self.width * self.height

    def __str__(self):
        """ print """
        return ("[Rectangle] " + str(self.__width) + "/" + str(self.__height))
