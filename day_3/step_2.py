import re


def main():
    with open('/Users/lucasg/work/advent_code_2024/day_3/input.txt', 'r') as file:
        file = file.read()
    pattern = r"(do\(\)|don't\(\)|mul\((\d+),(\d+)\))"
    matches = re.findall(pattern, file)
    result = 0
    skip = False
    for match in matches:
        if match[0] == "do()":
            skip = False
        elif match[0] == "don't()":
            skip = True
        elif not skip:
            result += int(match[1]) * int(match[2])
    print(result)

if __name__ == '__main__':
    main()