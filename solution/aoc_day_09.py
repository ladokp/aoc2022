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

    def part1(self):
        """Solve part 1"""
        head_x, head_y, tail_x, tail_y, seen = 0, 0, 0, 0, {(0, 0)}
        for direction, steps in self.data:
            move_x, move_y = self.OFFSET[direction]
            for _ in range(steps):
                head_x += move_x
                head_y += move_y
                for visited_position in self._get_positions(
                    head_x, head_y, tail_x, tail_y
                ):
                    tail_x, tail_y = visited_position
                    seen.add(visited_position)
        return len(seen)

    def part2(self):
        """Solve part 2"""
        rope, seen = [(0, 0)] * 10, set()
        for direction, steps in self.data:
            move_x, move_y = self.OFFSET[direction]
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


if __name__ == "__main__":
    AocSolution().print_solution()
