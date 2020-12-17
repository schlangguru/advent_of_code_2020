from typing import Dict, Tuple, List
from functools import reduce
import itertools

Coord3d = Tuple[int, int, int]

class PocketDimension():

    STATE_ACTIVE = '#'
    STATE_INACTIVE = '.'

    def __init__(self, initial_state: str):
        self.grid = {}

        lines = initial_state.strip().split('\n')
        for y, line in enumerate(lines):
            line = line.strip()
            for x, state in enumerate(line):
                if state in [self.STATE_ACTIVE, self.STATE_INACTIVE]:
                    self.grid[(x, y, 0)] = state
                else:
                    raise Exception(f"state '{state}' is not valid")


    def is_cube_active(self, xyz: Coord3d) -> bool:
        try:
            return self.grid[xyz] == self.STATE_ACTIVE
        except KeyError:
            return False


    def active_cube_count(self) -> int:
        return list(map(lambda xyz: self.is_cube_active(xyz), self.grid.keys())).count(True)


    def neighbours(self, xyz: Coord3d) -> List[Coord3d]:
        x_range = [xyz[0] - 1, xyz[0], xyz[0] + 1]
        y_range = [xyz[1] - 1, xyz[1], xyz[1] + 1]
        z_range = [xyz[2] - 1, xyz[2], xyz[2] + 1]

        return [coords for coords in itertools.product(x_range, y_range, z_range) if coords != xyz]


    def boot(self, cycles: int = 6):
        for i in range(cycles):
            self.expand()
            self.apply_updates()


    def expand(self):
        for xyz in list(self.grid.keys()):
            for neighbour in self.neighbours(xyz):
                if neighbour not in self.grid:
                    self.grid[neighbour] = self.STATE_INACTIVE


    def apply_updates(self):
        updates = []
        for xyz in self.grid.keys():
            if update := self.get_update(xyz): updates.append(update)

        for xyz, state in updates:
            self.grid[xyz] = state


    def get_update(self, xyz: Coord3d) -> Tuple[Coord3d, chr]:
        neighbours = self.neighbours(xyz)
        active_neighbour_count = list(map(lambda xyz: self.is_cube_active(xyz), neighbours)).count(True)
        if self.is_cube_active(xyz):
            if active_neighbour_count not in [2, 3]:
                return (xyz, self.STATE_INACTIVE)
        else:
            if active_neighbour_count == 3:
                return (xyz, self.STATE_ACTIVE)


    def __repr__(self):
        x_range = list(map(lambda xyz: xyz[0], self.grid.keys()))
        y_range = list(map(lambda xyz: xyz[1], self.grid.keys()))
        z_range = list(map(lambda xyz: xyz[2], self.grid.keys()))

        repr = ""
        for z in range(min(z_range), max(z_range) + 1):
            repr += f"z={z}\n"
            repr += "---\n"
            for y in range(min(y_range), max(y_range) + 1):
                for x in range(min(x_range), max(x_range) + 1):
                    state = self.STATE_INACTIVE
                    if self.is_cube_active((x, y, z)):
                        state = self.STATE_ACTIVE
                    repr += state
                repr += "\n"
            repr += "\n"

        return repr


