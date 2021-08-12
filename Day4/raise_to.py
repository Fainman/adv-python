#!/usr/bin/env python3
"""
Author : hvalle <me@wsu.com>
Date   : 8/12/2021
Purpose: Function Factory
"""


def raise_to(exp):
    def raise_to_exp(x):
        return pow(x, exp)
    return raise_to_exp # no ()


# --------------------------------------------------
def main():
    """Make your noise here"""
    square = raise_to(2)
    print(square.__closure__)
    print(square(5))
    print(square(9))
    #
    cube = raise_to(3)
    print(cube.__closure__)
    print(cube(5))
    print(cube(10))


# --------------------------------------------------
if __name__ == '__main__':
    main()
