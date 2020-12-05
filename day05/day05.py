import os
from functools import reduce

ROW_COUNT = 128
COL_COUNT = 8



def binary_search(list, direction):
    idx = int(len(list) / 2)
    if direction in ['F', 'L']:
        return list[0:idx]
    elif direction in ['B', 'R']:
        return list[idx:len(list)]
    raise Exception(f"Invalid direction {direction}")

def seat_id(row, col):
    return (row * 8) + col

def part01(boarding_passes):
    rows = list(range(ROW_COUNT))
    cols = list(range(COL_COUNT))

    seat_ids = []
    for boarding_pass in boarding_passes:
        row_indicators = boarding_pass[0:7]
        col_indicators = boarding_pass[7:10]

        [row] = reduce(binary_search, row_indicators, rows)
        [col] = reduce(binary_search, col_indicators, cols)
        seat_ids.append(seat_id(row, col))

    return max(seat_ids)

def main():
    working_dir = os.path.dirname(__file__)
    input_file = os.path.join(working_dir, "input.txt")

    lines = []
    with open(input_file, 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    print("Part01 - Highest seat ID:", part01(lines))

if __name__ == "__main__":
    main()