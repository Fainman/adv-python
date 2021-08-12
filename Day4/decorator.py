#!/usr/bin/env python3
"""
Author : hvalle <me@wsu.com>
Date   : 8/12/2021
Purpose: Basics of decorators
"""


def outer_function(msg):
    message = msg

    def inner_function():
        print(message)

    return inner_function  # no ()


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f'Wrapper executed this before {original_function.__name__}')
        return original_function(*args, **kwargs)  # the execution of the function
    return wrapper_function


@decorator_function
def display():
    print(f'Display function ran')

# This will not work with the current decorator
# unless you make sure pass all the parameter
@decorator_function
def display_info(name, age):
    print(f'Display function ran for {name} {age}')

# --------------------------------------------------
def main():
    """Make your noise here"""
    hi_func = outer_function('Hi')
    bye_func = outer_function('Bye')
    hi_func()
    bye_func()
    # without Decorator
    # decorated_display = decorator_function(display)
    # decorated_display()
    # With Decorator
    display()
    display_info('Waldo', 21)


# --------------------------------------------------
if __name__ == '__main__':
    main()
