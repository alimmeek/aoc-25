import sys

from pathlib import Path


example = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""


def process_input(text: str) -> tuple[list[tuple[int,int]], list[int]]:
    intervals: list[tuple[int,int]] = []
    ids: list[int] = []
    new_line_reached = False

    for line in text.split('\n'):
        if line == '':
            new_line_reached = True
            continue

        if not new_line_reached:
            start, end = map(int, line.split('-'))
            intervals.append((start, end))
        else:
            ids.append(int(line))
    
    return intervals, ids


def pt1(intervals: list[tuple[int,int]], ids: list[int]) -> int:
    valid_count = 0

    for id in ids:
        for start, end in intervals:
            if start <= id <= end:
                valid_count += 1
                break

    return valid_count


def merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]
    for start, end in intervals[1:]:
        last_start, last_end = merged[-1]

        if start <= last_end:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))

    return merged


def pt2(intervals:list[tuple[int, int]]) -> int:
    return sum((interval[1] - interval[0] + 1) for interval in merge_intervals(intervals))


if __name__ == '__main__':
    intervals, ids = process_input(
        example if len(sys.argv) == 1
        else Path(sys.argv[1]).open().read()
    )

    print(pt1(intervals, ids))
    print(pt2(intervals))