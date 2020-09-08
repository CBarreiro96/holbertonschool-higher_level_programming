#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is None:
        return
    my_list2 = my_list[:]
    if (0 <= idx < len(my_list)):
        my_list2[idx] = element
    else:
        return(my_list)
    return(my_list2)
