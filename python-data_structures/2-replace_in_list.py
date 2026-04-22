#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    my_list = mylist.replace(idx, element)
    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list
    return my_list
