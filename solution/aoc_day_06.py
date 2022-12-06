# aoc_day_06.py

from solution.aoc_base import AocBaseClass
from collections import Counter


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        """Parse input"""
        return puzzle_input.split("\n")[0]

    DAY = 6

    def _get_end_index_of_first_distinct_frame(self, frame_length):
        for index in range(0, len(self.data)):
            word_count = len(Counter(self.data[index : index + frame_length]).values())
            if word_count == frame_length:
                return index + frame_length

    def part1(self):
        """Solve part 1"""
        return self._get_end_index_of_first_distinct_frame(4)

    def part2(self):
        """Solve part 2"""
        return self._get_end_index_of_first_distinct_frame(14)


if __name__ == "__main__":
    AocSolution().print_solution()
