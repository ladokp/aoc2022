# test_aoc_day_19.py

import pytest

import solution.aoc_day_19 as aoc


@pytest.fixture
def test_solution():
    return aoc.AocSolution(test_suffix="_test")


@pytest.fixture
def exercise_solution():
    return aoc.AocSolution()


def test_parse_test_solution(test_solution):
    """Test if input is parsed properly"""
    assert test_solution.data == [
        "Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each "
        "obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 "
        "obsidian.",
        "Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each "
        "obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 "
        "obsidian.",
    ]


def test_test_solution(test_solution):
    """Test part 1 on example input"""
    assert test_solution.part1() == 33
    assert test_solution.part2() == 3472


def test_exercise_solution(exercise_solution):
    """Test part 1 on exercise_solution input"""
    assert exercise_solution.part1() == 1127
    assert exercise_solution.part2() == 21546
