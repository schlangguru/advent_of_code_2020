import os
import re
from typing import List, Dict, Tuple

import sys
sys.path.append("util")
from decorators import benchmark
import util
from matcher import Rule, RuleMatcher


RULE_PATTERN = re.compile(r"^(\d+): (.*)$")


def parse_input(input: str) -> Tuple[Dict[int, Rule], List[str]]:
    parts = input.split('\n\n')
    rules = parse_rules(parts[0].strip())
    messages = list(map(str.strip, parts[1].strip().split('\n')))

    return (rules, messages)


def parse_rules(input: str) -> Dict[int, str]:
    lines = [line.strip() for line in input.split('\n')]
    return {nmb: rule for nmb, rule in map(parse_rule, lines)}


def parse_rule(line: str) -> Tuple[int, Rule]:
    line = line.strip()
    if match := RULE_PATTERN.match(line):
        nmb =  int(match.group(1))
        rule_str = match.group(2)

        if match := re.compile(r"\"(\w+)\"").match(rule_str):
            rule = match.group(1)
        else:
            rule = list(map(lambda s: list(map(lambda x: int(x), s.split(" "))), rule_str.split(" | ")))

        return (nmb, rule)

    raise Exception(f"RULE_PATTERN does not match {line}")


@benchmark
def part01(input: str):
    rules, messages = parse_input(input)
    matcher = RuleMatcher(rules)

    valid_msgs = list(filter(matcher.match, messages))

    return len(valid_msgs)


@benchmark
def part02(input: str):
    rules, messages = parse_input(input)
    matcher = RuleMatcher(rules)

    rules[8] = parse_rule("8: 42 | 42 8")[1]
    rules[11] = parse_rule("11: 42 31 | 42 11 31")[1]

    valid_msgs = list(filter(matcher.match, messages))

    return len(valid_msgs)


def main(input_file: str = "input.txt"):
    working_dir = os.path.dirname(__file__)
    input = os.path.join(working_dir, input_file)

    content = []
    with open(input, 'r') as f:
        content = f.read()

    print(f"Part01 - Result: {part01(content)}")
    print(f"Part02 - Result: {part02(content)}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()