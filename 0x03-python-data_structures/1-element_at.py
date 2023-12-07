#!/usr/bin/python3
def get_element(my_list, index):
    if index < 0 or index >= len(my_list):
        print("Index out of range")
        return None
    else:
        return my_list[index]
