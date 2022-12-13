# test_aoc_day_13.py

import pytest

import solution.aoc_day_13 as aoc


@pytest.fixture
def test_solution():
    return aoc.AocSolution(test_suffix="_test")


@pytest.fixture
def exercise_solution():
    return aoc.AocSolution()


def test_parse_test_solution(test_solution):
    """Test if input is parsed properly"""
    assert test_solution.data == [
        [[1, 1, 3, 1, 1], [1, 1, 5, 1, 1]],
        [[[1], [2, 3, 4]], [[1], 4]],
        [[9], [[8, 7, 6]]],
        [[[4, 4], 4, 4], [[4, 4], 4, 4, 4]],
        [[7, 7, 7, 7], [7, 7, 7]],
        [[], [3]],
        [[[[]]], [[]]],
        [
            [1, [2, [3, [4, [5, 6, 7]]]], 8, 9],
            [1, [2, [3, [4, [5, 6, 0]]]], 8, 9],
        ],
    ]


def test_part1_test_solution(test_solution):
    """Test part 1 on example input"""
    assert test_solution.part1() == 13


def test_part2_test_solution(test_solution):
    """Test part 2 on example input"""
    assert test_solution.part2() == 140


def test_part1_exercise_solution(exercise_solution):
    """Test part 1 on exercise_solution input"""
    assert exercise_solution.part1() == 5252


def test_part2_exercise_solution(exercise_solution):
    """Test part 2 on exercise_solution input"""
    assert exercise_solution.part2() == 20592
