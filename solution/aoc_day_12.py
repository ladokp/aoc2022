# aoc_day_12.py
import dijkstar

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        """Parse input"""
        s_x, s_y = -1, -1
        e_x, e_y = -1, -1
        board = []
        for row_index, row in enumerate(puzzle_input.split("\n")):
            vals = []
            for col_index, col in enumerate(row):
                match col:
                    case "S":
                        height = 0
                        s_x, s_y = row_index, col_index
                    case "E":
                        height = 25
                        e_x, e_y = row_index, col_index
                    case _:
                        height = ord(col) - ord("a")
                vals.append(height)
            board.append(vals)
        return board, (s_x, s_y), (e_x, e_y)

    DAY = 12

    def _find_shortest_path(self):
        graph = dijkstar.Graph()
        board, start, end = self.data
        for row_index, row in enumerate(board):
            for column_index, height in enumerate(row):
                if column_index > 0 and row[column_index - 1] <= height + 1:
                    graph.add_edge(
                        (row_index, column_index),
                        (row_index, column_index - 1),
                        1,
                    )
                if (
                    column_index < len(row) - 1
                    and row[column_index + 1] <= height + 1
                ):
                    graph.add_edge(
                        (row_index, column_index),
                        (row_index, column_index + 1),
                        1,
                    )
                if (
                    row_index > 0
                    and board[row_index - 1][column_index] <= height + 1
                ):
                    graph.add_edge(
                        (row_index, column_index),
                        (row_index - 1, column_index),
                        1,
                    )
                if (
                    row_index < len(board) - 1
                    and board[row_index + 1][column_index] <= height + 1
                ):
                    graph.add_edge(
                        (row_index, column_index),
                        (row_index + 1, column_index),
                        1,
                    )
        part1 = dijkstar.find_path(graph, start, end).total_cost
        best = 1_000_000
        for row_index, row in enumerate(board):
            for column_index, height in enumerate(row):
                if height == 0:
                    try:
                        cost = dijkstar.find_path(
                            graph, (row_index, column_index), end
                        ).total_cost
                    except dijkstar.algorithm.NoPathError:
                        continue
                    if cost < best:
                        best = cost
        self.solved = True
        self.solutions = part1, best

    def part1(self):
        """Solve part 1"""
        if not self.solved:
            self._find_shortest_path()
        return self.solutions[0]

    def part2(self):
        """Solve part 2"""
        if not self.solved:
            self._find_shortest_path()
        return self.solutions[1]


if __name__ == "__main__":
    AocSolution().print_solution()
