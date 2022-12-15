from itertools import count

def parse():
    with open('day14.txt') as f:
        paths = [line.strip().split(' -> ') for line in f]
        for path in paths:
            int_path = []
            for coord in path:
                x, y = coord.split(',')
                int_path.append((int(x), int(y)))
            yield int_path


def calculate_bounds(paths):
    all_coords = [c for path in paths for c in path]
    x_min = min(all_coords, key=lambda c: c[0])[0]
    x_max = max(all_coords, key=lambda c: c[0])[0]
    y_min = 0
    y_max = max(all_coords, key=lambda c: c[1])[1]
    return (x_min, x_max, y_min, y_max)


def build_matrix(paths, bounds, start):
    x_min, x_max, y_min, y_max = bounds
    width = x_max - x_min  + 1
    height = y_max - y_min + 1
    m = [['.' for _ in range(width)] for _ in range(height)]

    for path in paths:
        for (x1, y1), (x2, y2) in zip(path, path[1:]):
            dy = 1 if y1 <= y2 else -1
            dx = 1 if x1 <= x2 else -1
            for y in range(y1, y2 + dy, dy):
                for x in range(x1, x2 + dx, dx):
                    m[y - y_min][x - x_min] = '#'


    #start_x, start_y = start[0] - x_min, start[1] - y_min
    #m[start[1] - y_min][start[0] - x_min] = '+'

    return m


def trickle_sand(matrix, start):
    x_min, x_max, y_min, y_max = bounds
    start_x, start_y = start[0] - x_min, start[1] - y_min
    dirs = [(0, 1), (-1, 1), (1, 1)]

    for i in count():
        p = [start_x, start_y]

        while True:
            for dx, dy in dirs:
                next_p = p[0] + dx, p[1] + dy
            


def draw(matrix):
    for row in matrix:
        print(''.join(row))


if __name__ == '__main__':
    paths = list(parse())
    bounds = calculate_bounds(paths)
    matrix = build_matrix(paths, bounds, (500, 0))
    draw(matrix)