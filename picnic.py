#!/usr/bin/env python3
"""
Author : John Guerra
Date   : 8/9/2021
Purpose: Program that sets multiple positional arguments. Could be one or could be many. List of items that
are being brought to the picnic
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('item',
                        metavar='str',
                        nargs='+',                  # One or more arguments
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        help='sort the items',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make your noise here"""

    args = get_args()
    print(args.item)
    items = args.item

    # Check if the list needs to be sorted
    if args.sorted:
        items.sort()

    # Prepare list to print
    num_items = len(args.item)

    # 0 Items, print 'nothing'
    if num_items == 0:
        bringing = 'nothing'

    # 1 Item, just print the item
    elif num_items == 1:
        bringing = args.item[0]

    # 2 Items: item1 and item2
    elif num_items == 2:
        bringing = ' and '.join(args.item)

    # 3 or more Items: item1, item2, itemX, and itemLast
    else:
        args.item[-1] = 'and ' + args.item[-1]
        bringing = ', '.join(args.item)

    # Print info
    print(f'You are bringing {bringing}')
# --------------------------------------------------


if __name__ == '__main__':
    main()
