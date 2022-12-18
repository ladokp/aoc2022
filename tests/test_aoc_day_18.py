# test_aoc_day_18.py

import pytest

import solution.aoc_day_18 as aoc


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
            (1, 2, 2),
            (1, 2, 5),
            (2, 1, 2),
            (2, 1, 5),
            (2, 2, 1),
            (2, 2, 2),
            (2, 2, 3),
            (2, 2, 4),
            (2, 2, 6),
            (2, 3, 2),
            (2, 3, 5),
            (3, 2, 2),
            (3, 2, 5),
        },
        set(),
        set(),
    )


def test_part1_test_solution(test_solution):
    """Test part 1 on example input"""
    assert test_solution.part1() == 64


def test_part2_test_solution(test_solution):
    """Test part 2 on example input"""
    assert test_solution.part2() == 58


def test_part1_exercise_solution(exercise_solution):
    """Test part 1 on exercise_solution input"""
    assert exercise_solution.part1() == 3374


def test_part2_exercise_solution(exercise_solution):
    """Test part 2 on exercise_solution input"""
    assert exercise_solution.part2() == 2010
