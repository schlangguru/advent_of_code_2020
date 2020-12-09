import os
import re
import itertools

from typing import List, Tuple, Dict
import sys
sys.path.append("util")

from decorators import benchmark

def is_value_valid(preamble: List[int], value: int) -> bool:
    sums = map(sum, itertools.combinations(preamble, 2))
    return value in sums

def find_contiguous_set_for_number(number: int, data: List[int]):
    summand_count = 2
    while summand_count <= len(data):
        for summands in sliding_window(data, summand_count):
            if sum(summands) == number:
                return summands
        summand_count += 1

    raise Exception(f"No numbers found in data that sum to {number}")

def sliding_window(list: List[any], window_size):
    start = 0
    while start < len(list):
        end = start + window_size
        if end > len(list):
            end = len(list)
        yield list[start:end]
        start += 1


@benchmark
def part01(data: List[int], preamble_length = 25):
    for list in sliding_window(data, preamble_length + 1):
        preamble = list[0:preamble_length]
        value = list[preamble_length]
        if not is_value_valid(preamble, value):
            return value

    raise Exception("No invalid number found")

@benchmark
def part02(data: List[int], preamble_length = 25):
    invalid_number = part01(data, preamble_length)
    summands = find_contiguous_set_for_number(invalid_number, data)
    return min(summands) + max(summands)

def main():
    working_dir = os.path.dirname(__file__)
    input = os.path.join(working_dir, "input.txt")

    data = []
    with open(input, 'r') as f:
        data = [int(line.strip()) for line in f.readlines()]

    print("Part01 - First invalid number:", part01(data))
    print("Part02 - Result:", part02(data))

if __name__ == "__main__":
    main()