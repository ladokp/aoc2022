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
        lol = []
        for line in puzzle_input.split("\n"):
            asd = re.match(
                "Valve (..) has flow rate=(.*); tunnels? leads? to valves?( .*,)* (..)",
                line,
            )
            g = asd.groups()
            valve = {}
            valve["name"] = g[0]
            valve["flow"] = int(g[1])
            valve["dest"] = [g[3]]
            if g[2] != None:
                for x in g[2][:-1].strip().split(","):
                    valve["dest"].append(x.strip())
            if valve["flow"] > 0:
                lol.append(g[0])
            valves[valve["name"]] = valve
        return valves, lol

    DAY = 16

    def h(self, current, remaining, sm, tkn):
        if remaining <= 1:
            return -1
        cv = self.data[0][current]
        if cv["flow"] > 0:
            remaining -= 1
            sm += remaining * cv["flow"]
        ret = sm
        for i in self.data[1]:
            if i in tkn:
                continue
            tkn.add(i)
            ret = max(
                self.h(i, remaining - self.dist[(current, i)], sm, tkn), ret
            )
            tkn.remove(i)
        return ret

    def part1(self):
        """Solve part 1"""
        for valve_a in self.data[0].values():
            for valve_b in self.data[0].values():
                if valve_a == valve_b:
                    self.dist[(valve_a["name"], valve_b["name"])] = 0
                else:
                    self.dist[(valve_a["name"], valve_b["name"])] = 1e9
        for i in range(len(self.data[0])):
            for valve_a in self.data[0].values():
                for valve_b in self.data[0].values():
                    for d in valve_b["dest"]:
                        self.dist[(valve_a["name"], d)] = min(
                            self.dist[(valve_a["name"], d)],
                            self.dist[(valve_a["name"], valve_b["name"])] + 1,
                        )
        return self.h("AA", 30, 0, set())

    def part2(self):
        """Solve part 2"""


if __name__ == "__main__":
    AocSolution().print_solution()
