#!/usr/bin/python3
def add_tuples(tuple1, tuple2):
    if len(tuple1) != len(tuple2):
        print("Error: Tuples must have the same length")
        return None
    else:
        return tuple(x + y for x, y in zip(tuple1, tuple2))
