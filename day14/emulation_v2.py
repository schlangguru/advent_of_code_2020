import re
import itertools
from typing import List, Dict

class Bitmask():

    def __init__(self, mask: str):
        self.mask = mask

    def apply(self, address: int) -> List[int]:
        # overwrite 1s
        bits = self.mask.replace('X', '0')
        mask = int(bits, 2)
        address = mask | address

        # Generate floating masks
        combinations = itertools.product('01', repeat=self.mask.count('X'))
        bit_list = [int(self.mask.replace('1', '0').replace('X', '{}').format(*bits), 2) for bits in combinations]
        address_list = [address ^ bits for bits in bit_list]

        return address_list


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
        address_list = self.bitmask.apply(address)
        for mapped_address in address_list:
            self.mem[mapped_address] = value
