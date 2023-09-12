#!/usr/bin/python3
'''verifies if an obj is an instance of a class or its superclass'''


def is_kind_of_class(obj, a_class):
    '''returns true if obj isinstance of a_class or a_class parent'''
    return isinstance(obj, a_class)
