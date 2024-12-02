def calculate_distance(list_a, list_b):
    distance = 0
    for i, n in enumerate(list_a):
        distance += abs(n - list_b[i])
    return distance


def main():
    with open('/Users/lucasg/work/advent_code_2024/day_1/input.txt', 'r') as file:
        lines = file.readlines()
    list_a, list_b = [], []
    for line in lines:
        a, b = line.strip().split("   ")
        list_a.append(int(a))
        list_b.append(int(b))
    list_a.sort()
    list_b.sort()
    res = calculate_distance(list_a=list_a, list_b=list_b)
    print(res)

if __name__ == '__main__':
    main()