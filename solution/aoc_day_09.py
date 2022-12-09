# aoc_day_09.py

from parse import compile

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        """Parse input"""
        instructions = []
        p = compile("{} {:d}")
        for line in puzzle_input.split("\n"):
            instructions.append(tuple(p.parse(line)))
        return tuple(instructions)

    DAY = 9
    OFFSET = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}

    @staticmethod
    def _get_positions(head_x, head_y, tail_x, tail_y):
        while max(abs(tail_x - head_x), abs(tail_y - head_y)) > 1:
            if abs(tail_x - head_x) > 0:
                tail_x += 1 if head_x > tail_x else -1
            if abs(tail_y - head_y) > 0:
                tail_y += 1 if head_y > tail_y else -1
            yield tail_x, tail_y

    def _get_seen_points(self, /, knots_count, instructions=None, offset=None):
        if not offset:
            offset = self.OFFSET
        if not instructions:
            instructions = self.data
        rope, seen = [(0, 0)] * knots_count, set()
        for direction, steps in instructions:
            move_x, move_y = offset[direction]
            for _ in range(steps):
                head_x, head_y = rope[0]
                rope[0] = head_x + move_x, head_y + move_y
                for i in range(1, len(rope)):
                    previous_x, previous_y = rope[i - 1]
                    knot_x, knot_y = rope[i]
                    for visited_position in self._get_positions(
                        previous_x, previous_y, knot_x, knot_y
                    ):
                        rope[i] = visited_position
                seen.add(rope[-1])
        return len(seen)

    def part1(self):
        """Solve part 1"""
        return self._get_seen_points(knots_count=2)

    def part2(self):
        """Solve part 2"""
        return self._get_seen_points(knots_count=10)


if __name__ == "__main__":
    AocSolution().print_solution()
