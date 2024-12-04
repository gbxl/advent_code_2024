def count_xmas(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "A":
                if diag_left(i, j, grid) and diag_right(i, j, grid):
                    count += 1
    return count

def diag_left(i, j, grid):
    """
    i-1, j-1 M.. or S..
             .A.    .A.
    i+1, j+1 ..S    ..M
    """
    if i - 1 < 0 or j-1 < 0 or i+1 >= len(grid) or j+1 >= len(grid[i]):
        return False
    if (grid[i-1][j-1] == "M" and grid[i+1][j+1] == "S") or (grid[i-1][j-1] == "S" and grid[i+1][j+1] == "M"):
        return True
    return False


def diag_right(i, j, grid):
    """
    i-1, j+1 ..M or ..S
             .A.    .A.
    i+1, j-1 S..    M..
    """
    if i - 1 < 0 or j-1 < 0 or i+1 >= len(grid) or j+1 >= len(grid[i]):
        return False
    if (grid[i-1][j+1] == "M" and grid[i+1][j-1] == "S") or (grid[i-1][j+1] == "S" and grid[i+1][j+-1] == "M"):
        return True
    return False



def main():
    with open('/Users/lucasg/work/advent_code_2024/day_4/input.txt', 'r') as file:
        lines = file.readlines()
    grid = [list(line.strip()) for line in lines]
    result = count_xmas(grid)
    print(result)


if __name__ == '__main__':
    main()