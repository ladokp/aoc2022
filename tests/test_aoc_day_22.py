# test_aoc_day_22.py

import pytest

import solution.aoc_day_22 as aoc


@pytest.fixture
def test_solution():
    return aoc.AocSolution(test_suffix="_test")


@pytest.fixture
def exercise_solution():
    return aoc.AocSolution()


def test_parse_test_solution(test_solution):
    """Test if input is parsed properly"""
    assert len(test_solution.data) == 3


def test_test_solution(test_solution):
    """Test part 1 on example input"""
    assert test_solution.part1() == 6032
    # assert test_solution.part2() == 5031


def test_exercise_solution(exercise_solution):
    """Test part 1 on exercise_solution input"""
    assert exercise_solution.part1() == 122082
    assert exercise_solution.part2() == 134076
