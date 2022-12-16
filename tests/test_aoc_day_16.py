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
    assert test_solution.data == (
        {
            "AA": {"dest": ["BB", "DD", "II"], "flow": 0, "name": "AA"},
            "BB": {"dest": ["AA", "CC"], "flow": 13, "name": "BB"},
            "CC": {"dest": ["BB", "DD"], "flow": 2, "name": "CC"},
            "DD": {"dest": ["EE", "CC", "AA"], "flow": 20, "name": "DD"},
            "EE": {"dest": ["DD", "FF"], "flow": 3, "name": "EE"},
            "FF": {"dest": ["GG", "EE"], "flow": 0, "name": "FF"},
            "GG": {"dest": ["HH", "FF"], "flow": 0, "name": "GG"},
            "HH": {"dest": ["GG"], "flow": 22, "name": "HH"},
            "II": {"dest": ["JJ", "AA"], "flow": 0, "name": "II"},
            "JJ": {"dest": ["II"], "flow": 21, "name": "JJ"},
        },
        ["BB", "CC", "DD", "EE", "HH", "JJ"],
    )


def test_part1_test_solution(test_solution):
    """Test part 1 on example input"""
    assert test_solution.part1() == 1651


def test_part2_test_solution(test_solution):
    """Test part 2 on example input"""
    assert test_solution.part2() == None


def test_part1_exercise_solution(exercise_solution):
    """Test part 1 on exercise_solution input"""
    assert exercise_solution.part1() == 2250


def test_part2_exercise_solution(exercise_solution):
    """Test part 2 on exercise_solution input"""
    assert exercise_solution.part2() == 3015
