#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arg_len = len(argv) - 1
    if arg_len == 0:
        print("{} arguments.".format(arg_len))
    elif arg_len == 1:
        print("{} argument:".format(arg_len))
        print("{}: {}".format(arg_len, argv[arg_len]))
    else:
        print("{} arguments:".format(arg_len))
        for i in range(1, arg_len + 1):
            print("{}: {}".format(i, argv[i]))
