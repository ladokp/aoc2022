# aoc_day_11.py
from copy import deepcopy
from functools import reduce

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        """Parse input"""
        items = [
            [63, 57],
            [82, 66, 87, 78, 77, 92, 83],
            [97, 53, 53, 85, 58, 54],
            [50],
            [64, 69, 52, 65, 73],
            [57, 91, 65],
            [67, 91, 84, 78, 60, 69, 99, 83],
            [58, 78, 69, 65],
        ]

        monkey_operations = [
            lambda x: x * 11,
            lambda x: x + 1,
            lambda x: x * 7,
            lambda x: x + 3,
            lambda x: x + 6,
            lambda x: x + 5,
            lambda x: x * x,
            lambda x: x + 7,
        ]

        monkey_tests = [
            lambda x: 6 if x % 7 == 0 else 2,
            lambda x: 5 if x % 11 == 0 else 0,
            lambda x: 4 if x % 13 == 0 else 3,
            lambda x: 1 if x % 3 == 0 else 7,
            lambda x: 3 if x % 17 == 0 else 7,
            lambda x: 0 if x % 2 == 0 else 6,
            lambda x: 2 if x % 5 == 0 else 4,
            lambda x: 5 if x % 19 == 0 else 1,
        ]

        return items, monkey_operations, monkey_tests

    DAY = 11

    def part1(self):
        """Solve part 1"""
        inspections = [0 for _ in range(8)]
        items = deepcopy(self.data[0])
        monkey_operations = deepcopy(self.data[1])
        monkey_tests = deepcopy(self.data[2])

        for r in range(20):
            for monkey in range(8):
                for idx, item in enumerate(items[monkey]):
                    inspections[monkey] += 1
                    new_item = monkey_operations[monkey](item)
                    new_item //= 3
                    items[monkey_tests[monkey](new_item)].append(new_item)

                items[monkey] = []
        return reduce(
            lambda x, y: x * y, sorted(inspections)[len(inspections) - 2 :]
        )

    def part2(self):
        """Solve part 2"""
        inspections = [0 for _ in range(8)]
        items = deepcopy(self.data[0])
        monkey_operations = deepcopy(self.data[1])
        monkey_tests = deepcopy(self.data[2])

        for r in range(10000):
            for monkey in range(8):
                for idx, item in enumerate(items[monkey]):
                    inspections[monkey] += 1
                    new_item = monkey_operations[monkey](item)
                    new_item %= 9699690
                    items[monkey_tests[monkey](new_item)].append(new_item)

                items[monkey] = []
        return reduce(
            lambda x, y: x * y, sorted(inspections)[len(inspections) - 2 :]
        )


if __name__ == "__main__":
    AocSolution().print_solution()
