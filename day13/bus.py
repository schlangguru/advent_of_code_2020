from typing import List, Generator
import itertools
import math

class Bus():
    def __init__(self, id: int):
        self.id = id


    def departure_times(self) -> Generator[int, None, None]:
        """
        Infinite generator for bus departure times.
        """
        for i in itertools.count(0, 1):
            yield i * self.id

    def next_departure_time(self, start: int) -> int:
        return math.ceil(start / self.id) * self.id