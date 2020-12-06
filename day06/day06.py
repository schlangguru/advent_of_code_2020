import os
import re

def parse_answers(input):
    group_answers = [re.sub(r"\s", "", x) for x in input.split("\n\n")]
    return sum(list(map(count_group_answers, group_answers)))

def count_group_answers(answers):
    return len(set(answers))

def remove_duplicates(from_list):
    return set(from_list)


def part01(input):
    return parse_answers(input)

def main():
    working_dir = os.path.dirname(__file__)
    input_file = os.path.join(working_dir, "input.txt")

    content = ""
    with open(input_file, 'r') as f:
        content = f.read()

    print("Part01 - Result:", part01(content))

if __name__ == '__main__':
    main()