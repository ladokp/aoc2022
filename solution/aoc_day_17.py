# aoc_day_17.py

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def __init__(self, /, test_suffix=""):
        super().__init__(test_suffix)
        self.shifts = 0

    def _parse(self, puzzle_input):
        """Parse input"""
        return puzzle_input, [
            ["####"],
            [" # ", "###", " # "],
            ["  #", "  #", "###"],
            ["#", "#", "#", "#"],
            ["##", "##"],
        ]

    DAY = 17

    def shift(self):
        v = self.data[0][self.shifts % len(self.data[0])]
        self.shifts += 1
        return v

    @staticmethod
    def touches_dropped(dropped, rock, rock_x, rock_y) -> bool:
        h = len(rock)
        for y, row in enumerate(rock):
            for x, c in enumerate(row):
                if c != " ":
                    px, py = rock_x + x, rock_y - h + y
                    if (px, py) in dropped:
                        return True
        return False

    @staticmethod
    def insert_dropped(rock, rock_x, rock_y):
        h, max_h, new = len(rock), 0, set()
        for y, row in enumerate(rock):
            for x, c in enumerate(row):
                if c != " ":
                    px, py = rock_x + x, rock_y - h + y
                    max_h = min(max_h, py)
                    new.add((px, py))
        return new, max_h

    def shift_rocks(self, i, height, dropped):
        rock = self.data[1][i % 5]
        r_width, rock_x, rock_y = len(rock[0]), 2, height - 3
        while True:
            if self.shift() == "<":
                if 0 < rock_x:
                    if not self.touches_dropped(
                        dropped, rock, rock_x - 1, rock_y
                    ):
                        rock_x -= 1
            else:
                if rock_x < 7 - r_width:
                    if not self.touches_dropped(
                        dropped, rock, rock_x + 1, rock_y
                    ):
                        rock_x += 1

            if self.touches_dropped(dropped, rock, rock_x, rock_y + 1):
                break
            rock_y += 1

        dropped_rock, m_height = self.insert_dropped(rock, rock_x, rock_y)
        dropped |= dropped_rock
        return min(height, m_height), dropped

    def part1(self):
        """Solve part 1"""
        dropped = set((x, 0) for x in range(7))
        height, index, rocks_count = 0, 0, 2022
        while index < rocks_count:
            height, dropped = self.shift_rocks(index, height, dropped)
            index += 1
        return -height

    def part2(self):
        """Solve part 2"""
        dropped = set((x, 0) for x in range(7))
        height, index, firsts, rocks_count = 0, 0, {}, 1_000_000_000_000
        while index < rocks_count:
            height, dropped = self.shift_rocks(index, height, dropped)
            line_id = tuple(
                (x, y)
                for x in range(7)
                for y in range(200)
                if (x, y + height) in dropped
            )
            looper = self.shifts % len(self.data[0]), line_id

            if looper not in firsts:
                firsts[looper] = index, height
            else:
                firsts_index, f_height = firsts[looper]
                height += (height - f_height) * (
                    (rocks_count - index) // (index - firsts_index)
                )
                index += (index - firsts_index) * (
                    (rocks_count - index) // (index - firsts_index)
                )
                d = {(x, y + height) for (x, y) in line_id}
                dropped |= d
            index += 1
        return -height


if __name__ == "__main__":
    AocSolution().print_solution()
