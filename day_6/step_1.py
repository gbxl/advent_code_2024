def predict_path(grid):
    pos = None
    # directions = ["N", "E", "S", "W"]
    direction_idx = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "^":
                pos = (i, j)
    positions = set()
    positions.add(pos)
    while True:
        pos = advance(direction_idx, pos, grid, positions)
        if pos and (0 <= pos[0] < len(grid)) and (0 <= pos[1] < len(grid[0])):
            direction_idx = (direction_idx + 1) % 4
        else:
            break

    return len(positions)


def advance(idx, pos, grid, positions):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while (0 <= pos[0] < len(grid)) and (0 <= pos[1] < len(grid[0])):
        di, dj = directions[idx]
        next_i, next_j = pos[0] + di, pos[1] + dj
        if grid[next_i][next_j] == "#":
            return pos
        else:
            pos = (next_i, next_j)
            if (0 <= next_i < len(grid)) and (0 <= next_j < len(grid[0])):
                positions.add(pos)
    

def main():
    with open('/Users/lucasg/work/advent_code_2024/day_6/input.txt', 'r') as file:
        lines = file.readlines()
    grid = [list(line.strip()) for line in lines]
    result = predict_path(grid)
    print(result)


if __name__ == '__main__':
    main()