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

    def compare_recursive(self, left, right):
        if isinstance(left, int):
            if isinstance(right, int):
                if left != right:
                    return -1 if left < right else 1
                return 0
            else:
                left = [left]
        elif isinstance(right, int):
            right = [right]

        for i in range(min(len(left), len(right))):
            if (rv := self.compare_recursive(left[i], right[i])) != 0:
                return rv

        return (
            -1
            if len(left) < len(right)
            else 1
            if len(left) > len(right)
            else 0
        )

    def _reorder_packets(self):
        self.part1_solution = 0
        all_packets = []

        for index, lines in enumerate(self.data, 1):
            line_a, line_b = lines
            if self.compare_recursive(line_a, line_b) <= 0:
                self.part1_solution += index
            all_packets.append(line_a)
            all_packets.append(line_b)

        all_packets.extend(([[2]], [[6]]))
        all_packets.sort(key=functools.cmp_to_key(self.compare_recursive))
        self.part2_solution = (all_packets.index([[2]]) + 1) * (
            all_packets.index([[6]]) + 1
        )
        self.solved = True

    def part1(self):
        """Solve part 1"""
        if not self.solved:
            self._reorder_packets()
        return self.part1_solution

    def part2(self):
        """Solve part 2"""
        if not self.solved:
            self._reorder_packets()
        return self.part2_solution


if __name__ == "__main__":
    AocSolution().print_solution()
