#!/usr/bin/python3
'''inherits from List'''


class MyList(list):
    '''class inherits from list'''

    def __init__(self, *args):
        super().__init__(self, *args)

    def print_sorted(self):
        '''prints sorted (ASC) list'''

        print(sorted(self))
