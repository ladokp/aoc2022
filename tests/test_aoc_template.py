# test_aoc_template.py

import pytest

import solution.aoc_base as aoc


@pytest.fixture
def test_solution():
    return aoc.AocSolution(test_suffix="_test")


@pytest.mark.skip(reason="Not implemented")
def test_parse_test_solution(test_solution):
    """Test if input is parsed properly"""
    assert test_solution.data is ...


@pytest.mark.skip(reason="Not implemented")
def test_part1_test_solution(test_solution):
    """Test part 1 on example input"""
    assert test_solution.part1() is ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_test_solution(test_solution):
    """Test part 2 on example input"""
    assert test_solution.part2() is ...
