#!/usr/bin/python3
def find_max_integer(numbers):
    max_int = float('-inf')  # Initialize with negative infinity

    for num in numbers:
        if isinstance(num, int) and num > max_int:
            max_int = num

    if max_int == float('-inf'):
        print("No integers found in the list")
        return None

    return max_int
