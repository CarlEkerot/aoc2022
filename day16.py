import re

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
        print(valves)

        # Assign indices
        idx_map = dict()
        for i, v in enumerate(valves):
            idx_map[v[0]] = i
        
        # Build ajd. matrix
        m = [[0 for _ in range(len(valves))] for _ in range(len(valves))]
        
        for src, rate, dsts in valves:
            src_idx = idx_map[src]
            for dst in dsts:
                dst_idx = idx_map[dst]
                m[src_idx][dst_idx] = rate
                m[dst_idx][src_idx] = rate
        
        [print(' '.join(map(lambda x: str(x).ljust(2, ' '), r))) for r in m]
        return m

            


if __name__ == '__main__':
    parse()

