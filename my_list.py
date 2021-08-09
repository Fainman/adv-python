#!/usr/bin/env python3
"""
Author : John Guerra
Date   : 8/9/2021
Purpose: Review list
"""

def main():
    """Review lists"""
    r = [4, -2, 10, -18, 22]
    # Slicing
    print(r[2:6])

    # Shallow copy list
    t = r
    print(f'Is t pointing to the same memory location as r? {t is r}')

    # Deep copy list (poor performance)
    t = r[:]
    print(f'Is t pointing to the same memory location as r? {t is r}')

    # Deep copy list (preferred performance)
    t = r.copy()
    print(f'Is t pointing to the same memory location as r? {t is r}')
    print(f'Is t equivalent to r? {t == r}')

# --------------------------------------------------
if __name__ == '__main__':
    main()
