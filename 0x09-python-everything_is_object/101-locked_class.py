#!/usr/bin/python3
"""Write a class LockedClass with no class or object attribute,
that prevents the user from dynamically creating new instance attributes,
except if the new instance attribute is called first_name.

You are not allowed to import any module"""


class LockeClass:
    """
    Only allows instantiation of an attribute called first_name
    """

    __slots__ = ["first_name"]
