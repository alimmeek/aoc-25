import ast
import numpy as np
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


def pt2(lights: list[list[str]], buttons: list[list[list[int]]], joltages: list[list[int]]):
    buttons_pushed = 0
    
    for k in range(1):
        tmp = np.array([[0 for _ in range(len(lights[k]))] for _ in range(len(buttons[k]))])
        for j in range(len(buttons[k])):
            for idx in buttons[k][j]:
                tmp[j][idx] = 1
                
    return buttons_pushed


if __name__ == "__main__":
    lights, buttons, joltages = process_input(
        example if len(sys.argv) == 1
        else Path(sys.argv[1]).open().read()
    )

    print(pt1(lights, buttons))
    print(pt2(lights, buttons, joltages))