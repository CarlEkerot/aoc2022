import copy
import re

REGEX_INPUT = re.compile("(.*)\n\n(.*)", re.MULTILINE | re.DOTALL)
REGEX_MOVES = re.compile("move (\d+) from (\d+) to (\d+)")

def parse():
    with open('day5.txt') as f:
        data = f.read()
        stacks_data, rest = REGEX_INPUT.match(data).groups()

        stacks_lines = stacks_data.split('\n')
        rev_lines = list(reversed(stacks_lines[:-1]))

        stacks = [[] for _ in (range((len(rev_lines[0]) + 1) // 4))]

        for i, line in enumerate(rev_lines):
            for j in range(0, len(stacks_lines[0]), 4):
                idx = j // 4
                token = line[j+1]
                if token != ' ':
                    stacks[idx].append(token)

        moves = [tuple(map(int, ms)) for ms in REGEX_MOVES.findall(rest)]
        return stacks, moves


def part1(stacks, moves):
    for num, src, dst in moves:
        for _ in range(num):
            x = stacks[src - 1].pop()
            stacks[dst - 1].append(x)

    top = ''
    for stack in stacks:
        top += stack[-1]
    return top


def part2(stacks, moves):
    for num, src, dst in moves:
        intermediate = []
        for _ in range(num):
            x = stacks[src - 1].pop()
            intermediate.append(x)
        stacks[dst - 1].extend(reversed(intermediate))

    top = ''
    for stack in stacks:
        top += stack[-1]
    return top

if __name__ == '__main__':
    stacks, moves = parse()
    print(part1(copy.deepcopy(stacks), moves))
    print(part2(copy.deepcopy(stacks), moves))
