def parse():
    with open('day6.txt') as f:
        return f.read()


def solve(stream, seq_len):
    for i in range(len(stream)):
        last_four = set(stream[i - seq_len : i])
        if (len(last_four) == seq_len):
            return i

if __name__ == '__main__':
    stream = parse()
    print(solve(stream, 4))
    print(solve(stream, 14))
