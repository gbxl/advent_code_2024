from collections import defaultdict


def count_antinodes(grid):
    pos = set()
    antennas = defaultdict(set)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == ".":
                continue
            antennas[grid[i][j]].add((i, j))
    for v in antennas.values():
        v_list = list(v)
        if len(v_list) > 1:
            [pos.add(p) for p in v_list]
        while len(v_list) > 0:
            left = v_list.pop(0)
            for i in range(len(v_list)):
                i_diff = (v_list[i][0] - left[0])
                j_diff = (v_list[i][1] - left[1])
                i_pos = left[0] - i_diff
                j_pos = left[1] - j_diff
                while i_pos >=0 and i_pos < len(grid) and j_pos >= 0 and j_pos < len(grid[0]):
                    pos.add((i_pos, j_pos))
                    i_pos = i_pos - i_diff
                    j_pos = j_pos - j_diff
                i_pos = v_list[i][0] + i_diff
                j_pos = v_list[i][1] + j_diff
                while i_pos >=0 and i_pos < len(grid) and j_pos >= 0 and j_pos < len(grid[0]):
                    pos.add((i_pos, j_pos))
                    i_pos = i_pos + i_diff
                    j_pos = j_pos + j_diff
    return pos


def main():
    with open('/Users/lucasg/work/advent_code_2024/day_8/input.txt', 'r') as file:
        lines = file.readlines()
    grid = [list(line.strip()) for line in lines]
    result = count_antinodes(grid)
    print(result)
    print(len(result))


if __name__ == '__main__':
    main()
