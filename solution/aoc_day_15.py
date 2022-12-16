# aoc_day_15.py

import z3

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        """Parse input"""
        sensors = []

        for line in puzzle_input.split("\n"):
            l, r = line.split(": ")
            ll, lr = l.split(", ")
            sx = int(ll.split(" ")[-1].split("=")[1])
            sy = int(lr.split("=")[1])
            rl, rr = r.split(", ")
            bx = int(rl.split(" ")[-1].split("=")[1])
            by = int(rr.split("=")[1])
            sensors.append((sx, sy, bx, by))
        return sensors

    DAY = 15

    @staticmethod
    def _abs(number):
        return z3.If(number >= 0, number, -number)

    def part1(self, target_y=2_000_000):
        """Solve part 1"""
        target_in_range, target_beacons = set(), set()
        for x, y, b_x, b_y in self.data:
            if y == target_y:
                target_in_range.add(x)
            if b_y == target_y:
                target_beacons.add(b_x)

            d = abs(x - b_x) + abs(y - b_y)
            d_x = d - abs(y - target_y)
            for x_2 in range(x - d_x, x + d_x + 1):
                target_in_range.add(x_2)

        return len(target_in_range.difference(target_beacons))

    def part2(self, border=4_000_000):
        """Solve part 2"""
        x_, y_ = z3.Int("X"), z3.Int("Y")

        o = z3.Optimize()
        o.add(x_ >= 0)
        o.add(y_ >= 0)
        o.add(x_ <= border)
        o.add(y_ <= border)

        for x, y, bx, by in self.data:
            d = abs(x - bx) + abs(y - by)
            o.add(self._abs(x_ - x) + self._abs(y_ - y) > d)

        o.check()
        return o.model().eval(x_ * 4_000_000 + y_)


if __name__ == "__main__":
    AocSolution().print_solution()
