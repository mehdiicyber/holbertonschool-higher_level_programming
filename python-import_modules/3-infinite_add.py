#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]
    list = []
    for i in argv:
        i = int(i)
        list.append(i)
    print(sum(list))
