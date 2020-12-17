from typing import Dict, Tuple, List
from functools import reduce
import itertools


class PocketDimension():

    STATE_ACTIVE = '#'
    STATE_INACTIVE = '.'

    def __init__(self, initial_state: str, dimensions=3):
        self.grid = {}

        lines = initial_state.strip().split('\n')
        for y, line in enumerate(lines):
            line = line.strip()
            for x, state in enumerate(line):
                if state in [self.STATE_ACTIVE, self.STATE_INACTIVE]:
                    self.grid[(x, y, *(0,)*(dimensions - 2))] = state
                else:
                    raise Exception(f"state '{state}' is not valid")


    def is_cube_active(self, coord: Tuple) -> bool:
        try:
            return self.grid[coord] == self.STATE_ACTIVE
        except KeyError:
            return False


    def active_cube_count(self) -> int:
        return list(map(lambda coord: self.is_cube_active(coord), self.grid.keys())).count(True)


    def neighbours(self, coord: Tuple) -> List[Tuple]:
        ranges = [[p - 1, p, p + 1] for p in coord]
        return [neighbour for neighbour in itertools.product(*ranges) if neighbour != coord]


    def traverse(self):
        for coord in itertools.product(*[range(min(p) - 1, max(p) + 2) for p in zip(*self.grid.keys())]):
            yield coord


    def boot(self, cycles: int=6):
        for _ in range(cycles):
            self.apply_updates()


    def apply_updates(self):
        updates = []
        for coord in self.traverse():
            if update := self.get_update(coord): updates.append(update)

        for coord, state in updates:
            self.grid[coord] = state


    def get_update(self, coord: Tuple) -> Tuple[Tuple, chr]:
        neighbours = self.neighbours(coord)
        active_neighbour_count = list(map(lambda coord: self.is_cube_active(coord), neighbours)).count(True)
        if self.is_cube_active(coord):
            if active_neighbour_count not in [2, 3]:
                return (coord, self.STATE_INACTIVE)
        else:
            if active_neighbour_count == 3:
                return (coord, self.STATE_ACTIVE)

