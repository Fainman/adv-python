#!/usr/bin/env python3
"""
Author : John Guerra
Date   : 8/11/2021
Purpose: Working with files
"""
import sys


# --------------------------------------------------
def main():
    """Make your noise here"""
    print(sys.getdefaultencoding())
    # Writing text files
    # f = open('wasteland.txt', mode='wt', encoding='utf-8')
    # f.write('This is the first line of text I have here.\n')
    # f.write('But, I can write more lines if I need to do it.\n')
    # f.close()

    # Reading files part at a time
    # g = open('wasteland.txt', mode='rt', encoding='utf-8')
    # info = g.read(27)
    # print(info)
    # info = g.read() # read the rest
    # print(info)
    # print(f'[{info}]')
    # g.close()

    # Reading all lines
    # g = open('wasteland.txt', mode='rt', encoding='utf-8')
    # info = g.readlines()
    # print(info)
    # g.close()

    # Appending text to files
    f = open('wasteland.txt', mode='at', encoding='utf-8')
    f.write('This is the first line of text I have here.\n')
    f.write('But, I can write more lines if I need to do it.\n')
    f.close()

# --------------------------------------------------
if __name__ == '__main__':
    main()
