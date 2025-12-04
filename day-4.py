def process_file():
    with open("input.txt", "r") as f:
        grid = [[char for char in line.strip('\n')] for line in f.readlines()]
    
    return grid


def get_surrounding(grid: list[list[str]], row: int, col: int) -> int:
    surrounding = 0

    if col > 0:
        surrounding += 1 if grid[row][col-1] == '@' else 0
    if col < len(grid[row])-1:
        surrounding += 1 if grid[row][col+1] == '@' else 0

    if row > 0:
        surrounding += 1 if grid[row-1][col] == '@' else 0
        if col > 0:
            surrounding += 1 if grid[row-1][col-1] == '@' else 0
        if col < len(grid)-1:
            surrounding += 1 if grid[row-1][col+1] == '@' else 0

    if row < len(grid)-1:
        surrounding += 1 if grid[row+1][col] == '@' else 0
        if col > 0:
            surrounding += 1 if grid[row+1][col-1] == '@' else 0
        if col < len(grid[row])-1:
            surrounding += 1 if grid[row+1][col+1] == '@' else 0
    
    return surrounding



def pt1(grid: list[list[str]]) -> int:
    accessible = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != '@':
                continue

            surrounding = get_surrounding(grid, i, j)
            
            if surrounding < 4:
                accessible += 1

    return accessible


def pt2(grid: list[list[str]]) -> int:
    total_removed = 0
    keep_going = True

    while (keep_going):
        keep_going = False

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != '@':
                    continue

                surrounding = get_surrounding(grid, i, j)
                
                if surrounding < 4:
                    total_removed += 1
                    grid[i][j] = 'x'
                    keep_going = True

    return total_removed


if __name__ == "__main__":
    print(pt2(process_file()))