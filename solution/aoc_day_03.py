# aoc_day_03.py

from solution.aoc_base import AocBaseClass
from string import ascii_letters


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        """Parse input"""
        rucksack_items = puzzle_input.split("\n")
        rucksacks_part_1 = [
            "".join(set(line[: len(line) // 2]).intersection(line[len(line) // 2 :]))
            for line in rucksack_items
        ]
        rucksacks_part_2 = [
            "".join(
                set(rucksack_items[current_position])
                .intersection(rucksack_items[current_position + 1])
                .intersection(rucksack_items[current_position + 2])
            )
            for current_position in range(0, len(rucksack_items), 3)
        ]
        return rucksacks_part_1, rucksacks_part_2

    DAY = 3

    @staticmethod
    def _get_priorities(common_items):
        return sum(ascii_letters.index(item) + 1 for item in common_items)

    def part1(self):
        """Solve part 1"""
        return self._get_priorities(self.data[0])

    def part2(self):
        """Solve part 2"""
        return self._get_priorities(self.data[1])


if __name__ == "__main__":
    AocSolution().print_solution()
