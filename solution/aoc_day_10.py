# aoc_day_10.py

from parse import compile

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        """Parse input"""
        return (
            [line.strip() for line in puzzle_input.split("\n")],
            [],
            [[" " for x in range(40)] for y in range(6)],
        )

    DAY = 10

    def _update_sprite(self, cycle, val):
        x, y = cycle % 40, cycle // 40
        if x in (val - 1, val, val + 1):
            self.data[2][y][x] = "#"

    def _check_cycle(self, x, val):
        if x in (20, 60, 100, 140, 180, 220):
            self.data[1].append(val * x)

    def _run_program(self):
        instructions, vals, sprite = self.data
        cycle, value = 0, 1

        for instruction in self.data[0]:
            if instruction == "noop":
                self._update_sprite(cycle, value)
                cycle += 1
                self._check_cycle(cycle, value)
            else:
                for _ in range(2):
                    self._update_sprite(cycle, value)
                    cycle += 1
                    self._check_cycle(cycle, value)
                value += int(instruction.split()[1])

        self.solved = True
        self.part1_solution, self.part2_solution = sum(vals), [
            "".join(pixel) for pixel in sprite
        ]

    def part1(self):
        """Solve part 1"""
        if not self.solved:
            self._run_program()
        return self.part1_solution

    def part2(self):
        """Solve part 2"""
        if not self.solved:
            self._run_program()
        return self.part2_solution


if __name__ == "__main__":
    AocSolution().print_solution()
