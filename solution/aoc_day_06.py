# aoc_day_06.py

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        """Parse input"""
        return puzzle_input.split("\n")[0]

    DAY = 6

    def _inspect_first_distinct_frame(self, frame_length):
        current_frame = []
        for index, character in enumerate(self.data, start=1):
            if character in current_frame:
                current_frame = current_frame[current_frame.index(character) + 1 :]
            current_frame.append(character)
            if len(current_frame) == frame_length:
                return index

    def part1(self):
        """Solve part 1"""
        return self._inspect_first_distinct_frame(4)

    def part2(self):
        """Solve part 2"""
        return self._inspect_first_distinct_frame(14)


if __name__ == "__main__":
    AocSolution().print_solution()
