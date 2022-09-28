#!/usr/bin/python3
def uniq_add(my_list=[]):
    """adds all unique integers in a list (0nly once for each integer)"""
    uniq_list = set(my_list)
    num = 0

    for i in uniq_list:
        num += i

    return (num)
