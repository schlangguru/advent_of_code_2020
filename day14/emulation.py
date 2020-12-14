from typing import List

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

    def __init__(self):
        self.bitmask: Bitmask = None
        self.mem: List[int]= [0]*36

