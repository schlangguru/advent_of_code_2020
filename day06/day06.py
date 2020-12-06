import os
import re
from functools import reduce
from operator import add

def parse_answers(input):
    group_answers = input.split("\n\n")
    return list(map(parse_group_answers, group_answers))

def parse_group_answers(input):
    group_answers = [answer.strip() for answer in input.split("\n") if len(answer) > 0]
    return list(filter(lambda x: x != "", group_answers))

def count_any_group_yes(group_answers):
    combined_answers = reduce(add, group_answers, "")
    return len(set(combined_answers))

def count_group_yes(group_answers):
    if len(group_answers) == 1:
        return len(group_answers[0])
    intersected_answers = reduce(intersect, group_answers)
    if len(intersected_answers) > 0:
        return len(intersected_answers)
    return 0

def intersect(list1, list2):
    return [x for x in list1 if x in list2]

def part01(input):
    answers = parse_answers(input)
    return sum(map(count_any_group_yes, answers))

def part02(input):
    answers = parse_answers(input)
    return sum(map(count_group_yes, answers))

def main():
    working_dir = os.path.dirname(__file__)
    input_file = os.path.join(working_dir, "input.txt")

    content = ""
    with open(input_file, 'r') as f:
        content = f.read()

    print("Part01 - Result:", part01(content))
    print("Part02 - Result:", part02(content))

if __name__ == '__main__':
    main()