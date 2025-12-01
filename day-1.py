def process_file():
    with open('input.txt', 'r') as file:
        lines = [line.strip('\n') for line in file.readlines()]
    
    return lines

def count_zeros_pt1(lines):
    zero_count = 0
    current_position = 50

    for line in lines:
        multiplier = 1 if line[0] == 'R' else -1
        delta = int(line[1:])
        current_position = (current_position + delta * multiplier) % 100
        
        if current_position == 0:
            zero_count += 1

    return zero_count

def count_zeros_pt2(lines):
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