#!/usr/bin/python3
"""Module for MyInt class"""


class MyInt(int):
    """subclass MyInt"""

    def __eq__(self, other):
        """override equals, inverting it"""
        return int(self) != int(other)

    def __ne__(self, other):
        """overrides not_equals, inverting it"""
        return int(self) == int(other)
