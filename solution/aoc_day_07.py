# aoc_day_07.py

from collections import defaultdict

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        """Parse input"""
        return self._build_directory_tree(
            [line.strip() for line in puzzle_input.split("\n")]
        )

    DAY = 7

    @staticmethod
    def _build_directory_tree(history):
        total_sizes, current_position, folder_stack = defaultdict(lambda: 0), 1, [""]
        while True:
            current_row = history[current_position]
            if current_row.startswith("$"):
                match current_row.split()[1:]:
                    case ["cd", ".."]:
                        folder_stack.pop()
                        current_position += 1
                    case ["cd", folder]:
                        folder_stack.append(folder)
                        current_position += 1
                    case ["ls"]:
                        new_position = current_position + 1
                        while new_position < len(history):
                            command = history[new_position]
                            if command.startswith("$"):
                                break
                            elif not command.startswith("dir"):
                                size = int(command.split()[0])
                                for index in range(len(folder_stack)):
                                    total_sizes[
                                        "/".join(folder_stack[: index + 1])
                                    ] += size
                            new_position += 1
                        current_position = new_position
                if current_position >= len(history):
                    break
        return total_sizes

    def part1(self):
        """Solve part 1"""
        return sum(size for size in self.data.values() if size <= 100_000)

    def part2(self):
        """Solve part 2"""
        unused_space = 70_000_000 - self.data[""]
        return min(
            size for size in self.data.values() if unused_space + size >= 30_000_000
        )


if __name__ == "__main__":
    AocSolution().print_solution()
