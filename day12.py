def parse():
    with open('day12.txt') as f:
        return [[c for c in line.strip()] for line in f]


def pos(emap, c):
    for i in range(len(emap)):
        for j in range(len(emap[0])):
            if emap[i][j] == c:
                return (i, j)


def elevation(v, emap):
    match emap[v[0]][v[1]]:
        case 'S': return ord('a')
        case 'E': return ord('z')
        case c: return ord(c)


def in_bounds(v, emap):
    return 0 <= v[0] < len(emap) and 0 <= v[1] < len(emap[0])


def can_traverse(v, w, emap):
    return elevation(w, emap) <= elevation(v, emap) + 1


def possible_neightbors(v, emap):
    for d in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
        w = (v[0] + d[0], v[1] + d[1])
        if in_bounds(w, emap) and can_traverse(v, w, emap):
            yield w


def shortest_path(start, end, emap):
    visited = []
    queue = [[start]]

    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in visited:
            neighbours = list(possible_neightbors(node, emap))
            for neighbour in neighbours:
                if neighbour == end:
                    return len(path)
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
            visited.append(node)


def part1(emap):
    start = pos(emap, 'S')
    end = pos(emap, 'E')
    print(shortest_path(start, end, emap))


def find_starts(emap):
    for i in range(len(emap)):
        for j in range(len(emap[0])):
            if emap[i][j] == 'a':
                yield (i, j)


def part2(emap):
    end = pos(emap, 'E')
    num_steps = []
    for start in find_starts(emap):
        steps = shortest_path(start, end, emap)
        if steps is not None:
            num_steps.append(steps)
    print(min(num_steps))


if __name__ == '__main__':
    emap = parse()
    part1(emap)
    part2(emap)
