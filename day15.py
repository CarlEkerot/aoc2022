import re

LIMIT = 4000000
REGEX = re.compile(
    'Sensor at x=([-]?\d+), y=([-]?\d+): '
    'closest beacon is at x=([-]?\d+), y=([-]?\d+)')


def parse():
    with open('day15.txt') as f:
        for line in f:
            (sx, sy, bx, by) = [int(d) for d in REGEX.match(line).groups()]
            yield (sx, sy), (bx, by)


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def bounds(sensors):
    x_min = 0
    x_max = 0
    for s, b in sensors:
        d = dist(s, b)
        if s[0] - d < x_min:
            x_min = s[0] - d
        if s[0] + d > x_max:
            x_max = s[0] + d
    return x_min, x_max


def on_line(sensors, y):
    x_min, x_max = bounds(sensors)
    for x in range(x_min, x_max + 1):
        yield (x, y)


def outer_edges(sensors):
    candidate_points = []
    for s, b in sensors:
        d = dist(s, b)
        r = d + 1

        corners = [
            (s[0], s[1] - r),  # U
            (s[0] + r, s[1]),  # R
            (s[0], s[1] + r),  # D
            (s[0] - r, s[1]),  # L
        ]
        delta = [(1, 1), (-1, 1), (-1, -1), (1, -1)]

        for c, d in zip(corners, delta):
            for i in range(r):
                p = (c[0] + d[0] * i, c[1] + d[1] * i)
                if 0 <= p[0] <= LIMIT and 0 <= p[1] <= LIMIT:
                    candidate_points.append(p)
    return candidate_points


def part1(sensors, candidates):
    count = 0
    for p in candidates:
        for s, b in sensors:
            if b != p and dist(p, s) <= dist(b, s):
                count += 1
                break
        else:
            if 0 <= p[0] <= LIMIT and 0 <= p[1] <= LIMIT:
                print(p[0] * LIMIT + p[1])
                return
    print(count)


if __name__ == '__main__':
    sensors = list(parse())
    part1(sensors, on_line(sensors, 2000000))
    part1(sensors, outer_edges(sensors))
