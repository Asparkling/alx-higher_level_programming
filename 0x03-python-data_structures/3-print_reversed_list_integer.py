#!/usr/bin/python3
def print_integers_reversed(numbers):
    for i in range(len(numbers)-1, -1, -1):
        if isinstance(numbers[i], int):
            print(numbers[i])
