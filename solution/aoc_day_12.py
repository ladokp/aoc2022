# aoc_day_12.py
import dijkstar

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def __init__(self, /, test_suffix=""):
        super().__init__(test_suffix)
        self.graph = None

    def _parse(self, puzzle_input):
        """Parse input"""
        sx, sy = -1, -1
        ex, ey = -1, -1
        board = []
        for row, s in enumerate(puzzle_input.split("\n")):
            vals = []
            for col, c in enumerate(s):
                match c:
                    case "S":
                        height = 0
                        sx, sy = row, col
                    case "E":
                        height = 25
                        ex, ey = row, col
                    case _:
                        height = ord(c) - ord("a")
                vals.append(height)
            board.append(vals)
        return board, (sx, sy), (ex, ey)

    DAY = 12

    def part1(self):
        """Solve part 1"""
        self.graph = graph = dijkstar.Graph()
        board, start, end = self.data
        for r, row in enumerate(board):
            for c, height in enumerate(row):
                if c > 0 and board[r][c - 1] <= height + 1:
                    graph.add_edge((r, c), (r, c - 1), 1)
                if c < len(row) - 1 and board[r][c + 1] <= height + 1:
                    graph.add_edge((r, c), (r, c + 1), 1)
                if r > 0 and board[r - 1][c] <= height + 1:
                    graph.add_edge((r, c), (r - 1, c), 1)
                if r < len(board) - 1 and board[r + 1][c] <= height + 1:
                    graph.add_edge((r, c), (r + 1, c), 1)
        return dijkstar.find_path(graph, start, end).total_cost

    def part2(self):
        """Solve part 2"""
        best = 1_000_000
        if not self.graph:
            self.part1()
        board, start, end = self.data
        for r, row in enumerate(board):
            for c, height in enumerate(row):
                if height == 0:
                    try:
                        cost = dijkstar.find_path(
                            self.graph, (r, c), end
                        ).total_cost
                    except dijkstar.algorithm.NoPathError:
                        continue
                    if cost < best:
                        best = cost
        return best


if __name__ == "__main__":
    AocSolution().print_solution()
