# aoc_day_23.py
from copy import deepcopy

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        """Parse input"""
        return puzzle_input.split("\n")

    DAY = 23

    MOVES = [
        [(0, -1), (1, -1), (-1, -1)],  # N NE NW
        [(0, 1), (1, 1), (-1, 1)],  # S SE SW
        [(-1, 0), (-1, -1), (-1, 1)],  # W NW SW
        [(1, 0), (1, -1), (1, 1)],
    ]  # E NE SE

    @staticmethod
    def is_elf(elves, x, y):
        if x < 0 or y < 0:
            return False
        if x >= len(elves) or y >= len(elves[x]):
            return False
        return elves[x][y]

    def part1(self):
        """Solve part 1"""
        lines = self.data
        moves = deepcopy(self.MOVES)
        tiles = None

        small_elves = [
            [lines[y][x] == "#" for y in range(len(lines))]
            for x in range(len(lines[0]))
        ]
        elves = [
            [False for _ in range(20 + len(small_elves))]
            for _ in range(20 + len(small_elves[0]))
        ]

        for x in range(len(small_elves)):
            for y in range(len(small_elves[0])):
                elves[x + 10][y + 10] = small_elves[x][y]

        for _ in range(10):
            proposed = [[None for _ in line] for line in elves]
            for x, _ in enumerate(elves):
                for y, _ in enumerate(elves[0]):
                    if not elves[x][y]:
                        continue
                    if (
                        sum(
                            self.is_elf(elves, x + xd, y + yd)
                            for xd in range(-1, 2)
                            for yd in range(-1, 2)
                        )
                        == 1
                    ):
                        continue
                    for move in moves:
                        if not any(
                            self.is_elf(elves, x + m[0], y + m[1])
                            for m in move
                        ):
                            proposed[x][y] = (x + move[0][0], y + move[0][1])
                            break
            counts = {
                pos: sum(l.count(pos) for l in proposed)
                for line in proposed
                for pos in line
            }

            for x in range(len(elves)):
                for y in range(len(elves[x])):
                    if proposed[x][y] and counts[proposed[x][y]] == 1:
                        elves[x][y] = False
                        elves[proposed[x][y][0]][proposed[x][y][1]] = True

            moves = moves[1:] + moves[:1]

            max_x, min_x, max_y, min_y = -1000, 1000, -1000, 1000
            for x in range(len(elves)):
                for y in range(len(elves[0])):
                    if elves[x][y]:
                        max_x = max(x, max_x)
                        min_x = min(x, min_x)
                        max_y = max(y, max_y)
                        min_y = min(y, min_y)

            tiles = 0
            for x in range(min_x, max_x + 1):
                for y in range(min_y, max_y + 1):
                    if not elves[x][y]:
                        tiles += 1

        return tiles

    def part2(self):
        """Solve part 2"""
        lines = self.data
        offset = 100
        moves = deepcopy(self.MOVES)
        small_elves = [
            [lines[y][x] == "#" for y in range(len(lines))]
            for x in range(len(lines[0]))
        ]
        elves = [
            [False for _ in range(2 * offset + len(small_elves))]
            for _ in range(2 * offset + len(small_elves[0]))
        ]

        for x in range(len(small_elves)):
            for y in range(len(small_elves[0])):
                elves[x + offset][y + offset] = small_elves[x][y]

        round_ = 1
        while True:
            proposed = [[None for _ in line] for line in elves]
            counts = {}
            for x in range(len(elves)):
                for y in range(len(elves[0])):
                    if not elves[x][y]:
                        continue
                    if (
                        sum(
                            self.is_elf(elves, x + xd, y + yd)
                            for xd in range(-1, 2)
                            for yd in range(-1, 2)
                        )
                        == 1
                    ):
                        continue

                    for move in moves:
                        if not any(
                            self.is_elf(elves, x + m[0], y + m[1])
                            for m in move
                        ):
                            proposed[x][y] = (x + move[0][0], y + move[0][1])
                            counts[proposed[x][y]] = (
                                1
                                if proposed[x][y] not in counts
                                else counts[proposed[x][y]] + 1
                            )
                            break
            moved = 0
            for x, _ in enumerate(elves):
                for y, _ in enumerate(elves[x]):
                    if proposed[x][y] and counts[proposed[x][y]] == 1:
                        elves[x][y] = False
                        elves[proposed[x][y][0]][proposed[x][y][1]] = True
                        moved += 1

            moves = moves[1:] + moves[:1]

            if moved == 0:
                return round_
            round_ += 1


if __name__ == "__main__":
    AocSolution().print_solution()
