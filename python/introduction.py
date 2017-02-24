#!/bin/python3
""" HackerRank 'Python' domain Introduction challenges.

    https://www.hackerrank.com/domains/python/py-introduction
"""

from testing import test_fn


def hello():
    return 'Hello, World!'


def weird_or_not(n):
    """ Python If-Else. """
    result = 'Weird'
    if not n % 2 and (n in range(2, 6) or n > 20):
        result = 'Not Weird'

    return result


def arithmetics(a, b):
    """ Arithmetic Operators. """
    return (a + b, a - b, a * b)


def division(a, b):
    """ (Tom Clancy's the) Division. """
    return (a // b, a / b)


def loops(n):
    """ Loops."""
    result = [i**2 for i in range(n)]
    return result


def is_leap(year):
    """ Write a function. """
    leap = year % 400 == 0 and year % 100 == 0
    leap = leap or year % 4 == 0 and year % 100 != 0
    return leap


if __name__ == '__main__':
    test_fn(hello(), 'Hello, World!')

    # Python If-Else
    test_fn(weird_or_not(3), 'Weird')
    test_fn(weird_or_not(24), 'Not Weird')
    test_fn(weird_or_not(20), 'Weird')

    # Arithmetic Operators
    test_fn(arithmetics(3, 2), (5, 1, 6))

    # Division
    test_fn(division(4, 3), (1, 1.3333333333333333))

    # Loops
    test_fn(loops(5), [0, 1, 4, 9, 16])

    # Write a function
    test_fn(is_leap(1990), False)
    test_fn(is_leap(1992), True)
