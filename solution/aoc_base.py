# aoc_base.py

import pathlib
import os
from abc import ABC, abstractmethod
from aocd import get_data
from pprint import pprint


class AocBaseClass(ABC):
    def __init__(self, /, test_suffix="", read_from_file=False):
        year, day = self.get_date()
        path = (
            f"{pathlib.Path(__file__).parent.parent}"
            f"/resources/day_"
            f"{day:02}"
            f"{test_suffix}.txt"
        )
        if not os.path.isfile(path=path):
            puzzle_input = get_data(day=day, year=year)
            with open(path, "w") as f:
                f.write(puzzle_input)
        else:
            puzzle_input = pathlib.Path(path).read_text().strip()
        self.solved = False
        self.data = self._parse(puzzle_input)
        self.solutions = None

    DAY = -1
    YEAR = 2021

    @classmethod
    def get_date(cls):
        """Return the corresponding day and year to reference the correct input file"""
        return cls.YEAR, cls.DAY

    @abstractmethod
    def _parse(self, puzzle_input):
        """Parse input"""
        pass

    @abstractmethod
    def part1(self):
        """Solve part 1"""
        pass

    @abstractmethod
    def part2(self):
        """Solve part 2"""
        pass

    def print_solution(self):
        if not self.solved:
            self.solve()
        part1, part2 = self.solutions
        pprint({"part1": part1, "part2": part2})

    def solve(self):
        """Solve the puzzle for the given input"""
        self.solutions = self.part1(), self.part2()
        self.solved = True


class AocSolution(AocBaseClass, ABC):
    pass
