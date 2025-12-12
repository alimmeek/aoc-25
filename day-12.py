from concurrent.futures import ProcessPoolExecutor
from dataclasses import dataclass
from functools import cached_property
from pathlib import Path

import sys


example = """0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2"""


@dataclass(frozen=True)
class Shape:
    grid: list[list[str]]

    @cached_property
    def variants(self) -> list["Shape"]:
        seen: set[tuple[tuple[str, ...], ...]] = set()
        results: list[Shape] = []

        g = self.grid

        for _ in range(4):
            g = rotate90(g)
            canonical = to_immutable(g)

            if canonical not in seen:
                seen.add(canonical)
                results.append(Shape(from_immutable(canonical)))

            flipped = flip(g)
            canonical_f = to_immutable(flipped)

            if canonical_f not in seen:
                seen.add(canonical_f)
                results.append(Shape(from_immutable(canonical_f)))

        return results

    @cached_property
    def cells(self) -> list[tuple[int, int]]:
        return [
            (x, y)
            for y, row in enumerate(self.grid)
            for x, v in enumerate(row)
            if v == '#'
        ]


def to_immutable(g: list[list[str]]) -> tuple[tuple[str, ...], ...]:
    return tuple(tuple(row) for row in g)


def from_immutable(t: tuple[tuple[str, ...], ...]) -> list[list[str]]:
    return [list(row) for row in t]


def rotate90(g: list[list[str]]) -> list[list[str]]:
    return [list(col) for col in zip(*g[::-1])]


def flip(g: list[list[str]]) -> list[list[str]]:
    return [row[::-1] for row in g]


def can_place(W: int, H: int, used: list[list[bool]], cells: list[tuple[int, int]], ox: int, oy: int) -> bool:
    for x, y in cells:
        X, Y = x + ox, y + oy
        if X < 0 or Y < 0 or X >= W or Y >= H:
            return False
        if used[Y][X]:
            return False
    return True


def do_the_bare_minimum(shapes: list[Shape], grid_sizes: list[tuple[int, int]], quantities: list[list[int]]):
    can_fit = 0

    for i in range(len(grid_sizes)):
        required_area = 0
        for shape in shapes:
            required_area += sum(line.count('#') for line in shape.grid) * quantities[i][shapes.index(shape)]
        
        if required_area > grid_sizes[i][0] * grid_sizes[i][1]:
            continue

        can_fit += 1

    return can_fit


def solve_for_realsies(arg: tuple[int, int, list[Shape], list[int]]) -> int:
    width, height, shapes, quantities = arg

    pieces: list[list[list[tuple[int, int]]]] = []
    for shape, qty in zip(shapes, quantities):
        var_list = [v.cells for v in shape.variants]
        for _ in range(qty):
            pieces.append(var_list)

    pieces.sort(key=lambda v: -max(len(c) for c in v))

    used = [[False] * width for _ in range(height)]

    def backtrack(i: int) -> bool:
        if i == len(pieces):
            return True

        for cells in pieces[i]:
            for oy in range(height):
                for ox in range(width):
                    if can_place(width, height, used, cells, ox, oy):
                        for x, y in cells:
                            used[y + oy][x + ox] = True

                        if backtrack(i + 1):
                            return True
                        
                        for x, y in cells:
                            used[y + oy][x + ox] = False

        return False

    return 1 if backtrack(0) else 0


def process_input(text: str) -> tuple[list[Shape], list[tuple[int, int]], list[list[int]]]:
    shapes: list[list[list[str]]] = []
    grid_sizes: list[tuple[int, int]] = []
    quantities: list[list[int]] = []

    for line in text.split('\n'):
        if 'x' in line:
            size = line[:line.index(':')].split('x')
            grid_sizes.append((int(size[0]), int(size[1])))

            tmp = line[line.index(':')+2:]
            quantities.append([int(x) for x in tmp.split()])
        else:
            if ':' not in line and line != '':
                shapes[-1].append([char for char in line])
            elif ':' in line:
                shapes.append([])
    
    return [Shape(shape) for shape in shapes], grid_sizes, quantities


if __name__ == "__main__":
    shapes, grid_sizes, quantities = process_input(
        example if len(sys.argv) == 1
        else Path(sys.argv[1]).open().read()
    )

    print(do_the_bare_minimum(shapes, grid_sizes, quantities))

    total = 0

    tasks = [
        (width, height, shapes, qty)
        for (width, height), qty in zip(grid_sizes, quantities)
    ]

    with ProcessPoolExecutor() as executor:
        for result in executor.map(solve_for_realsies, tasks):
            total += result

    print(total)