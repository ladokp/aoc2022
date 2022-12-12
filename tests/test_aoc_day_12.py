# test_aoc_day_12.py

import pytest

import solution.aoc_day_12 as aoc


@pytest.fixture
def test_solution():
    return aoc.AocSolution(test_suffix="_test")


@pytest.fixture
def exercise_solution():
    return aoc.AocSolution()


def test_parse_test_solution(test_solution):
    """Test if input is parsed properly"""
    assert test_solution.data == (
        {
            (0, 0): 0,
            (0, 1): 0,
            (0, 2): 0,
            (0, 3): 0,
            (0, 4): 0,
            (1, 0): 0,
            (1, 1): 1,
            (1, 2): 2,
            (1, 3): 2,
            (1, 4): 1,
            (2, 0): 1,
            (2, 1): 2,
            (2, 2): 2,
            (2, 3): 2,
            (2, 4): 3,
            (3, 0): 16,
            (3, 1): 17,
            (3, 2): 18,
            (3, 3): 19,
            (3, 4): 4,
            (4, 0): 15,
            (4, 1): 24,
            (4, 2): 25,
            (4, 3): 20,
            (4, 4): 5,
            (5, 0): 14,
            (5, 1): 23,
            (5, 2): 25,
            (5, 3): 21,
            (5, 4): 6,
            (6, 0): 13,
            (6, 1): 23,
            (6, 2): 23,
            (6, 3): 22,
            (6, 4): 7,
            (7, 0): 12,
            (7, 1): 11,
            (7, 2): 10,
            (7, 3): 9,
            (7, 4): 8,
        },
        (0, 0),
        (5, 2),
    )


def test_part1_test_solution(test_solution):
    """Test part 1 on example input"""
    assert test_solution.part1() == 31


def test_part2_test_solution(test_solution):
    """Test part 2 on example input"""
    assert test_solution.part2() == 29


def test_part1_exercise_solution(exercise_solution):
    """Test part 1 on exercise_solution input"""
    assert exercise_solution.part1() == 462


def test_part2_exercise_solution(exercise_solution):
    """Test part 2 on exercise_solution input"""
    assert exercise_solution.part2() == 451
