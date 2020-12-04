import os
import re

import passport_rules

FIELD_PATTERN = re.compile(r"(byr|iyr|eyr|hgt|hcl|ecl|pid|cid):([#\w]+)")

def parse_documents(input):
    separated_documents = input.split("\n\n")
    return list(map(parse_document, separated_documents))

def parse_document(input):
    document_str = input.replace("\n", " ").strip()
    document = dict(FIELD_PATTERN.findall(document_str))

    return document

def part01(input):
    documents = parse_documents(input)
    return list(map(passport_rules.has_required_fields, documents)).count(True)

def part02(input):
    documents = parse_documents(input)
    return list(map(passport_rules.is_valid, documents)).count(True)

def main():
    working_dir = os.path.dirname(__file__)
    input_file = os.path.join(working_dir, "input.txt")

    content = ""
    with open(input_file, 'r') as f:
        content = f.read()

    print("Part01 - Numver of valid passports:", part01(content))
    print("Part02 - Numver of valid passports:", part02(content))

if __name__ == "__main__":
    main()