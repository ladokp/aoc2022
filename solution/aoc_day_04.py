# aoc_day_04.py

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        """Parse input"""
        expanded_section_list = []
        for line in puzzle_input.split("\n"):
            sections = []
            for elf in line.split(","):
                lower_end, upper_end = tuple(map(int, elf.split("-")))
                sections.append(set(range(lower_end, upper_end + 1)))
            expanded_section_list.append(sections)
        return self._count_overlaps(expanded_section_list)

    DAY = 4

    @staticmethod
    def _count_overlaps(sections):
        fully_overlaps = overlaps = 0
        for section in sections:
            if intersect := set.intersection(*section):
                overlaps += 1
                if intersect in section:
                    fully_overlaps += 1
        return fully_overlaps, overlaps

    def part1(self):
        """Solve part 1"""
        return self.data[0]

    def part2(self):
        """Solve part 2"""
        return self.data[1]


if __name__ == "__main__":
    AocSolution().print_solution()
