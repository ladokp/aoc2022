# aoc_day_20.py

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def __init__(self, /, test_suffix=""):
        super().__init__(test_suffix)
        self.answer_1 = 0
        self.answer_2 = 1

    def _parse(self, puzzle_input):
        """Parse input"""
        return [(i, int(x)) for i, x in enumerate(puzzle_input.split("\n"))]

    DAY = 20

    @staticmethod
    def solve_puzzle(old_ints, key=1, iterations=1):
        integers = [(i, key * x) for i, x in old_ints]
        length = len(integers)
        for _ in range(iterations):
            for i in range(length):
                for index in range(length):
                    if integers[index][0] == i:  # got the right index
                        _, val = integers[index]
                        integers.pop(index)
                        new_idx = (index + val) % (length - 1)
                        integers.insert(new_idx, (i, val))
                        break

        index_0 = [i for i, (_, x) in enumerate(integers) if x == 0][0]
        return sum(
            integers[(index_0 + G) % length][1] for G in (1000, 2000, 3000)
        )

    def part1(self):
        """Solve part 1"""
        if not self.solved:
            self.answer_1 = self.solve_puzzle(self.data)
        return self.answer_1

    def part2(self):
        """Solve part 2"""
        if not self.solved:
            self.answer_2 = self.solve_puzzle(
                self.data, key=811589153, iterations=10
            )
        return self.answer_2


if __name__ == "__main__":
    AocSolution().print_solution()
