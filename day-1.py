import sys

from pathlib import Path


example = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""


def process_input(text: str) -> list[str]:
    return text.split('\n')


def pt1(lines: list[str]) -> int:
    print(lines)
    zero_count = 0
    current_position = 50

    for line in lines:
        multiplier = 1 if line[0] == 'R' else -1
        delta = int(line[1:])
        current_position = (current_position + delta * multiplier) % 100
        
        if current_position == 0:
            zero_count += 1

    return zero_count


def pt2(lines: list[str]) -> int:
    zero_count = 0
    current_position = 50
    
    for line in lines:
        delta = 1 if line[0] == 'R' else -1
        repetition = int(line[1:])
        
        for _ in range(repetition):
            current_position = (current_position + delta) % 100
            
            if current_position == 0:
                zero_count += 1

    return zero_count


if __name__ == "__main__":
    problem = process_input(
        example if len(sys.argv) == 1
        else Path(sys.argv[1]).open().read()
    )

    print(pt1(problem))
    print(pt2(problem))