def process_file() -> list[str]:
    with open("input.txt", "r") as f:
        intervals = f.readlines()[0].strip('\n').split(',')

    return intervals


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
    print(pt1(process_file()))
    print(pt2(process_file()))