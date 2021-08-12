#!/usr/bin/env python3
"""
Author : John Guerra
Date   : 8/12/2021
Purpose: Explore numpy
"""
import numpy as np


def np_arrays():
    array_one = np.array([1, 2, 3, 4])
    print(array_one)
    print(type(array_one))
    numbers = [9, 7, 10, 12]
    print(numbers, type(numbers))
    array_two = np.array(numbers)
    print(array_two, type(array_two))

    # Create arrays with initial placeholders
    array_of_zeros = np.zeros((3, 4))
    print(array_of_zeros)
    array_of_empty = np.empty((3, 4))


# --------------------------------------------------
def main():
    """Make your noise here"""
    np_arrays()

# --------------------------------------------------
if __name__ == '__main__':
    main()
