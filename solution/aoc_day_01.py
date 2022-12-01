# aoc_day_01.py

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        """Parse input"""
        parsed_data = list()
        elf_calories = 0
        for line in puzzle_input.split("\n"):
            if line:
                elf_calories += int(line)
            else:
                parsed_data.append(elf_calories)
                elf_calories = 0
        parsed_data.append(elf_calories)
        return list(sorted(parsed_data, reverse=True))

    DAY = 1

    def part1(self):
        """Solve part 1"""
        return self.data[0]

    def part2(self):
        """Solve part 2"""
        return sum(self.data[:3])


if __name__ == "__main__":
    AocSolution().print_solution()
