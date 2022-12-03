# aoc_day_03.py

from solution.aoc_base import AocBaseClass
import string


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        """Parse input"""
        rucksack_items = puzzle_input.split("\n")
        alphabet = {
            v: k + 1
            for k, v in enumerate(f"{string.ascii_lowercase}{string.ascii_uppercase}")
        }
        rucksacks_part_1 = [
            "".join(set(line[: len(line) // 2]).intersection(line[len(line) // 2 :]))
            for line in rucksack_items
        ]
        rucksacks_part_2 = [
            "".join(
                set(rucksack_items[range_])
                .intersection(rucksack_items[range_ + 1])
                .intersection(rucksack_items[range_ + 2])
            )
            for range_ in range(0, len(rucksack_items), 3)
        ]
        return rucksacks_part_1, rucksacks_part_2, alphabet

    DAY = 3

    def _get_priorities(self, common_items):
        priority = 0
        for item in common_items:
            priority += self.data[2].get(item, 0)
        return priority

    def part1(self):
        """Solve part 1"""
        return self._get_priorities(self.data[0])

    def part2(self):
        """Solve part 2"""
        return self._get_priorities(self.data[1])


if __name__ == "__main__":
    AocSolution().print_solution()