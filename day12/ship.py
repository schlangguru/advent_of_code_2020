from typing import Tuple

class Ship():

    directions = ('N', 'E', 'S', 'W')

    def __init__(self):
        self.facing_direction = 'E'
        self.position = (0, 0)

    def action(self, action: chr, value: int):
        if action == 'E':
            self._move(value, 0)
        elif action == 'S':
            self._move(0, value)
        elif action == 'W':
            self._move(-value, 0)
        elif action == 'N':
            self._move(0, -value)
        elif action == 'L':
            self._turn(-int(value / 90))
        elif action == 'R':
            self._turn(int(value / 90))
        elif action == 'F':
            self.action(self.facing_direction, value)
        else:
            raise Exception(f"Unkonwn action {action}")

    @property
    def manhattan_distance(self):
        return abs(self.position[0]) + abs(self.position[1])


    def _move(self, *position: Tuple[int, int]):
        self.position = (self.position[0] + position[0], self.position[1] + position[1])


    def _turn(self, direction: int):
        idx = self.directions.index(self.facing_direction) + direction
        idx = idx % 4
        self.facing_direction = self.directions[idx]