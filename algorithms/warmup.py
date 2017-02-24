#!/bin/python3
""" HackerRank 'Algorithms' domain Warmup challenges.

    https://www.hackerrank.com/domains/algorithms/warmup
"""
from testing import test_fn


def compare_triplets(triplet_A, triplet_B):
    """ Compare the Triplets. """

    scores = {'alice': 0, 'bob': 0}
    zipped_triplets = zip(triplet_A, triplet_B)
    for pair in zipped_triplets:
        if pair[0] > pair[1]:
            scores['alice'] += 1
        elif pair[0] < pair[1]:
            scores['bob'] += 1
    return '{alice} {bob}'.format(alice=scores['alice'], bob=scores['bob'])


def rotate_circulary(array, k):
    """ Circular Array Rotation. """
    k %= len(array)  # n can be higher than the array length and then... boom!
    return array[-k:] + array[:-k]


if __name__ == '__main__':
    # compare_triplets
    # test_fn('1 1', compare_triplets((5, 6, 7), (3, 6, 10)))

    # circular array rotation
    test_fn(2, rotate_circulary([1, 2, 3], 2)[0])
    test_fn(3, rotate_circulary([1, 2, 3], 2)[1])
    test_fn(1, rotate_circulary([1, 2, 3], 2)[2])
