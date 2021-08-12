#!/usr/bin/env python3
"""
Author : hvalle <me@wsu.com>
Date   : 8/12/2021
Purpose: Function that return functions
"""


def enclosing():
    x = 'close over'
    def local_func():
        print(x)
    return local_func    # no ()


def test_enclosing():
    lf = enclosing()
    lf()
    print(lf.__closure__)


# --------------------------------------------------
def main():
    """Make your noise here"""
    test_enclosing()



# --------------------------------------------------
if __name__ == '__main__':
    main()
