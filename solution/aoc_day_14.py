# aoc_day_14.py
from copy import deepcopy

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def __init__(self, /, test_suffix=""):
        super().__init__(test_suffix)
        self.grid = None

    def _parse(self, puzzle_input):
        """Parse input"""
        return [line for line in puzzle_input.strip().split("\n")]

    DAY = 14

    def _simulate_falling_sand(self, grid):
        mx, my = -1_000, -1_000
        while True:
            for line in self.data:
                pts = line.split(" -> ")
                _pts = []
                for pt in pts:
                    x, y = map(int, pt.split(","))
                    if x > mx:
                        mx = x
                    if y > my:
                        my = y
                    _pts.append((x, y))
                for i in range(len(_pts) - 1):
                    x1, y1 = _pts[i]
                    x2, y2 = _pts[i + 1]
                    if x1 == x2:
                        for y in range(min(y1, y2), max(y1, y2) + 1):
                            grid[(x1, y)] = "#"
                    else:
                        for x in range(min(x1, x2), max(x1, x2) + 1):
                            grid[(x, y1)] = "#"

            break
        return deepcopy(grid), mx, my

    def part1(self):
        """Solve part 1"""
        self.grid, mx, my = self._simulate_falling_sand({})

        sp = (500, 0)
        sc = 0
        steps = 0
        while True:
            x, y = sp
            if (y > my and x > mx) or (steps > 10_000_000):
                break
            steps += 1
            down_y = y + 1
            if (x, down_y) not in self.grid:
                sp = (x, down_y)
                continue
            else:
                if (x - 1, down_y) not in self.grid:
                    sp = (x - 1, down_y)
                    continue
                elif (x + 1, down_y) not in self.grid:
                    sp = (x + 1, down_y)
                    continue
                else:
                    self.grid[sp] = "o"
                    sc += 1
                    sp = (500, 0)
        return sc

    def part2(self):
        """Solve part 2"""
        self.grid, mx, my = self._simulate_falling_sand({})

        starting_point = (500, 0)
        sand_count = 0
        steps = 0
        y_lim = my + 2
        while True:
            x, y = starting_point
            steps += 1
            down_y = y + 1
            if (x, down_y) not in self.grid and down_y < y_lim:
                starting_point = (x, down_y)
                continue
            else:
                if (x - 1, down_y) not in self.grid and down_y < y_lim:
                    starting_point = (x - 1, down_y)
                    continue
                elif (x + 1, down_y) not in self.grid and down_y < y_lim:
                    starting_point = (x + 1, down_y)
                    continue
                else:
                    if starting_point == (500, 0):
                        break
                    self.grid[starting_point] = "o"
                    sand_count += 1
                    starting_point = (500, 0)
        return sand_count + 1


if __name__ == "__main__":
    AocSolution().print_solution()
