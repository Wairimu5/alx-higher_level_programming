#!/usr/bin/python3

# a function that replaces an element in a list at a specific position without modifying the original list

def new_in_list(my_list, idx, element):
    # Check if idx is out of range or negative
    if idx < 0 or idx >= len(my_list):
        # Return a copy of the original list
        return my_list.copy()

    # Create a copy of the original list
    new_list = my_list.copy()

    # Replace the element at the specified index with the new element
    new_list[idx] = element

    # Return the modified copy of the list
    return new_list
