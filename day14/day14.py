import os
import copy
import re
from typing import List, Tuple, Dict

import sys
sys.path.append("util")
from decorators import benchmark
import util


@benchmark
def part01(actions: List[str]):
    pass

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
    print(f"Part02 - Manhattan distance {part02(copy.deepcopy(actions))}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()