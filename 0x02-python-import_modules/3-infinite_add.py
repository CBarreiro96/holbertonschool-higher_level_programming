#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    Result = 0
    Number = len(argv)
    for i in range(1, Number):
        Result += int(argv[i])
    print("{:d}".format(Result))
