# aoc_day_16.py
import re

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def __init__(self, /, test_suffix=""):
        super().__init__(test_suffix)
        self.dist = {}

    def _parse(self, puzzle_input):
        """Parse input"""
        valves = {}
        for line in puzzle_input.split("\n"):
            line = line.replace(",", "").split(" ")
            label, rate, destinations = (
                line[1],
                int(re.findall("-?[\d]+", line[4])[0]),
                line[9:],
            )
            destinations.append(label)
            valves[label] = (rate, destinations)
        return valves

    DAY = 16

    def part1(self):
        """Solve part 1"""
        current, next_, current_rate = {("AA", 0): ((), 0)}, {}, 0
        for _ in range(0, 30):
            for (position, rate), (opened, total) in current.items():
                total += rate
                for next_position in self.data[position][1]:
                    next_opened, next_rate = opened, rate
                    if position == next_position:
                        if position in opened:
                            continue
                        next_opened = set(opened)
                        next_opened.add(position)
                        next_opened = tuple(next_opened)
                        next_rate += self.data[position][0]

                    if (
                        next_position,
                        next_rate,
                    ) not in next_ or total > next_[
                        (next_position, next_rate)
                    ][
                        1
                    ]:
                        next_[(next_position, next_rate)] = (
                            next_opened,
                            total,
                        )
            current = next_
            next_ = {}
            current_rate = max(
                total for (position, rate), (opened, total) in current.items()
            )
        return current_rate

    def part2(self):
        """Solve part 2"""
        current, next_, current_rate = {(("AA", "AA"), 0): ((), 0)}, {}, 0
        for _ in range(0, 26):
            for (position, rate), (opened, total) in current.items():
                total += rate
                for next_pos_0 in self.data[position[0]][1]:
                    for next_pos_1 in self.data[position[1]][1]:
                        next_pos = (next_pos_0, next_pos_1)
                        next_opened, next_rate = opened, rate

                        if position[0] == next_pos[0]:
                            if position[0] in next_opened:
                                continue
                            next_opened = set(next_opened)
                            next_opened.add(position[0])
                            next_opened = tuple(next_opened)
                            next_rate += self.data[position[0]][0]

                        if position[1] == next_pos[1]:
                            if position[1] in next_opened:
                                continue
                            next_opened = set(next_opened)
                            next_opened.add(position[1])
                            next_opened = tuple(next_opened)
                            next_rate += self.data[position[1]][0]

                        if (next_pos, next_rate) not in next_ or total > next_[
                            (next_pos, next_rate)
                        ][1]:
                            next_[(next_pos, next_rate)] = (next_opened, total)
            current = next_
            next_ = {}
            current_rate = max(
                total for (position, rate), (opened, total) in current.items()
            )
        return current_rate


if __name__ == "__main__":
    AocSolution().print_solution()
