import os
import copy
import re
from typing import List, Tuple, Dict

import sys
sys.path.append("util")
from decorators import benchmark
import util

from emulation import Emulator


@benchmark
def part01(instructions: List[str]):
    emulator = Emulator(instructions)
    emulator.run()

    return sum(emulator.mem.values())


@benchmark
def part02(instructions: List[str]):
    pass

def main(input_file: str = "input.txt"):
    working_dir = os.path.dirname(__file__)
    input = os.path.join(working_dir, input_file)

    instructions = []
    with open(input, 'r') as f:
        instructions = [line.strip() for line in f.readlines()]

    print(f"Part01 - Result {part01(copy.deepcopy(instructions))}")
    #print(f"Part02 - Manhattan distance {part02(copy.deepcopy(actions))}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()