#!/usr/bin/env python3
"""
Author : John Guerra
Date   : 8/11/2021
Purpose: Detecting callable objects
"""


def is_even(num):
    return num % 2 == 0


class CallMe:
    def __call__(self):
        print("Called!")


# --------------------------------------------------
def main():
    """Make your noise here"""
    print(callable(is_even))
    is_odd = lambda num: num % 2 != 0
    print(callable(is_odd))
    print(callable(CallMe))


# --------------------------------------------------
if __name__ == '__main__':
    main()
