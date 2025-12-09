def process_file() -> list[list[str]]:
    with open("input.txt", "r") as f:
        grid = [[word for word in line.strip('\n').split(' ')] for line in f.readlines()]
    
    return grid


def pt1(grid_p: list[list[str]]) -> int:
    sum = 0

    grid = [[word for word in line if word != ''] for line in grid_p]

    for j in range(len(grid[0])):
        op = grid[-1][j]
        running_total = 0 if op == '+' else 1
        for i in range(len(grid)-1):
            if op == '+':
                running_total += int(grid[i][j])
            elif op == '*':
                running_total *= int(grid[i][j])

        sum += running_total

    return sum


def pt2() -> int:
    sum = 0

    with open("input.txt", "r") as f:
        grid = [[word for word in line.strip('\n')] for line in f.readlines()]

    transpose = [[grid[j][i] for j in range(len(grid)-1)] for i in range(len(grid[0]))]
    ops = [grid[-1][i] for i in range(len(grid[-1])) if grid[-1][i] in ['+', '*']]

    op_idx = 0
    running_total = 0 if ops[op_idx] == '+' else 1
    for i in range(len(transpose)):
        if (i+1) % 4 == 0:
            op_idx += 1
            sum += running_total
            running_total = 0 if ops[op_idx] == '+' else 1
            continue
        num = int(''.join(transpose[i]).strip())
        if ops[op_idx] == '+':
            running_total += num
        elif ops[op_idx] == '*':
            running_total *= num
            
    sum += running_total
    return sum


if __name__ == "__main__":
    print(pt1(process_file()))
    print(pt2())