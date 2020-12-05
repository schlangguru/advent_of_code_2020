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


def part02(boarding_passes):
    rows = list(range(ROW_COUNT))
    cols = list(range(COL_COUNT))

    possible_seats = []
    for row in rows:
        for col in cols:
            possible_seats.append((row, col))

    taken_seats = []
    for boarding_pass in boarding_passes:
        row_indicators = boarding_pass[0:7]
        col_indicators = boarding_pass[7:10]

        [row] = reduce(binary_search, row_indicators, rows)
        [col] = reduce(binary_search, col_indicators, cols)
        taken_seats.append((row, col))

    free_seats = [seat for seat in possible_seats if seat not in taken_seats]
    free_seat_ids = list(map(lambda row_col: seat_id(row_col[0], row_col[1]), free_seats))
    taken_seat_ids = list(map(lambda row_col: seat_id(row_col[0], row_col[1]), taken_seats))
    my_seat = list(filter(lambda seat_id: (seat_id+1) in taken_seat_ids and (seat_id-1) in taken_seat_ids, free_seat_ids))

    return my_seat[0]


def main():
    working_dir = os.path.dirname(__file__)
    input_file = os.path.join(working_dir, "input.txt")

    lines = []
    with open(input_file, 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    print("Part01 - Highest seat ID:", part01(lines))
    print("Part02 - My Seat ID:", part02(lines))

if __name__ == "__main__":
    main()