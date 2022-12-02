# aoc_day_02.py

from solution.aoc_base import AocBaseClass
from types import MappingProxyType

scores_part1 = MappingProxyType(
    {
        ("B", "X"): 1,
        ("C", "Y"): 2,
        ("A", "Z"): 3,
        ("A", "X"): 4,
        ("B", "Y"): 5,
        ("C", "Z"): 6,
        ("C", "X"): 7,
        ("A", "Y"): 8,
        ("B", "Z"): 9,
    }
)

scores_part2 = MappingProxyType(
    {
        **scores_part1,
        ("C", "X"): 2,
        ("A", "X"): 3,
        ("A", "Y"): 4,
        ("C", "Y"): 6,
        ("C", "Z"): 7,
        ("A", "Z"): 8,
    }
)


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        """Parse input"""
        games = []
        for game in puzzle_input.split("\n"):
            games.append(tuple(game.split(" ")))
        return games

    DAY = 2

    def _get_total_score(self, scores=scores_part1):
        current_score = 0
        for game in self.data:
            current_score += scores.get(game)
        return current_score

    def part1(self):
        """Solve part 1"""
        return self._get_total_score()

    def part2(self):
        """Solve part 2"""
        return self._get_total_score(scores=scores_part2)


if __name__ == "__main__":
    AocSolution().print_solution()
