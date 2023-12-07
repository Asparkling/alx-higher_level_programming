#!/usr/bin/python3
def replace_element_copy(my_list, index, new_element):
    if index < 0 or index >= len(my_list):
        print("Index out of range")
        return my_list  # Return the original list
    else:
        # Create a copy of the list
        new_list = my_list[:]
        # Replace the element at the specified index in the copy
        new_list[index] = new_element
        return new_list
