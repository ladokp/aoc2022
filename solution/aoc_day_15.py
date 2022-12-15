# aoc_day_15.py

from solution.aoc_base import AocBaseClass
import z3


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

    def part1(self, target_y=2_000_000):
        """Solve part 1"""
        target_in_range = set()
        target_beacons = set()
        for x, y, bx, by in self.data:
            if y == target_y:
                target_in_range.add(x)
            if by == target_y:
                target_beacons.add(bx)

            d = abs(x - bx) + abs(y - by)
            dx = d - abs(y - target_y)
            for x2 in range(x - dx, x + dx + 1):
                target_in_range.add(x2)

        return len(target_in_range.difference(target_beacons))

    def part2(self, border=4_000_000):
        """Solve part 2"""

        def abs_(X):
            return z3.If(X >= 0, X, -X)

        x_, y_ = z3.Int("X"), z3.Int("Y")

        o = z3.Optimize()
        o.add(x_ >= 0)
        o.add(y_ >= 0)
        o.add(x_ <= border)
        o.add(y_ <= border)

        for x, y, bx, by in self.data:
            d = abs(x - bx) + abs(y - by)
            o.add(abs_(x_ - x) + abs_(y_ - y) > d)

        o.check()
        return o.model().eval(x_ * 4_000_000 + y_)


if __name__ == "__main__":
    AocSolution().print_solution()
