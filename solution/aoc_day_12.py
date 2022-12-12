# aoc_day_12.py

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        """Parse input"""
        grid, start, end = {}, None, None
        for line_index, line in enumerate(puzzle_input.splitlines()):
            for column_index, column in enumerate(line):
                if column == "S":
                    start = (column_index, line_index)
                    grid[start] = 0
                elif column == "E":
                    end = (column_index, line_index)
                    grid[end] = 25
                else:
                    grid[column_index, line_index] = ord(column) - ord("a")
        return grid, start, end

    DAY = 12

    def solve_breadth_first(self, *, part2=False):
        grid, start, end = self.data
        visited = set()
        path = [(0, end)]
        while path:
            steps, p_0 = path.pop(0)
            if grid[p_0] == 0 and (part2 or p_0 == start):
                return steps
            for d_x, d_y in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                p_1 = p_0[0] + d_x, p_0[1] + d_y
                if (
                    p_1 not in visited
                    and p_1 in grid
                    and grid[p_1] >= grid[p_0] - 1
                ):
                    visited.add(p_1)
                    path.append((steps + 1, p_1))

    def part1(self):
        """Solve part 1"""
        return self.solve_breadth_first()

    def part2(self):
        """Solve part 2"""
        return self.solve_breadth_first(part2=True)


if __name__ == "__main__":
    AocSolution().print_solution()
