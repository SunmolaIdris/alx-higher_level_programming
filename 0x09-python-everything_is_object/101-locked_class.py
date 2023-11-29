#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    This class prevents the user from creating an instance of new LockedClass with attributes
    other than 'first_name'.
    """

    __slots__ = ["first_name"]
