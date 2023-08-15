#!/usr/bin/python3
import sys
if __name__ == '__main__':
    i = 1
    n = 0
    while i < len(sys.argv):
        n += int(sys.argv[i])
        i += 1
    print("{:d}".format(n))
