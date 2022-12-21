# aoc_day_20.py

from solution.aoc_base import AocBaseClass


class Unknown:
    def __init__(self):
        self.op_list = []

    def solve(self, other_value):
        current_value = other_value
        while len(self.op_list) > 0:
            op, other, self_is_left = self.op_list.pop()
            if op == "-":
                current_value = current_value - other
            elif op == "//":
                current_value = current_value // other
            elif op == "+":
                if self_is_left:
                    current_value = current_value + other
                else:
                    current_value = other - current_value
            elif op == "*":
                if self_is_left:
                    current_value = current_value * other
                else:
                    current_value = other // current_value

        return current_value

    def add(self, other, self_is_left):
        self.op_list.append(("-", other, True))
        return self

    def sub(self, other, self_is_left):
        self.op_list.append(("+", other, self_is_left))
        return self

    def mul(self, other, self_is_left):
        self.op_list.append(("//", other, True))
        return self

    def div(self, other, self_is_left):
        self.op_list.append(("*", other, self_is_left))
        return self


class Monkey:
    def __init__(self, input):
        self.name, other = input.split(":")
        other = other[1:]
        self.value = None
        try:
            self.value = int(other)
        except ValueError:
            self.name1, self.op, self.name2 = other.split(" ")
            if self.op == "/":
                self.op = "//"

    def get_value(self, monkeys):
        if self.value is None:
            value1 = monkeys[self.name1].get_value(monkeys)
            value2 = monkeys[self.name2].get_value(monkeys)
            self.value = eval(f"{value1}{self.op}{value2}")

        return self.value

    def get_value2(self, monkeys):
        if self.value is None:
            value1 = monkeys[self.name1].get_value2(monkeys)
            value2 = monkeys[self.name2].get_value2(monkeys)

            if self.name == "root":
                if type(value1) is Unknown:
                    return value1.solve(value2)
                else:
                    return value2.solve(value1)

            unknown = None
            if type(value1) is Unknown:
                assert type(value2) is not Unknown
                unknown = value1
                other = value2
                self_is_left = True
            elif type(value2) is Unknown:
                assert type(value1) is not Unknown
                unknown = value2
                other = value1
                self_is_left = False

            if unknown is not None:
                if self.op == "+":
                    unknown.add(other, self_is_left)
                elif self.op == "-":
                    unknown.sub(other, self_is_left)
                elif self.op == "*":
                    unknown.mul(other, self_is_left)
                elif self.op == "//":
                    unknown.div(other, self_is_left)
                else:
                    assert False

                self.value = unknown
            else:
                self.value = eval(f"{value1}{self.op}{value2}")

        return self.value


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        """Parse input"""
        entries = puzzle_input.split("\n")
        for i in range(len(entries)):
            if entries[i][-1] == "\n":
                entries[i] = entries[i][:-1]
        return entries

    DAY = 21

    def part1(self):
        """Solve part 1"""
        monkeys = {}
        for e in self.data:
            monkey = Monkey(e)
            monkeys[monkey.name] = monkey

        return monkeys["root"].get_value(monkeys)

    def part2(self):
        """Solve part 2"""
        monkeys = {}
        for e in self.data:
            monkey = Monkey(e)
            monkeys[monkey.name] = monkey

        monkeys["humn"].value = Unknown()

        return monkeys["root"].get_value2(monkeys)


if __name__ == "__main__":
    AocSolution().print_solution()
