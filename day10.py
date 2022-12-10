CHECKPOINTS = [20, 60, 100, 140, 180, 220]
CRT_WIDTH = 40
CRT_HEIGHT = 6


def parse():
    with open('day10.txt') as f:
        for line in f:
            match line.strip().split():
                case 'addx', val:
                    yield 0
                    yield int(val)
                case _:
                    yield 0


def solve(vals):
    x = 1
    sig_strengths = []
    crt = [['.' for _ in range(CRT_WIDTH)] for _ in range(CRT_HEIGHT)]

    for cycle, val in enumerate(vals, 1):
        crt_x = (cycle - 1) % CRT_WIDTH
        crt_y = (cycle - 1) // CRT_WIDTH
        if crt_x in [x - 1, x, x + 1]:
            crt[crt_y][crt_x] = '#'
        if cycle in CHECKPOINTS:
            sig_strengths.append(cycle * x)
        x += val

    print(sum(sig_strengths))  # Part 1
    [print(''.join(line)) for line in crt]  # Part 2


if __name__ == '__main__':
    vals = parse()
    solve(vals)
