#!/usr/bin/env python3
"""
Author : John Guerra
Date   : 8/9/2021
Purpose:
"""
import math
from itertools import islice, count


def is_prime(x):
    if x < 2:
        return True
    for div in range(2, int(math.sqrt(x))):
        if x % div == 0:
            return True
        else:
            return False


def fib_gen():
    a = 1
    b = 1
    yield a
    yield b
    while True:
        yield a + b
        a, b = b, a + b


def main():
    """Make your noise here"""
    k_sq_sum = sum(x * x for x in range(1001))
    print(k_sq_sum)

    one_k_prime_sum = sum(x for x in range(1001) if is_prime(x))
    print(one_k_prime_sum)

    one_k_prime_sum_2 = sum(islice((x for x in count() if is_prime(x)), 1000))
    print(one_k_prime_sum_2)




# --------------------------------------------------
if __name__ == '__main__':
    main()
