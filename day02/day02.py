import os
import re

from CorporatePolicy import CorporatePolicy

database_entry_pattern = re.compile(r"(\d+)-(\d+) (\w): (\w+)")

def parse_passwords(lines):
    passwords = [parse_password(line.strip()) for line in lines]
    return list(filter(lambda pw: pw != None, passwords))

def parse_password(line):
    match = database_entry_pattern.match(line)
    if match:
        min = int(match.group(1))
        max = int(match.group(2))
        char = match.group(3)
        password = match.group(4)
        return (CorporatePolicy(min, max, char), password)
    else:
        raise Exception(f"Regex did not match '{line}''")

def get_number_of_valid_passwords(lines):
    entries = parse_passwords(lines)
    return len(list(filter(is_password_valid, entries)))

def is_password_valid(entry):
    policy = entry[0]
    password = entry[1]
    return policy.check_password(password)

def main():
    working_dir = os.path.dirname(__file__)
    input_file = os.path.join(working_dir, "input.txt")

    with open(input_file, 'r') as f:
        number_of_valid_passwords = get_number_of_valid_passwords(f.readlines())

    print("Number of valid passwords:", number_of_valid_passwords)


if __name__ == '__main__':
    main()