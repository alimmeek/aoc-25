def process_file() -> list[list[str]]:
    with open("input.txt", "r") as f:
        grid = [[char for char in line.strip('\n')] for line in f.readlines()]
    
    return grid


def pt1(grid: list[list[str]]) -> int:
    splits = 0
    grid[0][grid[0].index('S')] = '|'

    for i in range(1, len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '^' and grid[i-1][j] == '|':
                splits += 1
                if j > 0:
                    grid[i][j-1] = '|'
                if j < len(grid[0]) - 1:
                    grid[i][j+1] = '|'
            elif grid[i-1][j] == '|':
                grid[i][j] = '|'

    return splits


def pt2(grid: list[list[str]]) -> int:
    grid[0][grid[0].index('S')] = '1'

    for i in range(1, len(grid)):
        for j in range(len(grid[0])):
            if not grid[i-1][j].isdigit():
                continue

            if grid[i][j] == '^':
                if j > 0:
                    if grid[i][j-1].isdigit():
                        grid[i][j-1] = str(int(grid[i][j-1]) + int(grid[i-1][j]))
                    else:
                        grid[i][j-1] = str(int(grid[i-1][j]))

                if j < len(grid[0]) - 1:
                    if grid[i][j+1].isdigit():
                        grid[i][j+1] = str(int(grid[i][j+1]) + int(grid[i-1][j]))
                    else:
                        grid[i][j+1] = str(int(grid[i-1][j]))

            else:
                if grid[i][j].isdigit():
                    grid[i][j] = str(int(grid[i][j]) + int(grid[i-1][j]))
                else:
                    grid[i][j] = str(int(grid[i-1][j]))

    return sum(int(cell) for cell in grid[-1] if cell.isdigit())


if __name__ == "__main__":
    print(pt1(process_file()))
    print(pt2(process_file()))