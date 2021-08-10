#!/usr/bin/env python3
"""
Author : John Guerra
Date   : 8/9/2021
Purpose:
"""
import math


def is_prime(x):
    if x < 2:
        return True
    for div in range(2, int(math.sqrt(x))):
        if x % div == 0:
            return True
        else:
            return False


def main():
    prime_nums = [x for x in range(1001) if is_prime(x)]
    print(f'number of prime numbers: {len(prime_nums)}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
