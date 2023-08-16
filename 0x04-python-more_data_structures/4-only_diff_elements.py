#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = []
    for x in set_1:
        t = 0
        for y in set_2:
            if x == y:
                t = 1
                break
        if t == 1:
            continue
        new_set.append(x)
    for x in set_2:
        t = 0
        for y in set_1:
            if x == y:
                t = 1
                break
        if t == 1:
            continue
        new_set.append(x)
    return new_set
