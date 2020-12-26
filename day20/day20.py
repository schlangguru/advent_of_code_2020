import os
import re
from typing import List, Dict, Tuple
import math

import sys
sys.path.append("util")
from decorators import benchmark
import util
import puzzle

@benchmark
def part01(input: str):
    tiles = puzzle.parse_tiles(input)

    return math.prod(map(lambda tile: int(tile.id), puzzle.find_corner_tiles(tiles)))


@benchmark
def part02(input: str):
    tiles = puzzle.parse_tiles(input)
    image = puzzle.build_puzzle(tiles)

    # Find monster
    monster_count = 0
    for image_variation in image.as_tile().variations():
        monster_count = puzzle.count_monster(image_variation.tile)
        if monster_count > 0:
            print("Found # Monsters", monster_count)
            break

    number_of_hash = "".join(image_variation.tile).count('#')

    return number_of_hash - (monster_count * 15)


def main(input_file: str = "input.txt"):
    working_dir = os.path.dirname(__file__)
    input = os.path.join(working_dir, input_file)

    content = []
    with open(input, 'r') as f:
        content = f.read()

    # print(f"Part01 - Result: {part01(content)}")
    print(f"Part02 - Result: {part02(content)}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()