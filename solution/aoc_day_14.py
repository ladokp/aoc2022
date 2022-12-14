# aoc_day_14.py

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        """Parse input"""
        return puzzle_input.split("\n")

    DAY = 14

    def simulate_sand(self, part):
        blocked = set()

        for line in self.data:
            points = line.split(" -> ")
            for point_0, point_1 in zip(points, points[1:]):
                x_0, y_0 = list(map(int, point_0.split(",")))
                x_1, y_1 = list(map(int, point_1.split(",")))
                for x in range(min(x_0, x_1), max(x_0, x_1) + 1):
                    for y in range(min(y_0, y_1), max(y_0, y_1) + 1):
                        blocked.add((x, y))

        max_y = max(y for (x, y) in blocked)
        count = 0
        while True:
            x_0 = 500
            y_0 = 0
            while True:
                if (part == 1 and y_0 == max_y) or (500, 0) in blocked:
                    return count
                if part == 2 and y_0 == max_y + 1:
                    break
                if (x_0, y_0 + 1) not in blocked:
                    y_0 += 1
                elif (x_0 - 1, y_0 + 1) not in blocked:
                    x_0 -= 1
                    y_0 += 1
                elif (x_0 + 1, y_0 + 1) not in blocked:
                    x_0 += 1
                    y_0 += 1
                else:
                    break
            blocked.add((x_0, y_0))
            count += 1

    def part1(self):
        """Solve part 1"""
        return self.simulate_sand(1)

    def part2(self):
        """Solve part 2"""
        return self.simulate_sand(2)


if __name__ == "__main__":
    AocSolution().print_solution()
