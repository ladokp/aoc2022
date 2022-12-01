# aoc_base.py

from abc import ABC, abstractmethod
from aocd import get_data
from aocd.exceptions import PuzzleLockedError
from pathlib import Path
from pprint import pprint


class AocBaseClass(ABC):
    def __init__(self, /, test_suffix=""):
        year, day = self.get_date()
        puzzle_file_path = Path(__file__).parent.parent / Path(
            f"resources/day_{day:02}{test_suffix}.txt"
        )

        match puzzle_file_path.is_file():
            case True:
                puzzle_input = Path(puzzle_file_path).read_text().strip()
            case False:
                try:
                    puzzle_file_path.write_text(
                        puzzle_input := get_data(day=day, year=year)
                    )
                except PuzzleLockedError:
                    puzzle_input = None
            case _:
                puzzle_input = None

        self.solved = False
        self.data = self._parse(puzzle_input)
        self.solutions = None

    DAY = -1
    YEAR = 2022

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
