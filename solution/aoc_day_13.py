# aoc_day_13.py
import functools

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        """Parse input"""
        return [
            [eval(lines) for lines in paragraph.split("\n")]
            for paragraph in puzzle_input.split("\n\n")
        ]

    DAY = 13

    def compare(self, left, right):
        if isinstance(left, int):
            if isinstance(right, int):
                if left != right:
                    return -1 if left < right else 1
                return 0
            else:
                left = [left]
        elif isinstance(right, int):
            right = [right]

        for index in range(
            min(left_length := len(left), right_length := len(right))
        ):
            if (return_value := self.compare(left[index], right[index])) != 0:
                return return_value

        return (
            -1
            if left_length < right_length
            else 1
            if left_length > right_length
            else 0
        )

    def _check_packets(self):
        self.part1_solution = 0
        packets = []

        for index, lines in enumerate(self.data, 1):
            line_a, line_b = lines
            if self.compare(line_a, line_b) <= 0:
                self.part1_solution += index
            packets.append(line_a)
            packets.append(line_b)

        packets.extend(([[2]], [[6]]))
        packets.sort(key=functools.cmp_to_key(self.compare))
        self.part2_solution = (packets.index([[2]]) + 1) * (
            packets.index([[6]]) + 1
        )
        self.solved = True

    def part1(self):
        """Solve part 1"""
        if not self.solved:
            self._check_packets()
        return self.part1_solution

    def part2(self):
        """Solve part 2"""
        if not self.solved:
            self._check_packets()
        return self.part2_solution


if __name__ == "__main__":
    AocSolution().print_solution()
