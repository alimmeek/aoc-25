import ast
import numpy as np
import pulp
import sys

from pathlib import Path


example = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""


def process_input(text: str):
    lights = [[char for char in line[1:line.index("]")]] for line in text.split('\n')]
    buttons_read = [[button for button in line[line.index(']')+2:line.index('{')-1].split()] for line in text.split('\n')]
    joltages_read = [line[line.index('{'):] for line in text.split('\n')]

    buttons = [[([t] if isinstance((t := ast.literal_eval(s)), int) else list(t)) for s in sub] for sub in buttons_read]
    joltages = [list(map(int, s.strip('{}').split(','))) for s in joltages_read]

    return lights, buttons, joltages


def pt1(lights: list[list[str]], buttons: list[list[list[int]]]):
    buttons_pushed = 0
    
    for i in range(len(lights)):
        buttons_i = buttons[i]
        t = str(bin(2 ** len(buttons[i])-1))[2:]
        masks = sorted([str(bin(mask))[2:] for mask in range(1, 2 ** len(buttons[i]))], key=lambda x: x.count('1'))
        for mask in masks:
            pushed = [True if bit == '1' else False for bit in '0'*(len(t) - len(mask)) + mask]

            current = [0 for _ in range(len(lights[i]))]
            for j in range(len(buttons_i)):
                if pushed[j]:
                    for light in buttons_i[j]:
                        current[light] ^= 1
            
            if current == [1 if light == '#' else 0 for light in lights[i]]:
                buttons_pushed += mask.count('1')
                break
            
    return buttons_pushed


def pt2(buttons: list[list[list[int]]], joltages: list[list[int]]) -> int:
    button_pushes = 0

    for k in range(len(buttons)):
        m = len(joltages[k])
        n = len(buttons[k])

        A = np.zeros((m, n), dtype=int)
        for j, btn in enumerate(buttons[k]):
            for i in btn:
                A[i, j] += 1

        prob = pulp.LpProblem("ButtonPushes", pulp.LpMinimize)
        x = [pulp.LpVariable(f"x{j}", lowBound=0, cat="Integer") for j in range(n)]

        prob += pulp.lpSum(x)

        for i in range(m):
            prob += pulp.lpSum(A[i, j] * x[j] for j in range(n)) == joltages[k][i]

        prob.solve(pulp.PULP_CBC_CMD(msg=False))
        solution = np.array([int(v.value()) for v in x])

        button_pushes += solution.sum()

    return button_pushes


if __name__ == "__main__":
    lights, buttons, joltages = process_input(
        example if len(sys.argv) == 1
        else Path(sys.argv[1]).open().read()
    )

    print(pt1(lights, buttons))
    print(pt2(buttons, joltages))