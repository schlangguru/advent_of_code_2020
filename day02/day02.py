import os
import re

from corporate_policies import SledRentalCorporatePolicy, TobogganCorporatePolicy

database_entry_pattern = re.compile(r"(\d+)-(\d+) (\w): (\w+)")

def parse_password(line):
    match = database_entry_pattern.match(line)
    if match:
        return {
            "numbers": [
                int(match.group(1)),
                int(match.group(2))
            ],
            "char": match.group(3),
            "password": match.group(4)
        }
    else:
        raise Exception(f"Regex did not match '{line}''")

def part01(lines):
    entries = [parse_password(line.strip()) for line in lines]
    return len(list(filter(lambda entry:
        SledRentalCorporatePolicy(entry["numbers"][0], entry["numbers"][1], entry["char"])
            .check_password(entry["password"]),
        entries)))

def part02(lines):
    entries = [parse_password(line.strip()) for line in lines]
    return len(list(filter(lambda entry:
        TobogganCorporatePolicy(entry["numbers"][0], entry["numbers"][1], entry["char"])
            .check_password(entry["password"]),
        entries)))


def main():
    working_dir = os.path.dirname(__file__)
    input_file = os.path.join(working_dir, "input.txt")

    lines = []
    with open(input_file, 'r') as f:
        lines = f.readlines()

    print("Part 01 - Number of valid passwords:", part01(lines))
    print("Part 02 - Number of valid passwords:", part02(lines))


if __name__ == '__main__':
    main()