import os
import re
from functools import reduce
from operator import add

def parse_answers(input):
    group_answers = input.split("\n\n")
    return list(map(parse_group_answers, group_answers))

def parse_group_answers(input):
    return [answer.strip() for answer in input.split("\n") if len(answer) > 0]

def count_any_group_yes(group_answers):
    combined_answers = reduce(add, group_answers, "")
    return len(set(combined_answers))

def part01(input):
    answers = parse_answers(input)
    return sum(map(count_any_group_yes, answers))


def main():
    working_dir = os.path.dirname(__file__)
    input_file = os.path.join(working_dir, "input.txt")

    content = ""
    with open(input_file, 'r') as f:
        content = f.read()

    print("Part01 - Result:", part01(content))

if __name__ == '__main__':
    main()