import os
import re
import itertools
from functools import reduce, lru_cache
from operator import mul
from typing import List, Tuple, Dict

import sys
sys.path.append("util")
from decorators import benchmark
import util

def jolt_distributin(ratings: List[int]) -> Dict:
    distribution = {}
    for difference in jolt_differences(ratings):
        if difference in distribution.keys():
            distribution[difference] += 1
        else:
            distribution[difference] = 1

    return distribution


def jolt_differences(ratings: List[int]) -> List[int]:
    differences = []
    ratings.sort()
    for window in util.sliding_window(ratings, window_size = 2, skip_tail = True):
        differences.append(window[1] - window[0])

    return differences


def count_consecutive_ones(list: List[int]) -> List[int]:
    result = []
    sequence = list.copy() # Do not mutate the original list

    count = 0
    while len(sequence) > 0:
        val = sequence.pop(0)
        if val == 1:
            count += 1
        else:
            result.append(count)
            count = 0

    return result


@benchmark
def part01(adapter_ratings: List[int]):
    charger_rating = 0
    my_device_rating = max(adapter_ratings) + 3

    adapter_ratings.append(charger_rating)
    adapter_ratings.append(my_device_rating)

    distribution = jolt_distributin(adapter_ratings)

    return distribution


@benchmark
def part02_tribonacci(adapter_ratings: List[int]):
    charger_rating = 0
    my_device_rating = max(adapter_ratings) + 3

    adapter_ratings.append(charger_rating)
    adapter_ratings.append(my_device_rating)

    differences = jolt_differences(adapter_ratings)
    print("Differences: ", differences)
    # Insepect the differences
    # There are only differences with size 1 and 3
    print("Number of differences with size 2: ", differences.count(2)) # == 0

    # Since there are only 1s and 3s as differences we can count the sequence of consecutive 1s
    consecutive_ones = count_consecutive_ones(differences)
    print("Consecutive ones", consecutive_ones)
    # The longest sequence of consecutive 1s is 4
    print("Longest sequence of consecutive 1s:", max(consecutive_ones)) # == 4

    # If we have 0 consecutive 1s => we get 1 possible arrangement of this sub sequence (1)
    # If we have 1 consecutive 1s => we get 1 possible arrangement of this sub-sequence (1)
    # If we have 2 consecutive 1s => we get 2 possible arrangements of this sub-sequence (2)
    # If we have 3 consecutive 1s => we get 4 possible arrangements of this sub-sequence (1 + (1 + (2)))
    # If we have 4 consecutive 1s => we get 7 possible arrangements of this sub-sequence  (1 + (1 + 2 + (4)))
    return pow(2, consecutive_ones.count(2)) * pow(4, consecutive_ones.count(3)) * pow(7, consecutive_ones.count(4))


@benchmark
def part02_recursive(adapter_ratings: List[int]):
    charger_rating = 0
    my_device_rating = max(adapter_ratings) + 3

    adapter_ratings.append(charger_rating)
    adapter_ratings.append(my_device_rating)
    adapter_ratings.sort()

    @lru_cache
    def count_paths(from_idx: int):
        # End of the list reached
        if from_idx == len(adapter_ratings) - 1:
            return 1

        # count all paths from current adapter to all reachable (distance 3) next adapters
        next_idx = from_idx + 1
        paths = 0
        while next_idx < len(adapter_ratings) and (adapter_ratings[next_idx] - adapter_ratings[from_idx] <= 3):
            paths += count_paths(next_idx)
            next_idx += 1

        return paths

    return count_paths(0)

def part02(adapter_ratings: List[int]):
    # We are going to choose 2 different approaches for this one
    # each approach returns the desired result

    # Mathematical approach O(n)
    result1 = part02_tribonacci(adapter_ratings.copy())

    # Recursive approach O(2^n)
    result2 = part02_recursive(adapter_ratings.copy())

    if result1 != result2:
        raise Exception(f"Results are different. Tribonacci: {result1}, Recursive: {result2}")

    return result2


def main():
    working_dir = os.path.dirname(__file__)
    input = os.path.join(working_dir, "input.txt")

    data = []
    with open(input, 'r') as f:
        data = [int(line.strip()) for line in f.readlines()]

    jolt_distributin = part01(data.copy())
    print(f"Part01 - Jolt Distribution: {jolt_distributin}, Result: {jolt_distributin[1] * jolt_distributin[3]}")
    print(f"Part02 - Result: {part02(data.copy())}")


if __name__ == "__main__":
    main()