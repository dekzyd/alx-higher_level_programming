#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_len = len(sys.argv)
    sum = 0

    if arg_len <= 1:
        pass
    elif arg_len == 2:
        sum += int(sys.argv[1])
    else:
        for num in range(1, arg_len):
            sum += int(sys.argv[num])

    print(sum)
