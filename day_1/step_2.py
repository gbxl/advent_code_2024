from collections import defaultdict


def calculate_sim_score(list_a, list_b):
    counts = defaultdict(int)
    for item in list_b:
        counts[item] += 1
    total = 0
    for item in list_a:
        total += counts.get(item, 0) * item
    return total

def main():
    with open('/Users/lucasg/work/advent_code_2024/day_1/input.txt', 'r') as file:
        lines = file.readlines()
    list_a, list_b = [], []
    for line in lines:
        a, b = line.strip().split("   ")
        list_a.append(int(a))
        list_b.append(int(b))
    list_a.sort()
    res = calculate_sim_score(list_a=list_a, list_b=list_b)
    print(res)

if __name__ == '__main__':
    main()