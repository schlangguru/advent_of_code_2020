from typing import List, Tuple
import itertools

OCCUPIED_SEAT = '#'
EMPTY_SEAT = 'L'
FLOOR = '.'

class Seat():

    allowed_types = (OCCUPIED_SEAT, EMPTY_SEAT)

    def __init__(self, type: chr):
        if type not in self.allowed_types:
            raise Exception(f"Type {type} not allowed.")

        self.is_occupied = type == OCCUPIED_SEAT
        self.adjacent_seats: List[Seat] = []
        self.nearest_seats: List[Seat] = []


class SeatPlan():

    def __init__(self, plan: List[List[chr]]):
        self.plan: List[List[Seat]] = [[None for i in range(len(plan[0]))] for i in range(len(plan))]
        self.init_seats(plan)
        self.set_adjacent_seats()
        self.set_nearest_seats()


    def init_seats(self, plan: List[List[chr]]):
       for y in range(len(plan)):
            for x in range(len(plan[0])):
                char = plan[y][x]
                if char in ('#', 'L'):
                    self.plan[y][x] = Seat(char)
                else:
                    self.plan[y][x] = None


    def set_adjacent_seats(self):
        """
        Sets the adjacent seats for each seat in the plan.
        """
        for seat_position in self.traverse():
            seat = self.get(seat_position)
            if not seat:
                continue

            for xy in ((-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)):
                adjacent_pos = (seat_position[0] + xy[0], seat_position[1] + xy[1])
                if self.is_in_plan(adjacent_pos):
                    adjacent_seat = self.get(adjacent_pos)
                    if adjacent_seat:
                        seat.adjacent_seats.append(adjacent_seat)


    def set_nearest_seats(self):
        """
        Sets the list of nearest seats in sight for each seat in the plan.
        """
        for seat_position in self.traverse():
            seat = self.get(seat_position)
            if not seat:
                continue

            for direction in ['U', 'UR', 'R', 'DR', 'D', 'DL', 'L', 'UL']:
                nearest_seat = self.nearest_seat(seat_position, direction)
                if nearest_seat:
                    seat.nearest_seats.append(nearest_seat)


    def nearest_seat(self, seat_position: Tuple[int, int], direction: str) -> List[chr]:
        """
        Returns the nearest seat that is in the line of sight from seat_position to direction.
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
        pos = self.go_in_direction(seat_position, direction)
        while self.is_in_plan(pos):
            seat = self.get(pos)
            if seat:
                return seat
            pos = self.go_in_direction(pos, direction)

        return None


    def go_in_direction(self, seat_position: Tuple[int, int], direction: str) -> Tuple[int, int]:
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


    def get(self, seat_position: Tuple[int, int]) -> Seat:
        """
        Returns the seat at the given positon.
        """
        (x, y) = seat_position
        return self.plan[y][x]


    def traverse(self) -> Tuple[int, int]:
        """
        Generator to traverse the seat plan.
        Iterates through all positions in the plan
        """
        for x in range(0, self.width):
            for y in range(0, self.height):
                yield (x, y)


    def count_occupied(self):
        return len([1 for pos in self.traverse() if self.get(pos) and self.get(pos).is_occupied])


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
            (seat_position, occupy) = update
            self.seat_plan.get(seat_position).is_occupied = occupy

        return updates


    def _apply_rules_part01(self, seat_position: Tuple[int, int]) -> Tuple[Tuple[int, int], chr]:
        """
        Occupies or empties the seat according to the rules.
        """
        seat = self.seat_plan.get(seat_position)
        if seat:
            if seat.is_occupied:
                if len(list(filter(lambda s: s.is_occupied, seat.adjacent_seats))) >= 4:
                    return (seat_position, False)
            else:
                if len(list(filter(lambda s: s.is_occupied, seat.adjacent_seats))) == 0:
                    return (seat_position, True)

        None


    def _apply_rules_part02(self, seat_position: Tuple[int, int]) -> Tuple[Tuple[int, int], chr]:
        """
        Occupies or empties the seat according to the rules.
        """
        seat = self.seat_plan.get(seat_position)
        if seat:
            if seat.is_occupied:
                if len(list(filter(lambda s: s.is_occupied, seat.nearest_seats))) >= 5:
                    return (seat_position, False)
            else:
                if len(list(filter(lambda s: s.is_occupied, seat.nearest_seats)))== 0:
                    return (seat_position, True)

        None


