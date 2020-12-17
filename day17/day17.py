from typing import List
import os

import sys
sys.path.append("util")
from decorators import benchmark

from pocket_dimension import PocketDimension

@benchmark
def part01(initial_state: str):
    dimension = PocketDimension(initial_state, dimensions=3)
    dimension.boot()

    return dimension.active_cube_count()


@benchmark
def part02(initial_state: str):
    dimension = PocketDimension(initial_state, dimensions=4)
    dimension.boot()

    return dimension.active_cube_count()


def main(input_file: str = "input.txt"):
    working_dir = os.path.dirname(__file__)
    input_file = os.path.join(working_dir, input_file)

    initial_state = ""
    with open(input_file, 'r') as f:
        initial_state = f.read().strip()

    print(f"Part01 - Result: {part01(initial_state)}")
    print(f"Part02 - Result: {part02(initial_state)}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()