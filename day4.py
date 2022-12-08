import re

def parse(filepath):
    with open(filepath) as f:
        for line in f:
            a1, a2, b1, b2 = map(int, re.compile('^(\d+)-(\d+),(\d+)-(\d+)\n').findall(line)[0])
            yield (list(range(a1, a2+1)), list(range(b1, b2+1)))

def part1(pairs):
    return sum(1 for p1, p2 in pairs if set(p1).issubset(set(p2)) or set(p2).issubset(set(p1)))

def part2(pairs):
    return sum(1 for p1, p2 in pairs if set(p1).intersection(set(p2)) != set() or set(p2).intersection(set(p1)) != set())

if __name__ == '__main__':
    pairs = list(parse('day4.txt'))
    print(part1(pairs))
    print(part2(pairs))
