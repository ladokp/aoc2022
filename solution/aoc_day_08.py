# aoc_day_08.py
from copy import deepcopy

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        """Parse input"""
        puzzle_input = puzzle_input.split("\n")
        tree_map = [[int(height) for height in line] for line in puzzle_input]
        tree_visibility_mask = []
        for line_index, line in enumerate(tree_map):
            tree_visibility_mask.append([])
            for tree_index, tree in enumerate(line):
                if (
                    line_index == 0
                    or line_index == len(tree_map) - 1
                    or tree_index == 0
                    or tree_index == len(line) - 1
                ):
                    tree_visibility_mask[line_index].append(1)
                else:
                    tree_visibility_mask[line_index].append(0)
        return tree_map, tree_visibility_mask

    DAY = 8

    def _is_left_smaller(self, line_index, column_index):
        return (
            max(self.data[0][line_index][0:column_index])
            < self.data[0][line_index][column_index]
        )

    def _is_right_smaller(self, line_index, column_index):
        return (
            max(self.data[0][line_index][column_index + 1 : len(self.data[0])])
            < self.data[0][line_index][column_index]
        )

    def _is_upper_smaller(self, line_index, column_index):
        upper_heights = [
            self.data[0][index][column_index] for index in range(line_index)
        ]
        return max(upper_heights) < self.data[0][line_index][column_index]

    def _is_lower_smaller(self, line_index, column_index):
        lower_heights = [
            self.data[0][index][column_index]
            for index in range(line_index + 1, len(self.data[0]))
        ]
        return max(lower_heights) < self.data[0][line_index][column_index]

    def _get_left_score(self, line_index, column_index):
        current_height = self.data[0][line_index][column_index]
        score_counter = 0
        if column_index == 0:
            return 0
        for height in reversed(self.data[0][line_index][:column_index]):
            score_counter += 1
            if height >= current_height:
                break
        return score_counter

    def _get_right_score(self, line_index, column_index):
        current_height = self.data[0][line_index][column_index]
        score_counter = 0
        if column_index == len(self.data[0][line_index]):
            return 0
        for height in self.data[0][line_index][column_index + 1 :]:
            score_counter += 1
            if height >= current_height:
                break
        return score_counter

    def _get_lower_score(self, line_index, column_index):
        current_height = self.data[0][line_index][column_index]
        score_counter = 0
        if line_index == len(self.data[0]) - 1:
            return 0
        for height in self.data[0][line_index + 1 :]:
            height = height[column_index]
            score_counter += 1
            if height >= current_height:
                break
        return score_counter

    def _get_upper_score(self, line_index, column_index):
        current_height = self.data[0][line_index][column_index]
        score_counter = 0
        if line_index == 0:
            return 0
        for height in reversed(self.data[0][:line_index]):
            height = height[column_index]
            score_counter += 1
            if height >= current_height:
                break
        return score_counter

    def part1(self):
        """Solve part 1"""
        seen_tree_counter = 0
        tree_map, tree_visibility_mask = self.data[0], deepcopy(self.data[1])
        for line_index, line in enumerate(tree_map):
            for column_index, tree in enumerate(line):
                if tree_visibility_mask[line_index][column_index] == 1:
                    seen_tree_counter += 1
                elif (
                    self._is_left_smaller(line_index, column_index)
                    or self._is_right_smaller(line_index, column_index)
                    or self._is_upper_smaller(line_index, column_index)
                    or self._is_lower_smaller(line_index, column_index)
                ):
                    tree_visibility_mask[line_index][column_index] = 1
                    seen_tree_counter += 1
        return seen_tree_counter

    def part2(self):
        """Solve part 2"""
        tree_map, tree_visibility_mask = self.data[0], deepcopy(self.data[1])
        for line_index, line in enumerate(tree_map):
            for column_index, tree in enumerate(line):
                tree_visibility_mask[line_index][column_index] = (
                    self._get_upper_score(line_index, column_index)
                    * self._get_left_score(line_index, column_index)
                    * self._get_lower_score(line_index, column_index)
                    * self._get_right_score(line_index, column_index)
                )
            tree_visibility_mask[line_index] = max(tree_visibility_mask[line_index])
        return max(tree_visibility_mask)


if __name__ == "__main__":
    AocSolution().print_solution()
