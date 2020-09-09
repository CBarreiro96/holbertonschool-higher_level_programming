#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return
    my_list2 = []
    for n in my_list:
        if n % 2 == 0:
            my_list2.append(True)
        else:
            my_list2.append(False)
    return my_list2
