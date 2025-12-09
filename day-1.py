def process_file() -> list[str]:
    with open('input.txt', 'r') as file:
        lines = [line.strip('\n') for line in file.readlines()]
    
    return lines


def pt1(lines: list[str]) -> int:
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
    print(pt1(process_file()))
    print(pt2(process_file()))