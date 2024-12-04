def count_xmas(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "X":
                lines = is_line(i, j, grid)
                count += lines
                diags = is_diagonal(i, j, grid)
                count += diags
                cols = is_col(i, j, grid)
                count += cols
    return count

def is_col(i, j, grid):
    count = 0
    if i <= len(grid) - 4 and (grid[i][j] == "X" and grid[i+1][j] == "M" and 
        grid[i+2][j] == "A" and grid[i+3][j] == "S"):
        count += 1
    if i >= 3 and (grid[i][j] == "X" and grid[i-1][j] == "M" and 
        grid[i-2][j] == "A" and grid[i-3][j] == "S"):
        count += 1
    return count


def is_diagonal(i, j, grid):
    count = 0
    # Check for "XMAS" diagonally top-left to bottom-right
    if i <= len(grid) - 4 and j <= len(grid[0]) - 4:  # Ensure diagonal is in bounds
        if (grid[i][j] == "X" and grid[i+1][j+1] == "M" and 
            grid[i+2][j+2] == "A" and grid[i+3][j+3] == "S"):
            count += 1
    # Check for "SAMX" diagonally bottom-left to top-right
    if i >= 3 and j <= len(grid[0]) - 4:  # Ensure diagonal is in bounds
        if (grid[i][j] == "X" and grid[i-1][j+1] == "M" and 
            grid[i-2][j+2] == "A" and grid[i-3][j+3] == "S"):
            count += 1
    # Check for "XMAS" diagonally top-right to bottom-left
    if i <= len(grid) - 4 and j >= 3:  # Ensure diagonal is in bounds
        if (grid[i][j] == "X" and grid[i+1][j-1] == "M" and 
            grid[i+2][j-2] == "A" and grid[i+3][j-3] == "S"):
            count += 1
    # Check for "SAMX" diagonally bottom-right to top-left
    if i >= 3 and j >= 3:  # Ensure diagonal is in bounds
        if (grid[i][j] == "X" and grid[i-1][j-1] == "M" and 
            grid[i-2][j-2] == "A" and grid[i-3][j-3] == "S"):
            count += 1
    return count


def is_line(i, j, grid):
    count = 0
    if j <= len(grid[i]) - 4 and grid[i][j:j+4] == ["X", "M", "A", "S"]:
        count += 1
    if j >= 3 and grid[i][j-3:j+1] == ["S", "A", "M", "X"]:
        count += 1
    return count


def main():
    with open('/Users/lucasg/work/advent_code_2024/day_4/input.txt', 'r') as file:
        lines = file.readlines()
    grid = [list(line.strip()) for line in lines]
    result = count_xmas(grid)
    print(result)


if __name__ == '__main__':
    main()