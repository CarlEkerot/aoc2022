from itertools import zip_longest
from functools import cmp_to_key

DIV_A = [[2]]
DIV_B = [[6]]


def parse():
    with open('day13.txt') as f:
        pairs = f.read().split('\n\n')
        for pair in pairs:
            yield [eval(pkt) for pkt in pair.strip().split('\n')]


def sign(x):
    return 0 if abs(x) == 0 else x // abs(x)


def cmp(left, right):
    match (left, right):
        case (int(l), int(r)):
            return sign(l - r)
        case (list(l), list(r)):
            for a, b in zip_longest(l, r):
                if a is None:
                    return -1
                if b is None:
                    return 1
                res = cmp(a, b)
                if res != 0:
                    return res
        case (list(l), int(r)):
            return cmp(l, [r])
        case (int(l), list(r)):
            return cmp([l], r)
    return 0


def part1(pairs):
    indices = (i for i, (l, r) in enumerate(pairs, 1) if cmp(l, r) == -1)
    print(sum(indices))


def part2(pairs):
    packets = [e for p in pairs for e in p] + [DIV_A, DIV_B]
    res = sorted(packets, key=cmp_to_key(cmp))
    print((res.index(DIV_A) + 1) * (res.index(DIV_B) + 1))


if __name__ == '__main__':
    pairs = list(parse())
    part1(pairs)
    part2(pairs)
