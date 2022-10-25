#!/usr/bin/python3

"""Defines an inherited list Class MyList"""


class MyList(list):
    """a subclass of list"""

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt")
