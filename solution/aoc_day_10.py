# aoc_day_10.py
from advent_of_code_ocr import convert_array_6

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

    def _run_program(self):
        instructions, signal_strengths, sprite = self.data
        cycle, value = 0, 1

        for instruction in instructions:
            command, steps = (
                split_instruction
                if len(split_instruction := instruction.split()) == 2
                else (split_instruction[0], 0)
            )
            cycles = {"noop": 1, "addx": 2}.get(command, 0)
            for _ in range(cycles):
                if (x := cycle % 40) in (value - 1, value, value + 1):
                    sprite[cycle // 40][x] = "#"
                cycle += 1
                if cycle in (20, 60, 100, 140, 180, 220):
                    signal_strengths.append(value * cycle)
            if command == "addx":
                value += int(steps)

        self.solved = True
        sprite_ = ["".join(pixel) for pixel in sprite]
        try:
            sprite_ = convert_array_6(sprite_, empty_pixel=" ")
        except KeyError:
            pass
        self.part1_solution, self.part2_solution = sum(signal_strengths), sprite_

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
