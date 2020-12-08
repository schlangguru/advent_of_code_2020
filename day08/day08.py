import os
import re
from typing import List, Tuple, Dict
import sys
sys.path.append("util")

from decorators import benchmark
from emulation import Status, Emulator

INSRUCTION_PATTERN = re.compile(r"(\w+) ([+-]\d+)")

def parse_instructions(lines: List[str]) -> List[Tuple[str, int]]:
    return list(map(parse_instruction, lines))

def parse_instruction(line: str) -> Tuple[str, int]:
    match = INSRUCTION_PATTERN.match(line)
    if match:
        return (match.group(1), int(match.group(2)))

    raise Exception(f"Instruction {line} did not match pattern {INSRUCTION_PATTERN}")

def fixes(instructions: List[Tuple[str, int]]):
    """
    Generator that applies fixes to the given instructions.
    """
    replacements = {
        "jmp": "nop",
        "nop": "jmp"
    }
    for idx, instruction in enumerate(instructions):
        (operation, value) = instruction
        if operation in replacements.keys():
            new_operation = (replacements[operation], value)
            fixed_instructions = instructions.copy()
            fixed_instructions[idx] = new_operation

            yield fixed_instructions

@benchmark
def part01(lines):
    instructions = parse_instructions(lines)
    emulator = Emulator(instructions)
    emulator.run()
    return {
        "emulator Status": emulator.status,
        "accumulator": emulator.accumulator
    }

@benchmark
def part02(lines):
    instructions = parse_instructions(lines)
    emulator = Emulator(instructions)

    for fixed_instructions in fixes(instructions):
        emulator.reset()
        emulator.instructions = fixed_instructions
        emulator.run()

        if (emulator.status == Status.FINISHED):
            return {
                "emulator Status": emulator.status,
                "accumulator": emulator.accumulator
            }

    raise Exception("No Fix found")

def main():
    working_dir = os.path.dirname(__file__)
    input = os.path.join(working_dir, "input.txt")

    lines = []
    with open(input, 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    print("Part01 - Accumulator value before loop:", part01(lines))
    print("Part02 - Accumulator vaule after fix:", part02(lines))

if __name__ == "__main__":
    main()