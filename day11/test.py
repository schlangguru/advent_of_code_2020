import os
import unittest

import day11
from simulation import SeatPlanSimulator, SeatPlan, Seat

class TestSeatPlan(unittest.TestCase):

    def test_height_width(self):
        data1 = [".L."]
        data2 = [
            ".",
            "L",
            "."
        ]

        seat_plan1 = SeatPlan(data1)
        self.assertEqual(seat_plan1.width, 3)
        self.assertEqual(seat_plan1.height, 1)

        seat_plan2 = SeatPlan(data2)
        self.assertEqual(seat_plan2.width, 1)
        self.assertEqual(seat_plan2.height, 3)


    def test_get(self):
        data1 = [".L."]
        data2 = [
            ".",
            "L",
            "."
        ]

        seat_plan = SeatPlan(data1)
        self.assertEqual(seat_plan.get((0, 0)), None)
        self.assertEqual(seat_plan.get((1, 0)).is_occupied, False)
        self.assertEqual(seat_plan.get((2, 0)), None)

        seat_plan = SeatPlan(data2)
        self.assertEqual(seat_plan.get((0, 0)), None)
        self.assertEqual(seat_plan.get((0, 1)).is_occupied, False)
        self.assertEqual(seat_plan.get((0, 2)), None)


    def test_adjacent_seats(self):
        data = read("input.test.txt")
        seat_plan = SeatPlan(data)

        # Seat in plan
        l = list(map(lambda s: s.is_occupied, seat_plan.get((1, 1)).adjacent_seats))
        self.assertEqual(l, [False, False, False, False, False, False])

        # Corners
        l = list(map(lambda s: s.is_occupied, seat_plan.get((0, 0)).adjacent_seats))
        self.assertEqual(l, [False, False])
        l = list(map(lambda s: s.is_occupied, seat_plan.get((seat_plan.width-1, 0)).adjacent_seats))
        self.assertEqual(l, [False, False, False])
        l = list(map(lambda s: s.is_occupied, seat_plan.get((0, seat_plan.height-1)).adjacent_seats))
        self.assertEqual(l, [False])
        l = list(map(lambda s: s.is_occupied, seat_plan.get((seat_plan.width-1, seat_plan.height-1)).adjacent_seats))
        self.assertEqual(l, [False, False])


    def test_nearest_seats1(self):
        data = [
            ".......#.",
            "...#.....",
            ".#.......",
            ".........",
            "..#L....L",
            "....#....",
            ".........",
            "#........",
            "...#....."
        ]

        seat_plan = SeatPlan(data)
        l = list(map(lambda s: s.is_occupied, seat_plan.get((3, 4)).nearest_seats))
        self.assertEqual(l, [True, True, False, True, True, True, True, True])


class TestDay11(unittest.TestCase):

    def test_part01(self):
        data = read("input.test.txt")
        self.assertEqual(day11.part01(data), 37)


    def test_part02(self):
        data = read("input.test.txt")
        self.assertEqual(day11.part02(data), 26)



def read(input: str):
    working_dir = os.path.dirname(__file__)
    input = os.path.join(working_dir, input)

    data = []
    with open(input, 'r') as f:
        data = [list(line.strip()) for line in f.readlines()]

    return data

if __name__ == '__main__':
    unittest.main()