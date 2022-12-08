from itertools import takewhile

def parse():
    with open('day8.txt') as f:
        return [[int(c) for c in line.strip()] for line in f]


def ranges(x, y, max_x, max_y):
    return [
        [trees[i][x] for i in range(y - 1, -1, -1)],
        [trees[i][x] for i in range(y + 1, max_y)],
        [trees[y][i] for i in range(x - 1, -1, -1)],
        [trees[y][i] for i in range(x + 1, max_x)],
    ]


def part1(trees):
    max_y = len(trees)
    max_x = len(trees[0])
    visible_count = max_x * 2 + max_y * 2 - 4
    for y in range(1, max_y - 1):
        for x in range(1, max_x - 1):
            rs = ranges(x, y, max_x, max_y)
            visibility = [all(h < trees[y][x] for h in r) for r in rs]
            if any(visibility):
                visible_count += 1
    print(visible_count)


def part2(trees):
    max_y = len(trees)
    max_x = len(trees[0])
    scores = []
    for y in range(0, max_y):
        for x in range(0, max_x):
            score = 1
            for r in ranges(x, y, max_x, max_y):
                shorter = takewhile(lambda h: h < trees[y][x], r)
                num_shorter = len(list(shorter))
                if (num_shorter != len(r)):
                    num_shorter +=1
                score *= num_shorter
            scores.append(score)
    print(max(scores))


if __name__ == '__main__':
    trees = parse()
    part1(trees)
    part2(trees)
