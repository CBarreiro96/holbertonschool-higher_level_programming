#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print("{:d}".format(my_list[i]), end= "")
    except IndexError:
        return 1
    else:
        return x
    finally:
        print(" ")