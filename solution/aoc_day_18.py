# aoc_day_18.py
from collections import deque

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        """Parse input"""
        lines = [x for x in puzzle_input.split("\n")]
        points = set()
        for line in lines:
            x, y, z = line.split(",")
            x, y, z = int(x), int(y), int(z)
            points.add((x, y, z))
        return points, set(), set()

    DAY = 18

    def reaches_outside(self, x, y, z, part):
        points, inside, outside = self.data
        if (x, y, z) in outside:
            return True
        if (x, y, z) in inside:
            return False
        seen, qubes = set(), deque([(x, y, z)])
        while qubes:
            x, y, z = qubes.popleft()
            if (x, y, z) in points:
                continue
            if (x, y, z) in seen:
                continue
            seen.add((x, y, z))
            if len(seen) > (5000 if part == 2 else 0):
                for p in seen:
                    outside.add(p)
                return True
            for _ in [-1, 1]:
                qubes.append((x + 1, y, z))
                qubes.append((x - 1, y, z))
                qubes.append((x, y + 1, z))
                qubes.append((x, y - 1, z))
                qubes.append((x, y, z + 1))
                qubes.append((x, y, z - 1))
        for p in seen:
            inside.add(p)
        return False

    def analyze_cubes(self, *, part=1):
        points, inside, outside, surface_area = *self.data, 0
        outside.clear()
        inside.clear()
        for (x, y, z) in points:
            if self.reaches_outside(x + 1, y, z, part):
                surface_area += 1
            if self.reaches_outside(x - 1, y, z, part):
                surface_area += 1
            if self.reaches_outside(x, y + 1, z, part):
                surface_area += 1
            if self.reaches_outside(x, y - 1, z, part):
                surface_area += 1
            if self.reaches_outside(x, y, z + 1, part):
                surface_area += 1
            if self.reaches_outside(x, y, z - 1, part):
                surface_area += 1
        return surface_area

    def part1(self):
        """Solve part 1"""
        return self.analyze_cubes()

    def part2(self):
        """Solve part 2"""
        return self.analyze_cubes(part=2)


if __name__ == "__main__":
    AocSolution().print_solution()
