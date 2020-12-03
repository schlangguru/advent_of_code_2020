import os
from functools import reduce

TREE = '#'
SPACE = '.'

SLOPE = []
CURRENT_POS = [0, 0]

def move(x, y):
    """
    Move the current postion x to right and y down.
    """
    CURRENT_POS[0] = (CURRENT_POS[0] + x) % len(SLOPE[0])
    CURRENT_POS[1] += y

def is_tree():
    """
    Checks if there is a tree at the current positon.
    """
    char = SLOPE[CURRENT_POS[1]][CURRENT_POS[0]]
    return char == TREE

def is_at_end():
    """
    Checks if the sled is at the and of the slope.
    """
    return CURRENT_POS[1] >= len(SLOPE)

def part01(slope):
    global SLOPE
    SLOPE = slope
    tree_count = 0
    while not is_at_end():
        if is_tree():
            tree_count += 1
        move(3, 1)

    return tree_count

def part02(slope):
    global SLOPE, CURRENT_POS
    SLOPE = slope
    tree_counts = []
    movements = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for movement in movements:
        CURRENT_POS = [0, 0]
        tree_count = 0
        while not is_at_end():
            if is_tree():
                tree_count += 1
            move(*movement)
        tree_counts.append(tree_count)

    return reduce(lambda x, y: x * y, tree_counts)

def main():
    working_dir = os.path.dirname(__file__)
    input_file = os.path.join(working_dir, "input.txt")

    slope = []
    with open(input_file, 'r') as f:
        slope = [line.strip() for line in f.readlines()]

    print("Part 01 - Number of trees:", part01(slope))
    print("Part 02 - Result:", part02(slope))

if __name__ == "__main__":
    main()