#!/usr/bin/python3
for letter in range(ord('a'), ord('z')):
    if letter == ord('e') or letter == ord('q'):
        continue
    else:
        print("{}".format(chr(letter)), end="")
