#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    Number = len(sys.argv)
    if(Number <= 1):
        print("0 arguments.")
    else:
        if Number == 2:
            print("{:d} argument:".format(Number-1))
        else:
            print("{:d} argument:".format(Number-1))
            for i in range(1, Number):
                print("{:d}: {}".format(i, sys.argv[i]))
