# test_aoc_day_24.py

import pytest

import solution.aoc_day_24 as aoc


@pytest.fixture
def test_solution():
    return aoc.AocSolution(test_suffix="_test")


@pytest.fixture
def exercise_solution():
    return aoc.AocSolution()


def test_parse_test_solution(test_solution):
    """Test if input is parsed properly"""
    assert test_solution.data == (
        (
            {(2, 4), (1, 5), (1, 1), (0, 3), (1, 4), (3, 0), (0, 5)},
            {(0, 1), (0, 0), (2, 0), (2, 3), (2, 5), (3, 5)},
            {(3, 1), (3, 3), (0, 4), (3, 4)},
            {(3, 2), (2, 1)},
        ),
        4,
        6,
    )


def test_test_solution(test_solution):
    """Test part 1 on example input"""
    assert test_solution.part1() == 18
    assert test_solution.part2() == 54


def test_exercise_solution(exercise_solution):
    """Test part 1 on exercise_solution input"""
    assert exercise_solution.part1() == 228
    assert exercise_solution.part2() == 723
