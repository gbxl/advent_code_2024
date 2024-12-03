def get_safe_levels(reports):
    count = 0
    for report in reports:
        increasing = report[1] > report[0]
        bad_levels = 0
        for i in range(1, len(report)):
            diff = abs(report[i-1] - report[i])
            if diff > 3 or diff < 1:
                bad_levels += 1
            elif increasing and report[i-1] >= report[i]:
                bad_levels += 1
            elif not increasing and report[i-1] <= report[i]:
                bad_levels += 1
            if bad_levels > 1:
                break
        if bad_levels < 2:
            count += 1
    return count


def main():
    with open('/Users/lucasg/work/advent_code_2024/day_2/input.txt', 'r') as file:
        lines = file.readlines()
    reports = []
    for line in lines:
        levels = [int(x) for x in line.strip().split(" ")]
        reports.append(levels)
    res = get_safe_levels(reports)
    print(res)

if __name__ == '__main__':
    main()