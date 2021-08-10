#!/usr/bin/env python3
"""
Author : John Guerra
Date   : 8/10/2021
Purpose:
"""
from math import sqrt, dist


class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def calculate_distance(self, other_point):
        return sqrt((self._x - other_point._x)**2 +
                    (self._y - other_point._y)**2)

    def reset(self):
        self.move(0,0)

    def move(self, x, y):
        self._x = x
        self._y = y


def main():
    """Make your noise here"""
    p1 = Point()
    p2 = Point(-9, 3)

    print(p1._x, p1._y)
    print(p2._x, p2._y)
    p2.reset()
    print(p2._x, p2._y)
    p2.move(3,3)
    print(p2._x, p2._y)
    print(p1.calculate_distance(p2))

if __name__ == '__main__':
    main()
