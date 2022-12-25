# aoc_day_19.py
import re
from collections import deque

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def __init__(self, /, test_suffix=""):
        super().__init__(test_suffix)
        self.answer_1 = 0
        self.answer_2 = 1

    def _parse(self, puzzle_input):
        """Parse input"""
        return puzzle_input.split("\n")

    DAY = 19

    def get_quality_level(self, blue_prints, time):
        _, c1, c2, c3, c32, c4, c43 = blue_prints
        max_co = max([c1, c2, c3, c4])
        best, queue, skip = 0, deque([(0, 0, 0, 0, 1, 0, 0, 0, time)]), set()
        while queue:
            o1, o2, o3, o4, r1, r2, r3, r4, t = queue.popleft()
            best = max(best, o4)
            if t == 0:
                continue

            if o1 >= t * max_co - r1 * (t - 1):
                o1 = t * max_co - r1 * (t - 1)
            if o2 >= t * c32 - r2 * (t - 1):
                o2 = t * c32 - r2 * (t - 1)
            if o3 >= t * c43 - r3 * (t - 1):
                o3 = t * c43 - r3 * (t - 1)
            ns = (o1, o2, o3, o4, r1, r2, r3, r4, t)
            if ns in skip:
                continue
            skip.add(ns)

            o1, o2, o3, o4 = o1 + r1, o2 + r2, o3 + r3, o4 + r4
            queue.append((o1, o2, o3, o4, r1, r2, r3, r4, t - 1))
            if o1 >= c1 + r1 and r1 < max_co:
                queue.append((o1 - c1, o2, o3, o4, r1 + 1, r2, r3, r4, t - 1))
            if o1 >= c2 + r1 and r2 < c32:
                queue.append((o1 - c2, o2, o3, o4, r1, r2 + 1, r3, r4, t - 1))
            if o1 >= c3 + r1 and o2 >= c32 + r2 and r3 < c43:
                queue.append(
                    (o1 - c3, o2 - c32, o3, o4, r1, r2, r3 + 1, r4, t - 1)
                )
            if o1 >= c4 + r1 and o3 >= c43 + r3:
                queue.append(
                    (o1 - c4, o2, o3 - c43, o4, r1, r2, r3, r4 + 1, t - 1)
                )
        return best

    def solve_puzzle(self):
        for index, line in enumerate(self.data):
            blue_print = [int(x) for x in re.findall(r"\b\d+\b", line.strip())]
            self.answer_1 += blue_print[0] * self.get_quality_level(
                blue_print, 24
            )
            if index < 3:
                self.answer_2 *= self.get_quality_level(blue_print, 32)
        self.solved = True

    def part1(self):
        """Solve part 1"""
        if not self.solved:
            self.solve_puzzle()
        return self.answer_1

    def part2(self):
        """Solve part 2"""
        if not self.solved:
            self.solve_puzzle()
        return self.answer_2


if __name__ == "__main__":
    AocSolution().print_solution()
