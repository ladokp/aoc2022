# test_aoc_day_20.py

import pytest

import solution.aoc_day_20 as aoc


@pytest.fixture
def test_solution():
    return aoc.AocSolution(test_suffix="_test")


@pytest.fixture
def exercise_solution():
    return aoc.AocSolution()


def test_parse_test_solution(test_solution):
    """Test if input is parsed properly"""
    assert test_solution.data == [
        (0, 1),
        (1, 2),
        (2, -3),
        (3, 3),
        (4, -2),
        (5, 0),
        (6, 4),
    ]


def test_test_solution(test_solution):
    """Test part 1 on example input"""
    assert test_solution.part1() == 3
    assert test_solution.part2() == 1623178306


def test_exercise_solution(exercise_solution):
    """Test part 1 on exercise_solution input"""
    assert exercise_solution.part1() == 3700
    assert exercise_solution.part2() == 10626948369382
