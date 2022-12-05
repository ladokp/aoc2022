# aoc_day_05.py
from collections import deque, defaultdict
from copy import copy, deepcopy

from parse import compile
from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        """Parse input"""
        starting_stacks, instructions = puzzle_input.split("\n\n")
        starting_stacks_list = starting_stacks.split("\n")
        starting_stacks_list.pop(-1)  # delete stack labels
        stacks = defaultdict(deque)
        for line in starting_stacks_list:
            for position in range(1, len(line), 4):
                i = 1 + (position - 1) // 4
                if line[position].strip():
                    stacks[i].insert(0, line[position])
        instructions_list = []
        p = compile("move {:d} from {:d} to {:d}")
        for line in instructions.split("\n"):
            instructions_list.append(tuple(p.parse(line)))
        return stacks, instructions_list

    DAY = 5

    def part1(self):
        """Solve part 1"""
        stacks = deepcopy(self.data[0])
        for amount, origin, destination in self.data[1]:
            for _ in range(amount):
                stacks[destination].append(stacks[origin].pop())
        return "".join([stacks[i][-1] for i in sorted(stacks)])

    def part2(self):
        """Solve part 2"""
        stacks = deepcopy(self.data[0])
        for amount, origin, destination in self.data[1]:
            move_stack = reversed([stacks[origin].pop() for _ in range(amount)])
            stacks[destination].extend(move_stack)
        return "".join([stacks[i][-1] for i in sorted(stacks)])


if __name__ == "__main__":
    AocSolution().print_solution()
