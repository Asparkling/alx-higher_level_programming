#!/usr/bin/python3
def replace_element(my_list, index, new_element):
    if index < 0 or index >= len(my_list):
        print("Index out of range")
    else:
        my_list[index] = new_element
