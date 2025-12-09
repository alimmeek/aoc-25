import sys

from pathlib import Path
from shapely.geometry import Polygon


example = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""


def process_input(text: str) -> list[list[int]]:
    return [[int(coord) for coord in line.split(',')] for line in text.split('\n')]


def pt1(corners: list[list[int]]) -> int:
    max_area = 0

    for i in range(len(corners)):
        for j in range(i+1, len(corners)):
            max_area = max(max_area, (abs(corners[i][0] - corners[j][0]) + 1) * (abs(corners[i][1] - corners[j][1]) + 1))

    return max_area


def pt2(red: list[list[int]]) -> int:
    red_green = Polygon(red)
    max_area = 0

    for i in range(len(red)):
        for j in range(i+1, len(red)):
            rect = Polygon([(red[i][0], red[i][1]), (red[i][0], red[j][1]), (red[j][0], red[j][1]), (red[j][0], red[i][1])])
            if red_green.contains(rect):                
                max_area = max(max_area, (abs(red[j][0] - red[i][0]) + 1) * (abs(red[j][1] - red[i][1]) + 1))
    
    return max_area


if __name__ == "__main__":
    problem = process_input(
        example if len(sys.argv) == 1
        else Path(sys.argv[1]).open().read()
    )

    print(pt1(problem))
    print(pt2(problem))