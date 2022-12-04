# test_aoc_day_04.py

import pytest
import solution.aoc_day_04 as aoc


@pytest.fixture
def test_solution():
    return aoc.AocSolution(test_suffix="_test")


@pytest.fixture
def exercise_solution():
    return aoc.AocSolution()


def test_parse_test_solution(test_solution):
    """Test that input is parsed properly"""
    assert test_solution.data == [
        ({2, 3, 4}, {8, 6, 7}),
        ({2, 3}, {4, 5}),
        ({5, 6, 7}, {8, 9, 7}),
        ({2, 3, 4, 5, 6, 7, 8}, {3, 4, 5, 6, 7}),
        ({6}, {4, 5, 6}),
        ({2, 3, 4, 5, 6}, {4, 5, 6, 7, 8}),
    ]


def test_part1_test_solution(test_solution):
    """Test part 1 on example input"""
    assert test_solution.part1() == 2


def test_part2_test_solution(test_solution):
    """Test part 2 on example input"""
    assert test_solution.part2() == 4


def test_part1_exercise_solution(exercise_solution):
    """Test part 1 on exercise_solution input"""
    assert exercise_solution.part1() == 496


def test_part2_exercise_solution(exercise_solution):
    """Test part 2 on exercise_solution input"""
    assert exercise_solution.part2() == 847
