# aoc_day_22.py

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        """Parse input"""
        lines = puzzle_input.split("\n")
        map_ = {}
        size = 0
        for i in range(len(lines[:-1]) - 1):
            for j in range(len(lines[:-1][i])):
                value = lines[:-1][i][j]
                if value != " ":
                    map_[i] = map_.get(i, {})
                    map_[i][j] = [1 if value == "." else 0][0]
                    size += 1
        return self.parse_intructions(lines[-1]), map_, size

    DAY = 22

    def parse_intructions(self, instructions):
        li = []
        while len(instructions) != 0:
            i = 1
            while instructions[:i].isnumeric() and i <= len(instructions):
                i += 1
            li.append((instructions[: i - 1], instructions[i - 1 : i]))
            instructions = instructions[i:]
        return [x for x in li if x != ""]

    def get_connected(self, x, y, direction):
        side_length = int((self.data[2] // 6) ** (1 / 2))
        positions = [(0, 1), (0, 2), (1, 1), (2, 0), (2, 1), (3, 0)]
        connections = {
            (0, 3): (5, 0),
            (0, 2): (3, 0),
            (1, 3): (5, 3),
            (1, 0): (4, 2),
            (1, 1): (2, 2),
            (2, 0): (1, 3),
            (2, 2): (3, 1),
            (3, 2): (0, 0),
            (3, 3): (2, 0),
            (4, 0): (1, 2),
            (4, 1): (5, 2),
            (5, 0): (4, 3),
            (5, 1): (1, 1),
            (5, 2): (0, 1),
        }
        start = positions.index((x // side_length, y // side_length))
        get_left_size = {
            0: lambda x, y: x % side_length,
            1: lambda x, y: (side_length - y - 1) % side_length,
            2: lambda x, y: (side_length - x - 1) % side_length,
            3: lambda x, y: y % side_length,
        }
        get_position = {
            0: lambda x, y, extra: (x + extra, y),
            1: lambda x, y, extra: (x, y + (side_length - extra - 1)),
            2: lambda x, y, extra: (
                x + (side_length - extra - 1),
                y + (side_length - 1),
            ),
            3: lambda x, y, extra: (x + (side_length - 1), y + extra),
        }
        return (
            get_position[connections[(start, direction)][1]](
                (positions[connections[(start, direction)][0]][0] * 50),
                (positions[connections[(start, direction)][0]][1] * 50),
                get_left_size[direction](x, y),
            ),
            connections[(start, direction)][1],
        )

    def solve_puzzle(self, part2=False):
        instructions, map_, size = self.data
        current = (0, min(map_[0]))
        facing = 0  # 0 right, 1 down, 2 left, 3 up
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for step in instructions:
            for i in range(int(step[0])):
                if facing % 2 == 0:
                    keys = [x for x in map_[current[0]]]
                    next_spot = (current[0], current[1] + moves[facing][1])
                    if part2:
                        if next_spot[1] > max(keys) or next_spot[1] < min(
                            keys
                        ):
                            resp = self.get_connected(*current, facing)
                            if map_[resp[0][0]][resp[0][1]]:
                                next_spot, facing = resp
                                current = next_spot
                            continue
                    else:
                        if next_spot[1] > max(keys):
                            next_spot = (
                                next_spot[0],
                                next_spot[1] - len(keys),
                            )
                        if next_spot[1] < min(keys):
                            next_spot = (
                                next_spot[0],
                                next_spot[1] + len(keys),
                            )
                    if list(map_[current[0]].values())[
                        next_spot[1] - min(keys)
                    ]:
                        current = next_spot
                else:
                    keys = [x for x in map_.keys() if current[1] in map_[x]]
                    next_spot = (current[0] + moves[facing][0], current[1])
                    if part2:
                        if next_spot[0] > max(keys) or next_spot[0] < min(
                            keys
                        ):
                            resp = self.get_connected(*current, facing)
                            if map_[resp[0][0]][resp[0][1]]:
                                next_spot, facing = resp
                                current = next_spot
                            continue
                    else:
                        if next_spot[0] > max(keys):
                            next_spot = (next_spot[0] - len(keys), current[1])
                        if next_spot[0] < min(keys):
                            next_spot = (next_spot[0] + len(keys), current[1])
                    if [
                        map_[x][current[1]]
                        for x in map_.keys()
                        if current[1] in map_[x]
                    ][next_spot[0] - min(keys)]:
                        current = next_spot
            if step[1] == "R":
                facing = (facing + 1) % 4
            elif step[1] == "L":
                facing = (facing - 1) % 4
        return 1000 * (current[0] + 1) + 4 * (current[1] + 1) + facing

    def part1(self):
        """Solve part 1"""
        return self.solve_puzzle()

    def part2(self):
        """Solve part 2"""
        return self.solve_puzzle(part2=True)


if __name__ == "__main__":
    AocSolution().print_solution()
