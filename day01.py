import itertools

def parse():
    with open('day1.txt') as f:
        lines = f.readlines()
        all_foods = [list(v) for k, v in itertools.groupby(lines, lambda x: x == '\n') if not k]
        int_foods = [[int(food) for food in foods] for foods in all_foods]
        return {k: v for (k, v) in enumerate(int_foods, 1)}


def solve(food_by_elf):
    summarized = ((k, sum(v)) for (k, v) in food_by_elf.items())
    sorted_by_cals = sorted(summarized, key=lambda x: x[1], reverse=True)
    top_3 = list(sorted_by_cals)[:3]

    return(top_3[0][1], sum((f[1] for f in top_3)))


if __name__ == '__main__':
    food_by_elf = parse()
    print(solve(food_by_elf))
