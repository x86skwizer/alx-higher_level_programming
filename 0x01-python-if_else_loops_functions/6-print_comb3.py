#!/usr/bin/python3
for t in range(10):
    for o in range(t + 1, 10):
        if t < 8:
            print("{:d}{:d}, ".format(t, o), end="")
        else:
            print("{:d}{:d}".format(t, o))
