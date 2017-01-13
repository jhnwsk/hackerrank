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


def find_divisble_pairs(integers, k):
    """ Divisible Pairs. """
    result = 0
    for index, integer in enumerate(integers):
        for pair in integers[index + 1:]:
            if (integer + pair) % k == 0:
                result += 1

    return result


def find_sum_owed(n, k, b_charged, prices):
    """ Bon Appetit. """
    b_owed = sum(p for i, p in enumerate(prices) if i != k) // 2
    result = b_charged - b_owed
    if result == 0:
        result = 'Bon Appetit'
    return result


def find_matching_socks(socks):
    """ Sock Merchant. """
    matching = {s: socks.count(s) for s in set(socks)}
    result = 0
    for m in matching.values():
        result += m // 2
    return result


def grow_utopian_tree(cycles):
    """ Utopian Tree. """
    result = []
    for c in cycles:
        height = 1
        for cycle in range(c):
            if cycle % 2 == 0:
                height *= 2
            else:
                height += 1
        result.append(height)
    return result


def check_class_cancelled(students, threshold, arrivals):
    result = 'NO'
    present = sum(a <= 0 for a in arrivals)
    if threshold > present:
        result = 'YES'
    return result


def count_beautiful_between(i, j, k):
    """ Beautiful Days at the Movies.

    args:
        i, j -- day numbers between which to search
        k    -- beautiful divisor

    """

    result = 0
    candidates = range(i, j + 1)
    for candidate in candidates:
        reverse = int(str(candidate)[::-1])
        if (candidate - reverse) % k == 0:
            result += 1
    return result


def find_ad_reach(n):
    """ Viral Advertising.

    args:
        n -- the number of days the campaign lasts

    """
    people = 0
    sent = 5
    for day in range(n):
        sent = sent // 2
        people += sent
        sent = sent * 3

    return people


def save_prisoner(prisoners, sweets, starting_id):
    """ Save the Prisoner! """
    result = starting_id + sweets - 1
    result = result % prisoners
    if result == 0:
        result = prisoners
    return result


def find_energy_at_game_end(jump_distance, clouds):
    """ Jumping On The Clouds. """
    cloud = 0
    game_ended = False
    energy = 100
    cost, thundercloud_cost = 1, 2
    while not game_ended:
        cloud = (cloud + jump_distance) % len(clouds)
        energy -= cost
        if clouds[cloud]:
            energy -= thundercloud_cost
        if cloud == 0 or energy <= 0:
            game_ended = True

    return energy

if __name__ == '__main__':
    # Mini-Max Sum
    test_fn(mini_max_sum([1, 2, 3, 4, 5]), '10 14')

    # Designer PDF Viewer
    letter_heights = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5,
                      5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    test_fn(find_area('abc', letter_heights), 9)

    # Apple and Orange
    house = (7, 11)
    apple_tree, orange_tree = (5, 15)
    apple_distances = (-2, 2, 1)
    orange_distances = (5, -6)
    test_fn(find_fruit_on_house(house, apple_tree, apple_distances), 1)
    test_fn(find_fruit_on_house(house, orange_tree, orange_distances), 1)

    # Kangaroos
    kangaroos = ([0, 2], [5, 3])
    test_fn(check_if_kangaroos_meet(kangaroos), 'NO')
    kangaroos = ([0, 4], [4, 2])
    test_fn(check_if_kangaroos_meet(kangaroos), 'YES')

    # Between Two Sets
    A, B = (2, 4), (16, 32, 96)
    test_fn(find_betweens(A, B), 3)
    A, B = (2, ), (20, 30, 12)
    test_fn(find_betweens(A, B), 1)

    # Divisible Sum Pairs
    integers = [1, 3, 2, 6, 1, 2]
    k = 3
    test_fn(find_divisble_pairs(integers, k), 5)

    # Bon Apetit
    n, k, b_charged = 4, 1, 12
    prices = [3, 10, 2, 9]
    test_fn(find_sum_owed(n, k, b_charged, prices), 5)
    n, k, b_charged = 4, 1, 7
    prices = [3, 10, 2, 9]
    test_fn(find_sum_owed(n, k, b_charged, prices), 'Bon Appetit')

    # Sock merchant
    socks = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    test_fn(find_matching_socks(socks), 3)

    # Utopian Tree
    cycles = [0, 1, 4]
    test_fn(grow_utopian_tree(cycles), [1, 2, 7])
    cycles = [4, 3]
    test_fn(grow_utopian_tree(cycles), [7, 6])

    # Angry Professor
    students, threshold = 4, 3
    arrival_times = [-1, -3, 4, 2]
    test_fn(check_class_cancelled(students, threshold, arrival_times), 'YES')
    students, threshold = 4, 2
    arrival_times = [0, -1, 2, 1]
    test_fn(check_class_cancelled(students, threshold, arrival_times), 'NO')

    # Beautiful Days at the Movies
    i, j, k = 20, 23, 6
    test_fn(count_beautiful_between(i, j, k), 2)

    # Viral Advertising
    n = 1
    test_fn(find_ad_reach(n), 2)
    n = 2
    test_fn(find_ad_reach(n), 5)
    n = 3
    test_fn(find_ad_reach(n), 9)
    n = 4
    test_fn(find_ad_reach(n), 15)

    # Save the Prisoner!
    n, m, s = 3, 7, 2
    test_fn(save_prisoner(n, m, s), 2)
    n, m, s = 6, 6, 1
    test_fn(save_prisoner(n, m, s), 6)
    n, m, s = 1, 1, 1
    test_fn(save_prisoner(n, m, s), 1)
    n, m, s = 5, 2, 1
    test_fn(save_prisoner(n, m, s), 2)
    n, m, s = 4, 5, 1
    test_fn(save_prisoner(n, m, s), 1)
    n, m, s = 499999999, 999999997, 2
    test_fn(save_prisoner(n, m, s), 499999999)
    n, m, s = 999999999, 999999999, 1
    test_fn(save_prisoner(n, m, s), 999999999)

    # Jumping in the Clouds
    n, k = 8, 2
    clouds = [0, 0, 1, 0, 0, 1, 1, 0]
    test_fn(find_energy_at_game_end(k, clouds), 92)
