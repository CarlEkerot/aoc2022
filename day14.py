def parse():
    with open('day14.txt') as f:
        paths = [line.strip().split(' -> ') for line in f]
        for path in paths:
            int_path = []
            for coord in path:
                x, y = coord.split(',')
                int_path.append((int(x), int(y)))
            yield int_path


def x_limits(paths):
    sorted_xs = sorted([c[0] for path in paths for c in path])
    return (sorted_xs[0], sorted_xs[-1])


def build_matrix(paths):
    size = 1000
    m = [['.' for _ in range(size)] for _ in range(size)]

    for path in paths:
        for (x1, y1), (x2, y2) in zip(path, path[1:]):
            dy = 1 if y1 <= y2 else -1
            dx = 1 if x1 <= x2 else -1
            for y in range(y1, y2 + dy, dy):
                for x in range(x1, x2 + dx, dx):
                    m[y][x] = '#'
    # Add floor
    highest_y = max([c[1] for path in paths for c in path])
    for i in range(len(m[0])):
        m[highest_y + 2][i] = '#'
    return m


def solve(m):
    start = (500, 0)
    dirs = [(0, 1), (-1, 1), (1, 1)]
    x_min, x_max = x_limits(paths)
    p1_count = None

    p = start
    count = 0
    while True:
        for dx, dy in dirs:
            nx, ny = p[0] + dx, p[1] + dy
            if not x_min <= nx < x_max and not p1_count:
                p1_count = count

            if m[ny][nx] not in ['#', 'o']:
                p = [nx, ny]
                break
        else:
            count += 1
            if p == start:
                print(p1_count, count)
                return

            m[p[1]][p[0]] = 'o'
            p = start


if __name__ == '__main__':
    paths = list(parse())
    solve(build_matrix(paths))
