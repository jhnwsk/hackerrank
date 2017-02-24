#!/bin/python3
""" HackerRank 'Algorithms' domain Warmup challenges.

    https://www.hackerrank.com/domains/algorithms/implementation
"""

import pdb
from testing import test_fn


def find_non_divisible_subset_length(S, k):
    """ Non-Divisible Subset.

    args:
        S - the set to search in
        k - elements in subset should not be divisible by this

    """
    modulos = {i: 0 for i in range(k)}
    for s in S:
        modulo = s % k
        modulos[modulo] += 1

    result = min(modulos[0], 1)  # elements evenly divisible cannot be paired
    if k % 2 == 0:              # theres a 'center element' can be added only once
        result += 1

    for m in range(1, k // 2 + 1):
        if m != k - m:
            result += max(modulos[m], modulos[k - m])

    return result


def count_letters_in_repeated_string(s, n):
    s_length = len(s)
    multiply = n // s_length
    additional_letters = n % s_length
    search = s.count('a') * multiply
    search += s[:additional_letters].count('a')
    return search


if __name__ == '__main__':
    # Non-Divisible Subset
    S, k = [1, 7, 2, 4], 3
    test_fn(find_non_divisible_subset_length(S, k), 3)
    S, k = [1, 2, 3, 4, 5], 1
    test_fn(find_non_divisible_subset_length(S, k), 1)
    S, k = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4
    test_fn(find_non_divisible_subset_length(S, k), 5)

    # Repeated string
    s, n = 'aba', 10
    test_fn(count_letters_in_repeated_string(s, n), 7)
    s, n = 'a', 1000000000000
    test_fn(count_letters_in_repeated_string(s, n), 1000000000000)
