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
        flowing_valves = []
        for line in puzzle_input.split("\n"):
            groups = re.match(
                "Valve (..) has flow rate=(.*); tunnels? leads? to valves?( .*,)* (..)",
                line,
            ).groups()
            valve = {
                "name": groups[0],
                "flow": int(groups[1]),
                "dest": [groups[3]],
            }
            if groups[2]:
                for destination in groups[2][:-1].strip().split(","):
                    valve["dest"].append(destination.strip())
            if valve["flow"] > 0:
                flowing_valves.append(groups[0])
            valves[valve["name"]] = valve
        return valves, flowing_valves

    DAY = 16

    def h(self, current, remaining, sum_, tkn):
        if remaining <= 1:
            return -1
        current_valve = self.data[0][current]
        if current_valve["flow"] > 0:
            remaining -= 1
            sum_ += remaining * current_valve["flow"]
        return_value = sum_
        for index in self.data[1]:
            if index in tkn:
                continue
            tkn.add(index)
            return_value = max(
                self.h(
                    index, remaining - self.dist[(current, index)], sum_, tkn
                ),
                return_value,
            )
            tkn.remove(index)
        return return_value

    def part1(self):
        """Solve part 1"""
        for valve_a in self.data[0].values():
            for valve_b in self.data[0].values():
                if valve_a == valve_b:
                    self.dist[(valve_a["name"], valve_b["name"])] = 0
                else:
                    self.dist[(valve_a["name"], valve_b["name"])] = 1e9
        for _ in range(len(self.data[0])):
            for valve_a in self.data[0].values():
                for valve_b in self.data[0].values():
                    for destination in valve_b["dest"]:
                        self.dist[(valve_a["name"], destination)] = min(
                            self.dist[(valve_a["name"], destination)],
                            self.dist[(valve_a["name"], valve_b["name"])] + 1,
                        )
        return self.h("AA", 30, 0, set())

    def part2(self):
        """Solve part 2"""


if __name__ == "__main__":
    AocSolution().print_solution()
