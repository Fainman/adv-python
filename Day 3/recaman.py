#!/usr/bin/env python3
"""
Author : John Guerra
Date   : 8/11/2021
Purpose: Create a Recaman sequence
"""
from itertools import count, islice
import sys


def sequence():
    """Recaman sequence:
    a_0 = 0,
    a_n = a_(n-1) - n: if result is positive and not already in the list and a_n=a_(n-1) - n
    a_n = a_(n-1) + n: otherwise
    example: 0, 1, 3, 6, 2, 7, 13, 20, 12, 21, 11, 22, 10, 23"""

    seen = set()
    a = 0
    for n in count(1):
        yield a
        seen.add(a)
        c = a - n
        if c < 0 or c in seen:
            c = a + n
        a = c


def write_sequence(filename, num):
    """
    Write the Recaman series
    :param filename: file name
    :param num: maximum numbers to write
    :return: nothing
    """
    with open(filename, mode='wt', encoding='utf-8') as f:
        # Generate list and Write list
        f.writelines([f'{x}\n' for x in islice(sequence(), num)])


def read_series(filename):
    with open(filename, mode='rt', encoding='utf-8') as f:
        series = [int(line.strip()) for line in f]
    return series


# --------------------------------------------------
def main():
    """Make your noise here"""
    #print(write_sequence('test.txt', 10))
    write_sequence('test.txt', 10)

# --------------------------------------------------
if __name__ == '__main__':
    main()
