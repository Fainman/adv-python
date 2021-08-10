#!/usr/bin/env python3
"""
Author : John Guerra
Date   : 8/10/2021
Purpose:
"""


def main():

    cities = ['London', 'Madrid', 'New York', 'Ogden']

    print(all(x.istitle() for x in cities))

    # Use built-in zip
    sunday = [12, 14, 15, 15, 17, 21, 22, 22, 23, 22, 20, 18]
    monday = [13, 14, 14, 16, 20, 21, 22, 22, 21, 19, 18, 16]
    tuesday = [12, 13, 14, 16, 20, 20, 21, 20, 19, 16, 14, 12]

    for sun, mon, tue in zip(sunday, monday, tuesday):
        print(f'The average = {(sun + mon + tue)/2}, The minimum = {min(sun, mon, tue)}, The maximum = {max(sun, mon, tue)}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
