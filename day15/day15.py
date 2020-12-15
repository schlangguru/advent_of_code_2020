import copy
from typing import List

import sys
sys.path.append("util")
from decorators import benchmark
import util


@benchmark
def part01(start_numbers: List[int], turns=2020):
    numbers = [*start_numbers]
    for idx in range(len(start_numbers), turns):
        last_number = numbers[idx - 1]
        try:
            last_idx = len(numbers) - numbers[::-1].index(last_number, 1)
            new_number = idx - last_idx
        except ValueError:
            new_number = 0

        numbers.append(new_number)

    return numbers[-1]


@benchmark
def part02(start_numbers: List[int], turns=30_000_000):
    last_spoken = {number: idx for idx, number in enumerate(start_numbers[:-1])}
    last_number = start_numbers[-1]
    for idx in range(len(start_numbers), turns):
        try:
            last_idx = last_spoken[last_number]
            new_number = idx - 1 - last_idx
        except KeyError:
            new_number = 0

        last_spoken[last_number] = idx - 1
        last_number = new_number

    return last_number


def main(input_file: str = "input.txt"):
    print(f"Part01 - 2020th number: {part01([0,14,6,20,1,4])}")
    print(f"Part02 - 30.000.000th number: {part02([0,14,6,20,1,4])}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()