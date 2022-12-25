# test_aoc_day_25.py

import pytest

import solution.aoc_day_25 as aoc


@pytest.fixture
def test_solution():
    return aoc.AocSolution(test_suffix="_test")


@pytest.fixture
def exercise_solution():
    return aoc.AocSolution()


def test_parse_test_solution(test_solution):
    """Test if input is parsed properly"""
    assert test_solution.data == 4890


def test_test_solution(test_solution):
    """Test part 1 on example input"""
    assert test_solution.part1() == "2=-1=0"
    assert test_solution.part2() is None


def test_exercise_solution(exercise_solution):
    """Test part 1 on exercise_solution input"""
    assert exercise_solution.part1() == "2=0=02-0----2-=02-10"
    assert exercise_solution.part2() is None
