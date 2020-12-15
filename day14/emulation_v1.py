import re
from typing import List, Dict

class Bitmask():

    def __init__(self, mask: str):
        self.mask = mask

    def apply(self, value: int) -> int:
        bits = self.mask.replace('X', '0')
        mask = int(bits, 2)
        value = mask | value

        bits = self.mask.replace('X', '1')
        mask = int(bits, 2)
        value = mask & value

        return value


class Emulator():

    BITMASK_INSTR_PATTERN = re.compile(r"mask = (\w+)")
    MEM_INSTR_PATTERN = re.compile(r"mem\[(\d+)\] = (\d+)")

    def __init__(self, instructions: List[str]):
        self.instructions = instructions
        self.bitmask: Bitmask = None
        self.mem: Dict[int, int] = {}


    def run(self):
        for instruction in self.instructions:
            self.exec(instruction)

    def exec(self, instruction: str):
        if instruction.startswith("mask"):
            bitmask = self.BITMASK_INSTR_PATTERN.match(instruction).group(1)
            self.set_bitmask(bitmask)
        elif instruction.startswith("mem"):
            match = self.MEM_INSTR_PATTERN.match(instruction)
            self.set_mem(int(match.group(1)), int(match.group(2)))
        else:
            raise Exception(f"Unknown instruction {instruction}")


    def set_bitmask(self, bitmask: str):
        self.bitmask = Bitmask(bitmask)

    def set_mem(self, address: int, value: int):
        value = self.bitmask.apply(value)
        self.mem[address] = value
