""" HackerRank 'Algorithms' domain Warmup challenges.

    https://www.hackerrank.com/challenges/mini-max-sum
"""
from string import ascii_lowercase


def test_fn(actual, expected):
    print(expected, actual, expected == actual)


def mini_max_sum(integers):
    """ Mini-Max Sum. """
    sorted_integers = sorted(integers)
    mini = sum(sorted_integers[:-1])
    maxi = sum(sorted_integers[1:])

    return '{mini} {maxi}'.format(mini=mini, maxi=maxi)


def find_area(word, letter_heights):
    """ Designer PDF Viewer. """
    lenmap = {a[0]: a[1] for a in zip(ascii_lowercase, letter_heights)}
    return len(word) * max((lenmap[a] for a in word))


def find_fruit_on_house(house, tree, fall_distances):
    """ Apples and Oranges."""
    score = 0
    for d in fall_distances:
        if house[0] <= tree + d <= house[1]:
            score += 1
    return score


def check_if_kangaroos_meet(kangaroos):
    """ Kangaroos.

        The real answer is 'YES if (x1-x2)%(v1-v2)==0'
        Always look for functional solution before a procedural one.
    """
    result = 'NO'

    def sorted_kangaroos(kangaroos):
        return sorted(kangaroos, key=lambda x: x[0]), sorted(kangaroos, key=lambda x: x[1])

    kanga_distance, kanga_speed = sorted_kangaroos(kangaroos)

    while kanga_distance != kanga_speed:
        distances = [k[0] for k in kanga_distance]
        if len(distances) != len(set(distances)):
            result = 'YES'
        for k in kangaroos:
            k[0] += k[1]

        kanga_distance, kanga_speed = sorted_kangaroos(kangaroos)

    return result


def find_betweens(A, B):
    """ Between two sets.

        I assume that it is possible to find elements.
    """
    a, b = max(A), min(B)
    result = []
    for p in range(a, b + 1):
        if all(p % x == 0 for x in A) and all(x % p == 0 for x in B):
            result.append(p)
    return len(result)


if __name__ == '__main__':
    # Mini-Max Sum
    # test_fn(mini_max_sum([1, 2, 3, 4, 5]), '10 14')

    # Designer PDF Viewer
    letter_heights = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5,
                      5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    # test_fn(find_area('abc', letter_heights), 9)

    # Apple and Orange
    house = (7, 11)
    apple_tree, orange_tree = (5, 15)
    apple_distances = (-2, 2, 1)
    orange_distances = (5, -6)
    # test_fn(find_fruit_on_house(house, apple_tree, apple_distances), 1)
    # test_fn(find_fruit_on_house(house, orange_tree, orange_distances), 1)

    # Kangaroos
    kangaroos = ([0, 2], [5, 3])
    # test_fn(check_if_kangaroos_meet(kangaroos), 'NO')
    kangaroos = ([0, 4], [4, 2])
    # test_fn(check_if_kangaroos_meet(kangaroos), 'YES')

    # Between Two Sets
    A, B = (2, 4), (16, 32, 96)
    test_fn(find_betweens(A, B), 3)
    A, B = (2, ), (20, 30, 12)
    test_fn(find_betweens(A, B), 1)
