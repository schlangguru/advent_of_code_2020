from typing import Tuple, Sequence, List
import re
import itertools

class TicketRule():

    RULE_PATTERN = re.compile(r"([\w\s]+): (\d+)-(\d+) or (\d+)-(\d+)")

    def __init__(self, name: str, *ranges: Tuple[int, int]):
        self.name = name
        self.ranges = ranges


    @classmethod
    def parse(cls, rule_str: str) -> "TicketRule":
        match = cls.RULE_PATTERN.match(rule_str)
        if match:
            name = match.group(1)
            range0 = (int(match.group(2)), int(match.group(3)))
            range1 = (int(match.group(4)), int(match.group(5)))

            return cls(name, range0, range1)

        raise Exception(f"{cls.RULE_PATTERN} does not match {rule_str}")


    def is_valid(self, value: int) -> bool:
        is_valid = False
        for rng in self.ranges:
            is_valid = is_valid or (rng[0] <= value <= rng[1])

        return is_valid


    def __repr__(self) -> str:
        return f"Ticket Rule: {self.name}: {[rng for rng in self.ranges]}"


class Ticket():

    def __init__(self, *values: int):
        self.values = values


    @classmethod
    def parse(cls, ticket_str: str):
        return cls(*[int(val.strip()) for val in ticket_str.split(',')])


    def invalid_values(self, *rules: TicketRule) -> List[int]:
        valid_values = []
        for rule in rules:
            valid_values += [val for val in self.values if rule.is_valid(val)]

        return [val for val in self.values if val not in valid_values]


    def __repr__(self) -> str:
        return f"Ticket: {[val for val in self.values]}"