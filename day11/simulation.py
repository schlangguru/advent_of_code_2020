from typing import List, Tuple
import itertools

OCCUPIED_SEAT = '#'
EMPTY_SEAT = 'L'
FLOOR = '.'

class SeatPlan():

    def __init__(self, plan: List[List[chr]]):
        self.plan = plan

    @property
    def height(self) -> int:
        """
        Height of the seat plan.
        """
        return len(self.plan)

    @property
    def width(self) -> int:
        """
        Width of the seat plan.
        """
        return len(self.plan[0])


    def adjacent_seats(self, seat_position: Tuple[int, int]) -> List[str]:
        """
        Retruns a list of adjacent seats to the given seat.
        Adjacent seats are order from left to right and top to bottom.
        """
        (x, y) = seat_position
        result = []
        y_range = (max(0, y-1), min(self.height, y+2)) # upper bound is exclusive
        x_range = (max(0, x-1), min(self.width, x+2)) # upper bound is exclusive
        for j in range(*y_range):
            for i in range(*x_range):
                if seat_position != (i, j):
                    result.append(self.get((i, j)))

        return result

    def nearest_seats(self, seat_position: Tuple[int, int]) -> List[str]:
        """
        Returns a list of seats that are first in sight of each direction from the given seat_position.
        """
        result = []
        for direction in ['U', 'UR', 'R', 'DR', 'D', 'DL', 'L', 'UL']:
            line = self.line_of_sight(seat_position, direction)
            nearest_seat = next((s for s in line if s != '.'), None)
            if nearest_seat:
                result.append(nearest_seat)

        return result


    def get(self, seat_position: Tuple[int, int]) -> chr:
        """
        Returns the seat at the given positon.
        """
        (x, y) = seat_position
        return self.plan[y][x]

    def set(self, seat_position: Tuple[int, int], seat: chr):
        """
        Changes the seat at the given positoin.
        Raises an exception if the given position is floor.
        """
        (x, y) = seat_position
        if self.get((x, y)) == FLOOR:
            raise Exception(f"Cannot change {seat_position}. It is floor.")
        if seat != OCCUPIED_SEAT and seat != EMPTY_SEAT:
            raise Exception(f"Cannot set {seat}. Not an allowed value.")

        self.plan[y][x] = seat


    def traverse(self) -> Tuple[int, int]:
        """
        Generator to traverse the seat plan.
        Iterates through all positions in the plan
        """
        for x in range(0, self.width):
            for y in range(0, self.height):
                yield (x, y)

    def line_of_sight(self, seat_position: Tuple[int, int], direction: str) -> List[chr]:
        """
        Returns a list of seats that are in the line of sight from seat_position to direction.
        Allowed directions are:
        - U: up
        - R: right
        - D: down
        - L: left
        - UR: diagonal up - right
        - DR: diagnoal down - right
        - UL: diagnoal up - left
        - DL: diagonal down - left
        """
        result = []
        pos = self.go_to_direction(seat_position, direction)
        while self.is_in_plan(pos):
            s = self.get(pos)
            result.append(s)
            if s == '#' or s == 'L':
                break
            pos = self.go_to_direction(pos, direction)

        return result

    def go_to_direction(self, seat_position: Tuple[int, int], direction: str) -> Tuple[int, int]:
        (x, y) = seat_position
        if 'U' in direction:
            y -= 1
        if 'D' in direction:
            y += 1
        if 'L' in direction:
            x -= 1
        if 'R' in direction:
            x += 1

        return (x, y)

    def is_in_plan(self, seat_position: Tuple[int, int]) -> bool:
        (x, y) = seat_position
        return (0 <= x and x < self.width) and (0 <= y and y < self.height)

    def count(self, seat: chr):
        return len([1 for pos in self.traverse() if self.get(pos) == seat])


    def __repr__(self):
        result = ""
        for row in self.plan:
            result += "".join(row)
            result += "\n"

        return result


class SeatPlanSimulator():

    def __init__(self, seat_plan: SeatPlan, rule_set: str):
        self.seat_plan = seat_plan
        rule_sets = {
            "part01": self._apply_rules_part01,
            "part02": self._apply_rules_part02,
        }
        self.rule_set = rule_sets[rule_set]

    def simulate_round(self) -> Tuple[Tuple[int, int]]:
        """
        Simulates one round.
        Returns the updates applied in this round.
        """
        updates = []
        for (x, y) in self.seat_plan.traverse():
            update = self.rule_set((x, y))
            if update:
                updates.append(update)

        for update in updates:
            (seat_position, seat) = update
            self.seat_plan.set(seat_position, seat)

        return updates

    def _apply_rules_part01(self, seat_position: Tuple[int, int]) -> Tuple[Tuple[int, int], chr]:
        """
        Occupies or empties the seat according to the rules.
        """
        seat = self.seat_plan.get(seat_position)
        adj_seats = self.seat_plan.adjacent_seats(seat_position)
        if seat == EMPTY_SEAT:
            if adj_seats.count(OCCUPIED_SEAT) == 0:
                return (seat_position, OCCUPIED_SEAT)
        elif seat == OCCUPIED_SEAT:
            if adj_seats.count(OCCUPIED_SEAT) >= 4:
                return (seat_position, EMPTY_SEAT)

        None


    def _apply_rules_part02(self, seat_position: Tuple[int, int]) -> Tuple[Tuple[int, int], chr]:
        """
        Occupies or empties the seat according to the rules.
        """
        seat = self.seat_plan.get(seat_position)
        nearest_seats = self.seat_plan.nearest_seats(seat_position)
        if seat == EMPTY_SEAT:
            if nearest_seats.count(OCCUPIED_SEAT) == 0:
                return (seat_position, OCCUPIED_SEAT)
        elif seat == OCCUPIED_SEAT:
            if nearest_seats.count(OCCUPIED_SEAT) >= 5:
                return (seat_position, EMPTY_SEAT)

        None


