import sys

from pathlib import Path


example = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""


def process_input(text: str) -> list[list[int]]:
    return [[int(coord) for coord in line.split(',')] for line in text.split('\n')]


def find_circuit(coord: list[int], circuits: list[list[list[int]]]) -> int:
    for i in range(len(circuits)):
        if coord in circuits[i]:
            return i
    return -1


def pt1(coords: list[list[int]], is_example: bool) -> int:
    edges = sorted([
        (i, j, (x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)
        for i, (x1, y1, z1) in enumerate(coords)
        for j, (x2, y2, z2) in enumerate(coords)
        if j > i
    ], key=lambda x: x[-1])

    circuits = [[coord] for coord in coords]

    for k in range(10 if is_example else 1000):
        i_idx = find_circuit(coords[edges[k][0]], circuits)
        j_idx = find_circuit(coords[edges[k][1]], circuits)

        if i_idx != j_idx:
            circuits[i_idx] += circuits[j_idx]
            del circuits[j_idx]
    
    circuits.sort(key=lambda x: len(x), reverse=True)

    return len(circuits[0]) * len(circuits[1]) * len(circuits[2])


def pt2(coords: list[list[int]]) -> int:
    edges = sorted([
        (i, j, (x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)
        for i, (x1, y1, z1) in enumerate(coords)
        for j, (x2, y2, z2) in enumerate(coords)
        if j > i
    ], key=lambda x: x[-1])

    circuits = [[coord] for coord in coords]

    k = -1
    while len(circuits) != 1:
        k += 1
        i_idx = find_circuit(coords[edges[k][0]], circuits)
        j_idx = find_circuit(coords[edges[k][1]], circuits)

        if i_idx != j_idx:
            circuits[i_idx] += circuits[j_idx]
            del circuits[j_idx]

    return coords[edges[k][0]][0] * coords[edges[k][1]][0]


if __name__ == "__main__":
    problem = process_input(
        example if len(sys.argv) == 1
        else Path(sys.argv[1]).open().read()
    )
   
    print(pt1(problem, len(sys.argv) == 1))
    print(pt2(problem))