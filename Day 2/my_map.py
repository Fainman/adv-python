#!/usr/bin/env python3
"""
Author : John Guerra
Date   : 8/10/2021
Purpose: Review the map() function
"""


def combine(size, color, animal):
    return f'{size} {color} {animal}'


def five():
    for i in range(5):
        return i


# --------------------------------------------------
def main():
    """Make your noise here"""
    # Map() is lazy. It only produces the values as they are needed
    # ord: unicode value
    m = map(ord, "The purple Weber State")
    print(list(m))

    # Multiple mapping
    sizes = ['small', 'medium', 'large']
    colors = ['green', 'blue', 'red']
    animals = ['cow', 'dog', 'cat']

    # Create a list from the map
    print(list(map(combine, sizes, colors, animals)))

    # Comprehension
    print([str(i) for i in range(5)])
    print(list(map(str, range(5))))

    # Generator
    print(list(str(i) for i in range(5)))
    # Map
    print(list(map(str, range(5))))


# --------------------------------------------------
if __name__ == '__main__':
    main()
