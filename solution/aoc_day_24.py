# aoc_day_24.py
import math
from collections import deque

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        """Parse input"""
        blizzards = tuple(set() for _ in range(4))

        for r, line in enumerate(puzzle_input.splitlines()[1:]):
            for c, item in enumerate(line[1:]):
                if item in "<>^v":
                    blizzards["<>^v".find(item)].add((r, c))
        return blizzards, r, c

    DAY = 24

    def part1(self):
        """Solve part 1"""
        blizzards, r, c = self.data
        queue = deque([(0, -1, 0)])
        seen = set()
        target = (r, c - 1)
        lcm = r * c // math.gcd(r, c)

        while queue:
            time, cr, cc = queue.popleft()
            time += 1

            for dr, dc in ((0, 1), (0, -1), (-1, 0), (1, 0), (0, 0)):
                nr = cr + dr
                nc = cc + dc

                if (nr, nc) == target:
                    return time

                if (nr < 0 or nc < 0 or nr >= r or nc >= c) and not (
                    nr,
                    nc,
                ) == (
                    -1,
                    0,
                ):
                    continue

                for i, tr, tc in (
                    (0, 0, -1),
                    (1, 0, 1),
                    (2, -1, 0),
                    (3, 1, 0),
                ):
                    if (
                        (nr - tr * time) % r,
                        (nc - tc * time) % c,
                    ) in blizzards[i]:
                        break
                else:
                    key = (nr, nc, time % lcm)
                    if key in seen:
                        continue

                    seen.add(key)
                    queue.append((time, nr, nc))

    def part2(self):
        """Solve part 2"""
        blizzards, r, c = self.data
        queue = deque([(0, -1, 0, 0)])
        seen = set()
        targets = [(r, c - 1), (-1, 0)]
        lcm = r * c // math.gcd(r, c)

        while queue:
            time, cr, cc, stage = queue.popleft()
            time += 1

            for dr, dc in ((0, 1), (0, -1), (-1, 0), (1, 0), (0, 0)):
                nr = cr + dr
                nc = cc + dc

                n_stage = stage

                if (nr, nc) == targets[stage % 2]:
                    if stage == 2:
                        return time
                    n_stage += 1

                if (nr < 0 or nc < 0 or nr >= r or nc >= c) and (
                    nr,
                    nc,
                ) not in targets:
                    continue

                fail = False
                if (nr, nc) not in targets:
                    for i, tr, tc in (
                        (0, 0, -1),
                        (1, 0, 1),
                        (2, -1, 0),
                        (3, 1, 0),
                    ):
                        if (
                            (nr - tr * time) % r,
                            (nc - tc * time) % c,
                        ) in blizzards[i]:
                            fail = True
                            break

                if not fail:
                    key = (nr, nc, n_stage, time % lcm)
                    if key in seen:
                        continue

                    seen.add(key)
                    queue.append((time, nr, nc, n_stage))


if __name__ == "__main__":
    AocSolution().print_solution()
