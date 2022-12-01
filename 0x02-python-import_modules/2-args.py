#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_len = len(sys.argv) - 1

    if arg_len == 0:
        print("{} arguments.".format(arg_len))
    elif arg_len == 1:
        print("{} argument:".format(arg_len))
        print("{}: {}".format(arg_len, sys.argv[1]))
    else:
        print("{} arguments:".format(arg_len))
        for num in range(1, arg_len + 1):
            print("{}: {}".format(num, sys.argv[num]))

