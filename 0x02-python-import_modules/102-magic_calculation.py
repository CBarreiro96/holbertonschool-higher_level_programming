#!/usr/bin/python3
<<<<<<< HEAD
import dis
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub

    if a < b :
        c = add(a, b)
    for i in range(4, 6):
        c = add(c, i)
    return c
    else:
        return sub(a, b)
dis.dis(magic_calculation)
=======
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)
>>>>>>> d7d4ca6eca38dac34fb8f062c820da14479f4bb3
