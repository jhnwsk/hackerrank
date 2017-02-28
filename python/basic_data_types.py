#!/bin/python3
""" HackerRank 'Python > Basic Data Types' challenges.

    https://www.hackerrank.com/domains/python/py-basic-data-types
"""
from testing import test_fn
from copy import copy
from statistics import mean


def execute_commands(commands):
    """ Lists. """
    result = []
    the_list = []
    for command in commands:
        action = command.split()
        if action[0] == 'insert':
            the_list.insert(int(action[1]), int(action[2]))
        elif action[0] == 'remove':
            the_list.remove(int(action[1]))
        elif action[0] == 'append':
            the_list.append(int(action[1]))
        elif action[0] == 'sort':
            the_list.sort()
        elif action[0] == 'reverse':
            the_list.reverse()
        elif action[0] == 'pop':
            the_list.pop()
        elif action[0] == 'print':
            result.append(copy(the_list))

    return result


def calculate_tuple_hash(numbers):
    """ Tuples. """
    integer_list = map(int, numbers.split())
    result = tuple(integer_list)
    return hash(result)


def find_possible_coordinates(X, Y, Z, N):
    """ List comprehensions. """
    cuboid = []
    for x in range(X + 1):
        for y in range(Y + 1):
            for z in range(Z + 1):
                cuboid.append([x, y, z])

    incorrect = [i for i in cuboid if sum(i) != N]
    return incorrect

def find_second_largest_number(numbers):
    """ Find the second largest number. """
    numbers = set(int(x) for x in numbers.split())
    numbers = sorted(list(numbers))
    return numbers[-2]

def find_students_with_second_lowest_grade(students):
    """ Nested Lists. """
    grades = [s[1] for s in students]

    grades = sorted(set(grades))
    grade = grades[1]
    students = sorted(students, key=lambda x: x[1])
    students = [s[0] for s in students if s[1] == grade]

    return sorted(students)

def catalogue_students(students, student):
    """ Finding the precentage. """
    student_catalogue = {}

    for s in students:
        s = s.split(' ')
        student_catalogue[s[0]] = mean(float(mark) for mark in s[1:])
    return '{0:.2f}'.format(student_catalogue[student])

if __name__ == '__main__':
    # LISTS
    commands = (
        "insert 0 5",
        "insert 1 10",
        "insert 0 6",
        "print",
        "remove 6",
        "append 9",
        "append 1",
        "sort",
        "print",
        "pop",
        "reverse",
        "print")
    lists = [[6, 5, 10], [1, 5, 9, 10], [9, 5, 1]]
    test_fn(execute_commands(commands), lists)

    # TUPLES
    numbers = '1 2'
    test_fn(calculate_tuple_hash(numbers), 3713081631934410656)

    # LIST COMPREHENSIONS
    X, Y, Z, N = 1, 1, 1, 2
    test_fn(find_possible_coordinates(X, Y, Z, N), [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]])

    # SECOND LARGEST NUMBER
    numbers = "2 3 6 6 5"
    test_fn(find_second_largest_number(numbers), 5)

    # Nested Lists
    students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
    test_fn(find_students_with_second_lowest_grade(students), ['Berry', 'Harry'])

    # Finding the Percentage
    student_catalogue = ('Krishna 67 68 69', 'Arjun 70 98 63', 'Malika 52 56 60')
    student = 'Malika'
    test_fn(catalogue_students(student_catalogue, student), '56.00')
