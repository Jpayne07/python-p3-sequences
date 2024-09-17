#!/usr/bin/env python3

def print_fibonacci(length):
    list = []
    if length > 0:
        list.append(0)
    if length >=2:
        list.append(1)
        for i in range(2, length):
            list.append(list[-1]+list[-2])
    print(list)
