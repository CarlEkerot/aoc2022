from itertools import takewhile, product

def parse():
    with open('day8.txt') as f:
        return [[int(c) for c in line.strip()] for line in f]


def grid_coords(width, border=0):
    return product(range(border, width - border), range(border, width - border))


def ranges(x, y, width):
    return [
        [trees[i][x] for i in range(y - 1, -1, -1)],
        [trees[i][x] for i in range(y + 1, width)],
        [trees[y][i] for i in range(x - 1, -1, -1)],
        [trees[y][i] for i in range(x + 1, width)],
    ]


def part1(trees):
    width = len(trees)
    visible_count = 4 * width - 4
    for y, x in grid_coords(width, border=1):
        visibility = [all(h < trees[y][x] for h in r) for r in ranges(x, y, width)]
        visible_count += 1 if any(visibility) else 0
    print(visible_count)


def part2(trees):
    width = len(trees)
    scores = []
    for y, x in grid_coords(width):
        score = 1
        for r in ranges(x, y, width):
            num_shorter = sum(1 for _ in takewhile(lambda h: h < trees[y][x], r))
            if (num_shorter != len(r)):
                num_shorter += 1
            score *= num_shorter
        scores.append(score)
    print(max(scores))


if __name__ == '__main__':
    trees = parse()
    part1(trees)
    part2(trees)
