from shapely.geometry import Polygon


def process_file() -> list[list[int]]:
    with open("input.txt", "r") as f:
        corners = [[int(coord) for coord in line.strip('\n').split(',')] for line in f.readlines()]

    return corners


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
    print(pt1(process_file()))
    print(pt2(process_file()))