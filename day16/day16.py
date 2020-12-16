from typing import List, Tuple
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


@benchmark
def part02(rules: List[str], my_ticket: str, nearby_tickets: List[str]):
    pass


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