from collections import defaultdict


def count_antinodes(grid):
    pos = set()
    antennas = defaultdict(set)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == ".":
                continue
            antennas[grid[i][j]].add((i, j))
    print(antennas)
    for v in antennas.values():
        v_list = list(v)
        while len(v_list) > 0:
            left = v_list.pop(0)
            for i in range(len(v_list)):
                i_pos = left[0] - (v_list[i][0] - left[0])
                j_pos = left[1] - (v_list[i][1] - left[1])
                if i_pos >=0 and i_pos < len(grid) and j_pos >= 0 and j_pos < len(grid[0]):
                    pos.add((i_pos, j_pos))
                i_pos = v_list[i][0] + (v_list[i][0] - left[0])
                j_pos = v_list[i][1] + (v_list[i][1] - left[1])
                if i_pos >=0 and i_pos < len(grid) and j_pos >= 0 and j_pos < len(grid[0]):
                    pos.add((i_pos, j_pos))
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

"""
 0123456789
0..........
1...#...... => 1,3
2#......... => 2,0
3....a..... -> 3,4
4........a. -> 4,8
5.....a.... -> 5,5
6..#....... => 6,2
7......A... => 7,6
8..........
9..........
"""