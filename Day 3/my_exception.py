#!/usr/bin/env python3
"""
Author : John Guerra
Date   : 8/11/2021
Purpose: Review Exceptions
"""
from random import randrange


# --------------------------------------------------
def main():
    """Make your noise here"""
    # Random number between 0-99
    number = randrange(100)
    while True:
        try:
            guess = int(input('guess number?'))
        except ValueError:
            continue
        if guess == number:
            print('You got it!')
            break





# --------------------------------------------------
if __name__ == '__main__':
    main()
