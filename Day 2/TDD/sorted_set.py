#!/usr/bin/env python3
"""
Author : John Guerra
Date   : 8/10/2021
Purpose: Sorted Set Class
"""

class SortedSet:
    def __init__(self, items=None):
        """
        Create a sorted list, regardless of which iterable object you pass
        :param items: list of items
        """
        self._items = sorted(set(items)) if items is not None else []

    def __contains__(self, item):
        """Container Protocol"""
        return item in self._items

    def __len__(self):
        """Length Protocol"""
        return len(self._items)


#-------------------------------------------------
def main():
    pass


#-------------------------------------------------
if __name__ == '__main__':
    main()
