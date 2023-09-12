#!/usr/bin/python3
'''checks if obj is a subclass of a_class'''


def inherits_from(obj, a_class):
    '''returns true or false if obj is a subclass of a_class'''
    return isinstance(obj, a_class) and type(obj) != a_class
