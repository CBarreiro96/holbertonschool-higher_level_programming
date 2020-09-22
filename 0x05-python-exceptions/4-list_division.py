#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    index = 0
    for i in range(list_length):
        try:
            x = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            index = 1
        except TypeError:
            print("wrong type")
            index = 1
        except IndexError:
            print("out of range")
            index = 1
        finally:
            if index:
                index = 0
                new_list.append(0)
            else:
                new_list.append(x)
    return new_list
