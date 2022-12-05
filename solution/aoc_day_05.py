# aoc_day_05.py
from collections import deque, defaultdict
from copy import copy, deepcopy

from parse import compile
from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        """Parse input"""
        starting_stacks, instructions = puzzle_input.split("\n\n")
        starting_stacks = starting_stacks.split("\n")
        starting_stacks.pop(-1)  # delete stack labels
        stacks = defaultdict(deque)
        for line in starting_stacks:
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

    def _move_crates(self, /, crate_mover_version=9000):
        stacks = deepcopy(self.data[0])
        for amount, origin, destination in self.data[1]:
            crates_to_move = [stacks[origin].pop() for _ in range(amount)]
            if crate_mover_version == 9001:
                crates_to_move = reversed(crates_to_move)
            stacks[destination].extend(crates_to_move)
        return "".join([stacks[i][-1] for i in sorted(stacks)])

    def part1(self):
        """Solve part 1"""
        return self._move_crates()

    def part2(self):
        """Solve part 2"""
        return self._move_crates(crate_mover_version=9001)


if __name__ == "__main__":
    AocSolution().print_solution()
