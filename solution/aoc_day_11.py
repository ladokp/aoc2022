# aoc_day_11.py
from copy import deepcopy
from functools import reduce

from parse import compile

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        """Parse input"""
        items, monkey_operations, monkey_tests, modulo = [], [], [], 1
        p = compile(
            """Monkey {name:d}:
  Starting items: {items:item_list}
  Operation: new = {operation:operation_list}
  Test: divisible by {divider:d}
    If true: throw to monkey {true_monkey:d}
    If false: throw to monkey {false_monkey:d}""",
            {
                "item_list": lambda items_: items.append(
                    [int(number) for number in items_.split(",")]
                ),
                "operation_list": lambda operation: monkey_operations.append(
                    eval(f"lambda old: {operation}")
                ),
            },
        )
        for monkey in puzzle_input.split("\n\n"):
            parsed_monkey = p.parse(monkey)
            monkey_tests.append(
                eval(
                    f'lambda item: {parsed_monkey["true_monkey"]}'
                    f'if item % {parsed_monkey["divider"]} == 0'
                    f'else {parsed_monkey["false_monkey"]}'
                )
            )
            modulo *= parsed_monkey["divider"]

        return items, monkey_operations, monkey_tests, modulo

    DAY = 11

    def do_monkey_game(self, rounds, reducer):
        items = deepcopy(self.data[0])
        monkey_operations, monkey_tests, modulo = self.data[1:]
        monkey_count = len(monkey_tests)
        inspections = [0] * monkey_count

        for _ in range(rounds):
            for monkey in range(monkey_count):
                for item in items[monkey]:
                    inspections[monkey] += 1
                    new_item = (
                        monkey_operations[monkey](item) // reducer % modulo
                    )
                    items[monkey_tests[monkey](new_item)].append(new_item)
                items[monkey].clear()
        return reduce(
            lambda x, y: x * y, sorted(inspections)[monkey_count - 2 :]
        )

    def part1(self):
        """Solve part 1"""
        return self.do_monkey_game(20, 3)

    def part2(self):
        """Solve part 2"""
        return self.do_monkey_game(10_000, 1)


if __name__ == "__main__":
    AocSolution().print_solution()
