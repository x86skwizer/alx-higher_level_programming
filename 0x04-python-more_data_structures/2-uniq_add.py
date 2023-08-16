#!/usr/bin/python3
def uniq_add(my_list=[]):
    n = 0
    new_list = []
    for x in my_list:
        t = 0
        for y in new_list:
            if x == y:
                t = 1
                break
        if t == 1:
            t = 0
            continue
        new_list.append(x)
        n += x
    return n
