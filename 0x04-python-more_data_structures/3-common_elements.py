#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_set = []
    for x in set_1:
        for y in set_2:
            if x == y:
                new_set.append(x)
    return new_set
