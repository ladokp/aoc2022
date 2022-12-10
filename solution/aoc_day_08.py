# aoc_day_08.py
from copy import deepcopy

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        """Parse input"""
        tree_map = tuple(
            tuple(int(height) for height in line)
            for line in puzzle_input.split("\n")
        )
        tree_visibility_mask = []
        for line_index, line in enumerate(tree_map):
            tree_visibility_mask.append([])
            for tree_index, tree in enumerate(line):
                if line_index in (0, len(tree_map) - 1) or tree_index in (
                    0,
                    len(line) - 1,
                ):
                    tree_visibility_mask[line_index].append(1)
                else:
                    tree_visibility_mask[line_index].append(0)
        return self._score_trees(tree_map, tree_visibility_mask)

    DAY = 8

    @staticmethod
    def _is_left_smaller(tree_map, line_index, column_index):
        return (
            max(tree_map[line_index][0:column_index])
            < tree_map[line_index][column_index]
        )

    @staticmethod
    def _is_right_smaller(tree_map, line_index, column_index):
        return (
            max(tree_map[line_index][column_index + 1 : len(tree_map)])
            < tree_map[line_index][column_index]
        )

    @staticmethod
    def _is_upper_smaller(tree_map, line_index, column_index):
        upper_heights = [
            tree_map[index][column_index] for index in range(line_index)
        ]
        return max(upper_heights) < tree_map[line_index][column_index]

    @staticmethod
    def _is_lower_smaller(tree_map, line_index, column_index):
        lower_heights = [
            tree_map[index][column_index]
            for index in range(line_index + 1, len(tree_map))
        ]
        return max(lower_heights) < tree_map[line_index][column_index]

    @staticmethod
    def _get_left_score(tree_map, line_index, column_index):
        current_height = tree_map[line_index][column_index]
        score = 0
        if not column_index:
            return 0
        for height in reversed(tree_map[line_index][:column_index]):
            score += 1
            if height >= current_height:
                break
        return score

    @staticmethod
    def _get_right_score(tree_map, line_index, column_index):
        current_height = tree_map[line_index][column_index]
        score = 0
        if column_index == len(tree_map[line_index]):
            return 0
        for height in tree_map[line_index][column_index + 1 :]:
            score += 1
            if height >= current_height:
                break
        return score

    @staticmethod
    def _get_lower_score(tree_map, line_index, column_index):
        current_height = tree_map[line_index][column_index]
        score = 0
        if line_index == len(tree_map) - 1:
            return 0
        for height in tree_map[line_index + 1 :]:
            height = height[column_index]
            score += 1
            if height >= current_height:
                break
        return score

    @staticmethod
    def _get_upper_score(tree_map, line_index, column_index):
        current_height = tree_map[line_index][column_index]
        score = 0
        if not line_index:
            return 0
        for height in reversed(tree_map[:line_index]):
            height = height[column_index]
            score += 1
            if height >= current_height:
                break
        return score

    def _score_trees(self, tree_map, scoring_mask):
        tree_visibility_mask, tree_scores = deepcopy(scoring_mask), deepcopy(
            scoring_mask
        )
        seen_trees_counter = 0
        for line_index, line in enumerate(tree_map):
            for column_index, tree in enumerate(line):
                if tree_visibility_mask[line_index][column_index] == 1:
                    seen_trees_counter += 1
                elif (
                    self._is_left_smaller(tree_map, line_index, column_index)
                    or self._is_right_smaller(
                        tree_map, line_index, column_index
                    )
                    or self._is_upper_smaller(
                        tree_map, line_index, column_index
                    )
                    or self._is_lower_smaller(
                        tree_map, line_index, column_index
                    )
                ):
                    tree_visibility_mask[line_index][column_index] = 1
                    seen_trees_counter += 1
                tree_scores[line_index][column_index] = (
                    self._get_upper_score(tree_map, line_index, column_index)
                    * self._get_left_score(tree_map, line_index, column_index)
                    * self._get_lower_score(tree_map, line_index, column_index)
                    * self._get_right_score(tree_map, line_index, column_index)
                )
            tree_scores[line_index] = max(tree_scores[line_index])
        return seen_trees_counter, max(tree_scores)

    def part1(self):
        """Solve part 1"""
        return self.data[0]

    def part2(self):
        """Solve part 2"""
        return self.data[1]


if __name__ == "__main__":
    AocSolution().print_solution()
