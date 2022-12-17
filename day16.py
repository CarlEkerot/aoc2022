import re
from functools import cache
from dataclasses import dataclass
from copy import deepcopy


@dataclass()
class Valve:
    name: str
    pressure: int
    neighbors: list[str]


@dataclass()
class Move:
    src: str
    dst: str


@dataclass()
class Open:
    valve: str


REGEX = re.compile('Valve (\w+) has flow rate=(\d+); tunnel(?:s?) lead(?:s?) to valve(?:s?) (.*)')

def parse():
    with open('day16.txt') as f:
        valves = []
        for line in f:
            m = REGEX.match(line).groups()
            src = m[0]
            rate = int(m[1])
            dsts = m[2].strip().split(', ')
            valves.append((src, rate, dsts))

        # Assign indices
        idx_map = dict()
        for i, v in enumerate(valves):
            idx_map[v[0]] = i
        
        print(idx_map)
        # Build ajd. matrix
        m = [[-1 for _ in range(len(valves))] for _ in range(len(valves))]
        
        for src, rate, dsts in valves:
            src_idx = idx_map[src]
            for dst in dsts:
                dst_idx = idx_map[dst]
                m[src_idx][dst_idx] = rate
                m[dst_idx][src_idx] = rate
        
        [print(' '.join(map(lambda x: str(x).ljust(2, ' '), r))) for r in m]
        return m


def parse2():
    with open('day16.txt') as f:
        valves = dict()
        for line in f:
            m = REGEX.match(line).groups()
            src = m[0]
            rate = int(m[1])
            dsts = m[2].strip().split(', ')
            valves[src] = Valve(src, rate, dsts)
    return valves


T = {}

def solve(valve: Valve, valves: dict[Valve], open_valves: set[str], actions):
    key = (valve.name, tuple(open_valves))

    if key in T:
        return T[key]

    #print(actions)
    # At minute 30. Done.
    if len(actions) == 30:
        return sum(valves[v].pressure for v in open_valves)

    # Find max of opening valve vs jut moving
    candidates = [solve(
        valves[n],
        valves,
        open_valves, 
        actions + [Move(valve, n)]
    ) for n in valve.neighbors]
    if valve.name not in open_valves:
        candidates.append(
            solve(
                valve,
                valves,
                open_valves.union({valve.name}), 
                actions + [Open(valve)]
            )
        )
    
    opt = max(candidates)
    if key not in T:
        T[key] = opt

    return opt            


if __name__ == '__main__':
    valves = parse2()
    print(solve(valves['AA'], valves, set(), []))


