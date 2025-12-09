import sys

from pathlib import Path


example = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """


def pt1(inp: str) -> int:
    sum = 0

    grid = [line.split() for line in inp.split('\n')]

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


def pt2(inp: str) -> int:
    sum = 0

    grid = [[char for char in line] for line in inp.split('\n')]

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
    problem = example if len(sys.argv) == 1 else Path(sys.argv[1]).open().read()

    print(pt1(problem))
    print(pt2(problem))