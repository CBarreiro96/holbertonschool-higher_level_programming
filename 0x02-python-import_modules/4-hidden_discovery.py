#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    Dir_to_show = dir(hidden_4)
    Symbol_to_avoid = "__"
    for i in range(0, len(Dir_to_show)):
        if Symbol_to_avoid not in Dir_to_show[i]:
            print(Dir_to_show[i])
