# test_aoc_day_15.py

import pytest

import solution.aoc_day_15 as aoc


@pytest.fixture
def test_solution():
    return aoc.AocSolution(test_suffix="_test")


@pytest.fixture
def exercise_solution():
    return aoc.AocSolution()


def test_parse_test_solution(test_solution):
    """Test if input is parsed properly"""
    assert test_solution.data == [
        (2, 18, -2, 15),
        (9, 16, 10, 16),
        (13, 2, 15, 3),
        (12, 14, 10, 16),
        (10, 20, 10, 16),
        (14, 17, 10, 16),
        (8, 7, 2, 10),
        (2, 0, 2, 10),
        (0, 11, 2, 10),
        (20, 14, 25, 17),
        (17, 20, 21, 22),
        (16, 7, 15, 3),
        (14, 3, 15, 3),
        (20, 1, 15, 3),
    ]


def test_part1_test_solution(test_solution):
    """Test part 1 on example input"""
    assert test_solution.part1(10) == 26


def test_part2_test_solution(test_solution):
    """Test part 2 on example input"""
    assert test_solution.part2(20) == 56000011


def test_part1_exercise_solution(exercise_solution):
    """Test part 1 on exercise_solution input"""
    assert exercise_solution.part1() == 5870800


def test_part2_exercise_solution(exercise_solution):
    """Test part 2 on exercise_solution input"""
    assert exercise_solution.part2() == 10908230916597
