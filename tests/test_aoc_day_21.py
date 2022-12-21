# test_aoc_day_21.py

import pytest

import solution.aoc_day_21 as aoc


@pytest.fixture
def test_solution():
    return aoc.AocSolution(test_suffix="_test")


@pytest.fixture
def exercise_solution():
    return aoc.AocSolution()


def test_parse_test_solution(test_solution):
    """Test if input is parsed properly"""
    assert test_solution.data == [
        "root: pppw + sjmn",
        "dbpl: 5",
        "cczh: sllz + lgvd",
        "zczc: 2",
        "ptdq: humn - dvpt",
        "dvpt: 3",
        "lfqf: 4",
        "humn: 5",
        "ljgn: 2",
        "sjmn: drzm * dbpl",
        "sllz: 4",
        "pppw: cczh / lfqf",
        "lgvd: ljgn * ptdq",
        "drzm: hmdt - zczc",
        "hmdt: 32",
    ]


def test_test_solution(test_solution):
    """Test part 1 on example input"""
    assert test_solution.part1() == 152
    assert test_solution.part2() == 301


def test_exercise_solution(exercise_solution):
    """Test part 1 on exercise_solution input"""
    assert exercise_solution.part1() == 169525884255464
    assert exercise_solution.part2() == 3247317268284
