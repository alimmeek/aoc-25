def process_file() -> list[list[int]]:
    with open("input.txt", "r") as f:
        coords = [[int(coord) for coord in line.strip('\n').split(',')] for line in f.readlines()]
    
    return coords


def find_circuit(coord: list[int], circuits: list[list[list[int]]]) -> int:
    for i in range(len(circuits)):
        if coord in circuits[i]:
            return i
    return -1


def pt1(coords: list[list[int]]) -> int:
    edges = sorted([
        (i, j, (x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)
        for i, (x1, y1, z1) in enumerate(coords)
        for j, (x2, y2, z2) in enumerate(coords)
        if j > i
    ], key=lambda x: x[-1])

    circuits = [[coord] for coord in coords]

    for k in range(1000):
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
   print(pt1(process_file()))
   print(pt2(process_file()))