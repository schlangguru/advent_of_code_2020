from typing import List, Tuple, Dict
from enum import Enum

# Type aliases
Instruction = Tuple[str, int]
class Status(Enum):
    NOT_STARTED = "not-started"
    RUNNING = "running"
    LOOP = "loop"
    FINISHED = "finished"

class Emulator():
    """
    The Emulator executes Handheld Console bootcode in isolation.
    """
    def __init__(self, instructions: List[Instruction]):
        self.status = Status.NOT_STARTED
        self.instruction_pointer = 0
        self.instructions = instructions
        self.accumulator = 0
        self.operations = {
            "nop": self.nop,
            "jmp": self.jmp,
            "acc": self.acc
        }

    def run(self):
        """
        Runs the instructions either until an instruction will be exectured a second time (infinite loop)
        or the the program finishes (instruction_pointer hits end of instruction list).
        Returns the current value of the accumulator.
        """
        self.status = Status.RUNNING
        executed_instructions: List[int] = []
        while self.status == Status.RUNNING:
            executed_instructions.append(self.instruction_pointer)
            self.execute_instruction()
            if (self.instruction_pointer in executed_instructions):
                self.status = Status.LOOP
            if (self.instruction_pointer >= len(self.instructions)):
                self.status = Status.FINISHED

    def reset(self):
        self.status = Status.NOT_STARTED
        self.accumulator = 0
        self.instruction_pointer = 0

    def execute_instruction(self):
        """
        Executes the instruction the instruction the pointer currently point to.
        Moves the instruction_pointer to the next instruction.
        """
        (operation, value) = self.instructions[self.instruction_pointer]
        self.operations[operation](value)

    # ------------
    # Instructions
    # ------------
    def nop(self, value: int):
        """
        NOP instruction.
        """
        self.instruction_pointer += 1

    def jmp(self, value: int):
        """
        JMP instruction.
        """
        self.instruction_pointer += value

    def acc(self, value: int):
        """
        ACC instruction.
        """
        self.accumulator += value
        self.instruction_pointer += 1

