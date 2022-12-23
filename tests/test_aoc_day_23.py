# test_aoc_day_23.py

import pytest

import solution.aoc_day_23 as aoc


@pytest.fixture
def test_solution():
    return aoc.AocSolution(test_suffix="_test")


@pytest.fixture
def exercise_solution():
    return aoc.AocSolution()


def test_parse_test_solution(test_solution):
    """Test if input is parsed properly"""
    assert test_solution.data == [
        "....#..",
        "..###.#",
        "#...#.#",
        ".#...##",
        "#.###..",
        "##.#.##",
        ".#..#..",
    ]


def test_test_solution(test_solution):
    """Test part 1 on example input"""
    assert test_solution.part1() == 110
    assert test_solution.part2() == 20


def test_exercise_solution(exercise_solution):
    """Test part 1 on exercise_solution input"""
    assert exercise_solution.part1() == 3920
    assert exercise_solution.part2() == 889
