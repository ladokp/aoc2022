# test_aoc_day_16.py

import pytest

import solution.aoc_day_16 as aoc


@pytest.fixture
def test_solution():
    return aoc.AocSolution(test_suffix="_test")


@pytest.fixture
def exercise_solution():
    return aoc.AocSolution()


def test_parse_test_solution(test_solution):
    """Test if input is parsed properly"""
    assert test_solution.data == {
        "AA": (0, ["DD", "II", "BB", "AA"]),
        "BB": (13, ["CC", "AA", "BB"]),
        "CC": (2, ["DD", "BB", "CC"]),
        "DD": (20, ["CC", "AA", "EE", "DD"]),
        "EE": (3, ["FF", "DD", "EE"]),
        "FF": (0, ["EE", "GG", "FF"]),
        "GG": (0, ["FF", "HH", "GG"]),
        "HH": (22, ["GG", "HH"]),
        "II": (0, ["AA", "JJ", "II"]),
        "JJ": (21, ["II", "JJ"]),
    }


def test_part1_test_solution(test_solution):
    """Test part 1 on example input"""
    assert test_solution.part1() == 1651


def test_part2_test_solution(test_solution):
    """Test part 2 on example input"""
    assert test_solution.part2() == 1707


def test_part1_exercise_solution(exercise_solution):
    """Test part 1 on exercise_solution input"""
    assert exercise_solution.part1() == 2250


def test_part2_exercise_solution(exercise_solution):
    """Test part 2 on exercise_solution input"""
    assert exercise_solution.part2() == 3015
