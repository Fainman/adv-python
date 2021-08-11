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

    def __iter__(self):
        """Iter Protocol"""
        return iter(self._items)

    def __getitem__(self, index):
        """Index Protocol"""
        print(index)
        print(type(index))
        result = self._items[index]
        return SortedSet(result) if isinstance(index, slice) else result

    def __repr__(self):
        return 'SortedSet({})'.format(repr(self._items) if self._items else '')

    def __eq__(self, other):
        """If not instance return NoImplemented
        rather than raise NoImplementation Error"""
        if not isinstance(other, SortedSet):
            return NotImplemented
        return self._items == other._items

    def __ne__(self, other):
        """If not instance return NoImplemented
                rather than raise NoImplementation Error"""
        if not isinstance(other, SortedSet):
            return NotImplemented
        return self._items != other._items


#-------------------------------------------------
def main():
    pass


#-------------------------------------------------
if __name__ == '__main__':
    main()
