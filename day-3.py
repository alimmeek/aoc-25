def process_file():
    with open("input.txt", "r") as f:
        battery_packs = [line.strip('\n') for line in f.readlines()]
    
    return battery_packs


def pt1(battery_packs: list[str]):
    sum = 0

    for pack in battery_packs:
        pack_str = [char for char in pack]
        largest = sorted(pack_str, reverse=True)[0]
        largest_index = pack_str.index(largest)

        if (largest_index == len(pack_str)-1):
            second = sorted(pack_str, reverse=True)[1]
            joltage = int(str(second) + str(largest))
        else:
            second = sorted(pack_str[largest_index+1:], reverse=True)[0]
            joltage = int(str(largest) + str(second))
        
        sum += joltage

    return sum


def pt2(battery_packs: list[str]):
    sum = 0

    for pack in battery_packs:
        pack_i = [int(x) for x in pack]

        final_num = [0 for _ in range(12)]
        positions = [0 for _ in range(12)]

        final_num[0] = max(pack_i[:-11])
        positions[0] = pack_i.index(final_num[0])
        pack_i[positions[0]] = 0

        for i in range(1, 11):
            final_num[i] = max(pack_i[positions[i-1]+1:][:-11 + i])
            positions[i] = positions[i-1]+1+pack_i[positions[i-1]+1:].index(final_num[i])
            pack_i[positions[i]] = 0
        final_num[-1] = max(pack_i[positions[-2]+1:])
        
        sum += int("".join([str(digit) for digit in final_num]))

    return sum


if __name__ == "__main__":
    print(pt2(process_file()))
