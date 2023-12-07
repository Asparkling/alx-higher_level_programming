#!/usr/bin/python3
def get_length_and_first_char(string):
    if len(string) == 0:
        print("Error: String is empty")
        return None
    else:
        return len(string), string[0]
