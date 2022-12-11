import copy
import math
import operator
import re
from dataclasses import dataclass

REGEX = r'''Monkey (\d+):
  Starting items: (.*)
  Operation: new = (.*) ([+*]) (.*)
  Test: divisible by (\d+)
    If true: throw to monkey (\d+)
    If false: throw to monkey (\d+)'''


@dataclass
class Monkey:
    id: int
    items: list[int]
    op: str
    op_left: str
    op_right: str
    test: int
    dst_true: int
    dst_false: int
    inspections: int = 0

    def exec(self, old):
        match (self.op_left, self.op_right):
            case ('old', 'old'): return self.op(old, old)
            case ('old', v): return self.op(old, int(v))
            case (v, 'old'): return self.op(int(v), old)
            case (v, w): return self.op(int(v), int(w))

    def dst(self, val):
        return self.dst_true if val % self.test == 0 else self.dst_false


def parse():
    with open('day11.txt') as f:
        text = f.read()
        matches = re.finditer(REGEX, text, re.MULTILINE)
        for m in matches:
            id = int(m.group(1))
            items = [int(i) for i in m.group(2).split(', ')]
            op_left = m.group(3)
            op = operator.mul if m.group(4) == '*' else operator.add
            op_right = m.group(5)
            test = int(m.group(6))
            dst_true = int(m.group(7))
            dst_false = int(m.group(8))

            yield Monkey(id, items, op, op_left, op_right, test, dst_true, dst_false)


def solve(monkeys, rounds, adjustment):
    monkeys_by_id = {m.id: m for m in monkeys}
    for _ in range(rounds):
        for monkey in monkeys:
            while monkey.items:
                monkey.inspections += 1
                old = monkey.items.pop(0)
                new = monkey.exec(old)
                adjusted = adjustment(new)
                monkeys_by_id[monkey.dst(adjusted)].items.append(adjusted)
    top_monkeys = sorted(monkeys, key=lambda m: m.inspections, reverse=True)
    print(top_monkeys[0].inspections * top_monkeys[1].inspections)


if __name__ == '__main__':
    monkeys = list(parse())
    all_tests = math.prod(m.test for m in monkeys)
    solve(copy.deepcopy(monkeys), 20, lambda x: x // 3)  # Part 1
    solve(copy.deepcopy(monkeys), 10000, lambda x: x % all_tests)  # Part 2
