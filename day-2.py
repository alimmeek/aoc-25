import sys

from pathlib import Path


example = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"


def process_input(text: str) -> list[str]:
    return text.strip('\n').split(',')


def pt1(intervals: list[str]) -> int:
    sum = 0
    for interval in intervals:
        low, high = interval.split('-')

        if len(low) % 2 != 0 and len(high) % 2 != 0:
            continue

        for i in range(int(low), int(high)+1):
            if len(str(i)) % 2 != 0:
                continue

            mid = len(str(i)) // 2

            if str(i)[:mid] == str(i)[mid:]:
                sum += i
    
    return sum


def pt2(intervals: list[str]) -> int:
    sum = 0
    for interval in intervals:
        low, high = interval.split('-')

        for i in range(int(low), int(high)+1):
            tmp = str(i)
            lengths = [i for i in range(1, len(tmp)) if len(tmp) % i == 0]

            for length in lengths:
                char_set = set([tmp[i:i+length] for i in range(0, len(tmp), length)])
                
                if len(char_set) == 1:
                    sum += i
                    break

    return sum


if __name__ == "__main__":
    problem = process_input(
        example if len(sys.argv) == 1
        else Path(sys.argv[1]).open().read()
    )

    print(pt1(problem))
    print(pt2(problem))