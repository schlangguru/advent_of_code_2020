from typing import List, Tuple, Dict
import os
import copy
import itertools

import sys
sys.path.append("util")
from decorators import benchmark
import util

from train_ticket import TicketRule, Ticket

def parse_input(input: str) -> Tuple[List[str], str, List[str]]:
    input = input.strip()

    rules: List[str] = []
    my_ticket = str
    nearby_tickets: List[str] = []

    # Every part is separated by 2 new lines
    parts = input.split('\n\n')

    rules = [line.strip() for line in parts[0].split('\n')]
    my_ticket = parts[1].split('\n')[1].strip()
    nearby_tickets = [line.strip() for line in parts[2].split('\n')[1:]]

    return (rules, my_ticket, nearby_tickets)


@benchmark
def part01(rules: List[str], my_ticket: str, nearby_tickets: List[str]):
    rules = [TicketRule.parse(line) for line in rules]
    tickets = [Ticket.parse(line) for line in nearby_tickets]

    invalid_values_per_ticket = [ticket.invalid_values(*rules) for ticket in tickets]
    invalid_values = list(itertools.chain(*invalid_values_per_ticket))

    return sum(invalid_values)


def find_rules(values_per_field: Dict[int, List[int]], rules: List[TicketRule]) -> Dict[int, str]:
    result = {}

    if len(values_per_field.keys()) == 0:
        return result

    # Find all fields where exactly one rule matches all values
    for field_idx, field_values in values_per_field.items():
        possible_rules = list(filter(lambda rule: rule.all_valid(*field_values), rules))
        if len(possible_rules) == 1:
            result[field_idx] = possible_rules[0]

    # Go down in recursion - exclude already found rules
    remaining_rules = [rule for rule in rules if rule not in result.values()]
    remaining_fields = {idx: vals for idx, vals in values_per_field.items() if idx not in result.keys()}
    return {**result, **find_rules(remaining_fields, remaining_rules)}


@benchmark
def part02(rules: List[str], my_ticket: str, nearby_tickets: List[str]):
    rules = [TicketRule.parse(line) for line in rules]
    my_ticket = Ticket.parse(my_ticket)
    nearby_tickets = [Ticket.parse(line) for line in nearby_tickets]

    # fitler out invalid tickets
    nearby_tickets = list(filter(lambda ticket: ticket.is_valid(*rules), nearby_tickets))

    # Create a dict with all values per field idx
    field_count = len(my_ticket.values)
    values_per_field = {}
    for field_idx in range(field_count):
        values_per_field[field_idx] = [ticket.values[field_idx] for ticket in nearby_tickets]

    # Find the rules for each field
    rules_per_field = find_rules(values_per_field, rules)

    # build my ticket representation
    result = 1
    my_ticket_repr = {}
    for field_idx, value in enumerate(my_ticket.values):
        name = rules_per_field[field_idx].name
        my_ticket_repr[name] = value

        if name.startswith('departure'):
            result *= value

    print("My Ticket:", my_ticket_repr)

    return result


def main(input_file: str = "input.txt"):
    working_dir = os.path.dirname(__file__)
    input = os.path.join(working_dir, input_file)

    rules: List[str] = []
    my_ticket = str
    nearby_tickets: List[str] = []

    with open(input, 'r') as f:
        rules, my_ticket, nearby_tickets = parse_input(f.read())


    print(f"Part01 - Result: {part01(copy.deepcopy(rules), copy.deepcopy(my_ticket), copy.deepcopy(nearby_tickets))}")
    print(f"Part02 - Result: {part02(copy.deepcopy(rules), copy.deepcopy(my_ticket), copy.deepcopy(nearby_tickets))}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()