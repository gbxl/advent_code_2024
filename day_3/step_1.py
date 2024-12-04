import re


def main():
    with open('/Users/lucasg/work/advent_code_2024/day_3/input.txt', 'r') as file:
        file = file.read()
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, file)
    result = [int(x) * int(y) for x, y in matches]
    print(sum(result))

if __name__ == '__main__':
    main()