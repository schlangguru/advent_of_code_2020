import os

TREE = '#'
SPACE = '.'

SLOPE = []
CURRENT_POS = [0, 0]

def move(x, y):
    CURRENT_POS[0] = (CURRENT_POS[0] + x) % len(SLOPE[0])
    CURRENT_POS[1] += y



def is_tree():
    char = SLOPE[CURRENT_POS[1]][CURRENT_POS[0]]
    return char == TREE

def is_at_end():
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

def main():
    working_dir = os.path.dirname(__file__)
    input_file = os.path.join(working_dir, "input.txt")

    slope = []
    with open(input_file, 'r') as f:
        slope = [line.strip() for line in f.readlines()]

    print("Part 01 - Number of trees:", part01(slope))

if __name__ == "__main__":
    main()