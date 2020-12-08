import os
import re
from functools import reduce

BAG_NAME_PATTERN = re.compile(r"^(\w+) (w+)")
CONTAINED_BAGS_PATTERN = re.compile(r"(\d+) (\w+ \w+) bags?")
NO_CONTAINED_BAGS_PATTERN = re.compile("no other bags")

def parse_rules(rule_lines):
    return list(map(parse_rule, rule_lines))

def parse_rule(rule_line):
    rule_parts = rule_line.split(" bags contain ")
    color = rule_parts[0]
    contains = parse_contained_bags(rule_parts[1])
    return {
        "color": color,
        "contains": contains
    }

def parse_contained_bags(contained_bags_str):
    contained_bags = []
    # finds list of tuples like: [('1', 'bright white'), ('2', 'muted yellow')]
    matches = CONTAINED_BAGS_PATTERN.findall(contained_bags_str)
    for match in matches:
        contained_bags.append({
            "count": int(match[0]),
            "color": match[1]
        })

    return contained_bags

def find_bags_that_can_contain(bag_color, rules):
    return [rule["color"] for rule in rules if can_contain(bag_color, rule)]

def can_contain(bag_color, rule):
    return bag_color in list(map(lambda dict: dict["color"], rule["contains"]))

def count_bags(bag_color, rules):
    count = 1
    [rule] = filter(lambda rule: rule["color"] == bag_color, rules)
    inner_bags = rule["contains"]
    for inner_bag in inner_bags:
        count += inner_bag["count"] * count_bags(inner_bag["color"], rules)

    return count

def part01(rule_lines):
    my_bag = "shiny gold"
    rules = parse_rules(rule_lines)
    bags = find_bags_that_can_contain(my_bag, rules)
    new_bags_added = True
    while new_bags_added:
        possible_new_bags = []
        for bag in bags:
            possible_new_bags += [bag for bag in find_bags_that_can_contain(bag, rules) if bag not in possible_new_bags]
        new_bags = [bag for bag in possible_new_bags if bag not in bags]
        if len(new_bags) > 0:
            new_bags_added = True
            bags += new_bags
        else:
            new_bags_added = False

    return len(bags)

def part02(rule_lines):
    my_bag = "shiny gold"
    rules = parse_rules(rule_lines)
    bag_count = count_bags(my_bag, rules)
    containing_bag_count = bag_count -1
    return containing_bag_count

def main():
    working_dir = os.path.dirname(__file__)
    input = os.path.join(working_dir, "input.txt")

    lines = []
    with open(input, 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    print("Part01 - Number of bags that may contian 'shiny gold'", part01(lines))
    print("Part02 - Number bags in 'shiny gold'", part02(lines))

if __name__ == "__main__":
    main()