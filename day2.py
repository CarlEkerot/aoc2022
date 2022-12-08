RESULT = [
    [1, 0, 2],
    [2, 1, 0],
    [0, 2, 1]
]

IDX = {'A': 0, 'B': 1, 'C': 2, 'X': 0, 'Y': 1, 'Z': 2}

P2 = [
    [2, 0, 1],
    [0, 1, 2],
    [1, 2, 0]
]

WIN_SCORES = []


def parse():
    with open('day2.txt') as f:
        for line in f:
            yield tuple(map(lambda x: IDX[x], line.split()))


def part1(rounds):
    return sum(me + 1 + RESULT[me][elf] * 3 for elf, me in rounds)


def part2(rounds):
    return sum(P2[want][elf] + 1 + RESULT[P2[want][elf]][elf] * 3 for elf, want in rounds)


if __name__ == '__main__':
    rounds = list(parse())
    print(part1(rounds))
    print(part2(rounds))