from collections import defaultdict
from dataclasses import dataclass

@dataclass
class ChangeDirectory:
    to: str

@dataclass
class FileEntry:
    size: int
    name: str


def parse():
    with open('day7.txt') as f:
        entries = []
        for line in f:
            tokens = line.split()
            match tokens:
                case ['$', 'cd', dst]: entries.append(ChangeDirectory(dst))
                case ['$', _]: pass
                case ['dir', _]: pass
                case [size, name]: entries.append(FileEntry(int(size), name))
        return entries[1:]


def solve(entries):
    current_dir = ['/']
    dir_sizes = defaultdict(int)
    for entry in entries:
        match entry:
            case ChangeDirectory('..'):
                current_dir.pop()
            case ChangeDirectory(to):
                current_dir.append(to)
            case FileEntry(size, name):
                for i in range(len(current_dir)):
                    path = '/'.join(current_dir[:i+1])
                    dir_sizes[path] += size

    # Part 1
    sum_of_dirs = sum(size for path, size in dir_sizes.items() if size <= 100000)
    print(sum_of_dirs)

    to_free = 30000000 - (70000000 - dir_sizes['/'])
    large_dirs = filter(lambda x: x[1] >= to_free, dir_sizes.items())
    print(min(large_dirs, key=lambda x: x[1]))


if __name__ == '__main__':
    entries = parse()
    solve(entries)
