#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """Represents a square
    Attributes:
        __size (int): size of the side of a square
    """
    def __init__(self, size=0):
        """Initializes a square
        Args:
            size (int): size of a side of the square
        Returns:
            None
        """
        if isinstance(size, int):
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """Calculates area of square
        Args:
            None
        Returns:
            Area of the square.
        """
        return self.__size ** 2
