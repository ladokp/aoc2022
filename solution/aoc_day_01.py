# aoc_day_01.py

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        """Parse input"""
        elves_calories = [0]
        for line in puzzle_input.split("\n"):
            if line.strip():
                elves_calories[-1] += int(line)
            else:
                elves_calories.append(0)
        elves_calories.sort()
        return elves_calories[-1], sum(elves_calories[-3:])

    DAY = 1

    def part1(self):
        """Solve part 1"""
        return self.data[0]

    def part2(self):
        """Solve part 2"""
        return self.data[1]


if __name__ == "__main__":
    AocSolution().print_solution()
