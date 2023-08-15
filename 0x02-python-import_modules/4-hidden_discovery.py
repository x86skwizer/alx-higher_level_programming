#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    arr = dir(hidden_4)
    for s in arr:
        if s[:2] != "__":
            print(s)
