#!/bin/python3
""" HackerRank 'Python > Strings' challenges.

    https://www.hackerrank.com/domains/python/py-strings
"""
from testing import test_fn


def swap_case(case):
    """ sWAP cASE """
    return case.swapcase()


def split_and_join(a_string):
    """ String Split and Join """
    return '-'.join(a_string.split(' '))


def say_hello(first, last):
    """ What's Your Name? """
    return 'Hello {name}! You just delved into python.'.format(name=' '.join([first, last]))


def replace_at_index(a_string, index, replace_with):
    """ Mutations """
    return a_string[:index] + replace_with + a_string[index + 1:]


def count_substring(string, substring):
    """ Find A String. """
    count = 0
    substring_len = len(substring)
    for i in range(len(string)):
        count += string.count(substring, i, i + substring_len)

    return count

if __name__ == '__main__':
    case = 'Pythonist 3'
    test_fn(swap_case(case), 'pYTHONIST 3')

    # String Split and Join
    a_string = 'this is a string'
    test_fn(split_and_join(a_string), 'this-is-a-string')

    # What's Your Name?
    first, last = 'Guido', 'Rossum'
    test_fn(say_hello(first, last),
            'Hello Guido Rossum! You just delved into python.')

    # Mutations
    a_string, index, replace_with = 'abracadabra', 5, 'k'
    test_fn(replace_at_index(a_string, index, replace_with), 'abrackdabra')

    # Find A String
    string, substring = 'ABCDCDC', 'CDC'
    test_fn(count_substring(string, substring), 2)
