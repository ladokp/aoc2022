# aoc_day_04.py

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        """Parse input"""
        expanded_section_list = []
        for line in puzzle_input.split("\n"):
            sections = []
            for section in line.split(","):
                section = section.split("-")
                sections.append(set(range(int(section[0]), int(section[1]) + 1)))
            expanded_section_list.append(sections)
        return self._find_overlaps(expanded_section_list)

    DAY = 4

    @staticmethod
    def _find_overlaps(sections):
        fully_overlaps = 0
        overlaps = 0
        for section in sections:
            if intersect := section[0].intersection(section[1]):
                overlaps += 1
                if intersect == section[0] or intersect == section[1]:
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
