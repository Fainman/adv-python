#!/usr/bin/env python3
"""
Author : t19 <me@wsu.com>
Date   : 8/9/2021
Purpose: Review Tuples
"""


def minmax(items):
    """
    Return the maximum and minimum of the collection
    :param items: collection of objects
    :return: min and max
    """
    return min(items), max(items)


def main():
    """Make your noise here"""
    # A tuple of any kind of object
    t = ("Ogden", 1.99, 2)
    # t = "Ogden", 1.99, 2 # Python assumes this is a tuple
    print(t)
    print(t[0])
    print(t[1])


# --------------------------------------------------
if __name__ == '__main__':
    # main()
    items = (3, 88, 11, 22, 90)
    min, max = minmax(items)
    print(f"Minimum: {min} Maximum: {max}")
