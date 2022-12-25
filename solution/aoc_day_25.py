# aoc_day_25.py

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        """Parse input"""
        return sum(self.from_snafu(line) for line in puzzle_input.split("\n"))

    DAY = 25

    @staticmethod
    def from_snafu(snafu_number):
        decimal_number = 0
        for character in snafu_number:
            decimal_number *= 5
            if character == "0":
                decimal_number += 0
            elif character == "1":
                decimal_number += 1
            elif character == "2":
                decimal_number += 2
            elif character == "-":
                decimal_number -= 1
            elif character == "=":
                decimal_number -= 2
        return decimal_number

    @staticmethod
    def to_snafu(decimal_number):
        snafu_number = ""
        while decimal_number > 0:
            current_number = decimal_number % 5
            if current_number == 3:
                current_number = -2
                characters = "="
            elif current_number == 4:
                current_number = -1
                characters = "-"
            else:
                characters = str(current_number)
            snafu_number = characters + snafu_number
            decimal_number = (decimal_number - current_number) // 5
        return snafu_number

    def part1(self):
        """Solve part 1"""
        return self.to_snafu(self.data)

    def part2(self):
        """Solve part 2"""


if __name__ == "__main__":
    AocSolution().print_solution()
