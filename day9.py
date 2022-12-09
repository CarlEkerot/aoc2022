DIRS = {
    'U': (0, -1),
    'D': (0, 1),
    'L': (-1, 0),
    'R': (1, 0),
}


def parse():
    with open('day9.txt') as f:
        for line in f:
            a, b = line.strip().split()
            yield [a, int(b)]


def move_head(hpos, dir):
    hpos[0] += dir[0]
    hpos[1] += dir[1]


def move_tail(hpos, tpos):
    dx, dy = (hpos[0] - tpos[0], hpos[1] - tpos[1])
    if abs(dx) == 2 or abs(dy) == 2:
        tpos[0] += dx // abs(dx) if dx != 0 else dx
        tpos[1] += dy // abs(dy) if dy != 0 else dy


def solve(moves):
    poss = [[0, 0] for _ in range(10)]
    visited = [{(0, 0)} for _ in range(10)]
    for move_dir, num_moves in moves:
        dir = DIRS[move_dir]
        for _ in range(num_moves):
            move_head(poss[0], dir)
            for i in range(len(poss)):
                if i + 1 < len(poss):
                    move_tail(poss[i], poss[i + 1])
                visited[i].add(tuple(poss[i]))
    print(len(visited[1]))   # Part 1
    print(len(visited[-1]))  # Part 2


if __name__ == '__main__':
    moves = list(parse())
    solve(moves)
