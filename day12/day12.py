import os
import copy
import re
from typing import List, Tuple, Dict

import sys
sys.path.append("util")
from decorators import benchmark
import util

from ship import Ship

ACTION_PATTEN = re.compile(r"(\w)(\d+)")

def parse_actions(input: List[str]) -> List[Tuple[chr, int]]:
    return list(map(parse_action, input))

def parse_action(input: str) -> Tuple[chr, int]:
    match = ACTION_PATTEN.match(input)
    if match:
        return (match.group(1), int(match.group(2)))

    raise Exception(f"Action {input} does not match the pattern {ACTION_PATTEN}")

@benchmark
def part01(actions: List[str]):
    actions = parse_actions(actions)
    ship = Ship()
    for action, value in actions:
        ship.action(action, value)

    return ship.manhattan_distance


@benchmark
def part02(actions: List[str]):
    pass


def main(input_file: str = "input.txt"):
    working_dir = os.path.dirname(__file__)
    input = os.path.join(working_dir, input_file)

    actions = []
    with open(input, 'r') as f:
        actions = [line.strip() for line in f.readlines()]

    print(f"Part01 - Manhattan distance {part01(copy.deepcopy(actions))}")
    # print(f"Part02 - Result {part02(copy.deepcopy(actions))}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()