import os
import unittest

import day11
import simulation

class TestSeatPlan(unittest.TestCase):

    def test_height_width(self):
        data1 = [".L."]
        data2 = [
            ".",
            "L",
            "."
        ]

        seat_plan1 = simulation.SeatPlan(data1)
        self.assertEqual(seat_plan1.width, 3)
        self.assertEqual(seat_plan1.height, 1)

        seat_plan2 = simulation.SeatPlan(data2)
        self.assertEqual(seat_plan2.width, 1)
        self.assertEqual(seat_plan2.height, 3)


    def test_get(self):
        data1 = [".L."]
        data2 = [
            ".",
            "L",
            "."
        ]

        seat_plan = simulation.SeatPlan(data1)
        self.assertEqual(seat_plan.get((0, 0)), '.')
        self.assertEqual(seat_plan.get((1, 0)), 'L')
        self.assertEqual(seat_plan.get((2, 0)), '.')

        seat_plan = simulation.SeatPlan(data2)
        self.assertEqual(seat_plan.get((0, 0)), '.')
        self.assertEqual(seat_plan.get((0, 1)), 'L')
        self.assertEqual(seat_plan.get((0, 2)), '.')


    def test_adjacent_seats1(self):
        data = read("input.test.txt")
        seat_plan = simulation.SeatPlan(data)

        # Seat in plan
        self.assertEqual(seat_plan.adjacent_seats((1, 1)), ['L', '.', 'L', 'L', 'L', 'L', '.', 'L'])

        # Corners
        self.assertEqual(seat_plan.adjacent_seats((0, 0)), ['.', 'L', 'L'])
        self.assertEqual(seat_plan.adjacent_seats((seat_plan.width-1, 0)), ['L', 'L', 'L'])
        self.assertEqual(seat_plan.adjacent_seats((0, seat_plan.height-1)), ['L', '.', '.'])
        self.assertEqual(seat_plan.adjacent_seats((seat_plan.width-1, seat_plan.height-1)), ['.', 'L', 'L'])


    def test_adjacent_seats2(self):
        data = [
            "L"
        ]

        seat_plan = simulation.SeatPlan(data)

        self.assertEqual(seat_plan.adjacent_seats((0, 0)), [])


    def test_adjacent_seats3(self):
        data1 = [".L."]
        data2 = [
            ".",
            "L",
            "."
        ]

        seat_plan1 = simulation.SeatPlan(data1)
        self.assertEqual(seat_plan1.adjacent_seats((0, 0)), ['L'])
        self.assertEqual(seat_plan1.adjacent_seats((1, 0)), ['.', '.'])
        self.assertEqual(seat_plan1.adjacent_seats((2, 0)), ['L'])

        seat_plan2 = simulation.SeatPlan(data2)
        self.assertEqual(seat_plan2.adjacent_seats((0, 0)), ['L'])
        self.assertEqual(seat_plan2.adjacent_seats((0, 1)), ['.', '.'])
        self.assertEqual(seat_plan2.adjacent_seats((0, 2)), ['L'])


    def test_line_of_sight(self):
        data = [
            "↖..↑..↗",
            ".↖.↑.↗.",
            "-.↖↑↗..",
            "←←←L→→→",
            "-.↙↓↘..",
            "-↙.↓.↘.",
            "↙..↓..↘"
        ]

        seat_plan = simulation.SeatPlan(data)
        pos = (3, 3)
        self.assertEqual(seat_plan.line_of_sight(pos, 'U'), ['↑', '↑', '↑'])
        self.assertEqual(seat_plan.line_of_sight(pos, 'D'), ['↓', '↓', '↓'])
        self.assertEqual(seat_plan.line_of_sight(pos, 'L'), ['←', '←', '←'])
        self.assertEqual(seat_plan.line_of_sight(pos, 'R'), ['→', '→', '→'])
        self.assertEqual(seat_plan.line_of_sight(pos, 'UR'), ['↗', '↗', '↗'])
        self.assertEqual(seat_plan.line_of_sight(pos, 'DR'), ['↘', '↘', '↘'])
        self.assertEqual(seat_plan.line_of_sight(pos, 'UL'), ['↖', '↖', '↖'])
        self.assertEqual(seat_plan.line_of_sight(pos, 'DL'), ['↙', '↙', '↙'])


    def test_nearest_seats1(self):
        data = [
            ".......#.",
            "...#.....",
            ".#.......",
            ".........",
            "..#L....#",
            "....#....",
            ".........",
            "#........",
            "...#....."
        ]

        seat_plan = simulation.SeatPlan(data)
        self.assertEqual(seat_plan.nearest_seats((3, 4)), ['#', '#', '#', '#', '#', '#', '#', '#'])


    def test_nearest_seats2(self):
        data = [
            ".............",
            ".L.L.#.#.#.#.",
            ".............",
        ]

        seat_plan = simulation.SeatPlan(data)
        self.assertEqual(seat_plan.nearest_seats((1, 1)), ['L'])


    def test_nearest_seats3(self):
        data = [
            ".##.##.",
            "#.#.#.#",
            "##...##",
            "...L...",
            "##...##",
            "#.#.#.#",
            ".##.##."
        ]

        seat_plan = simulation.SeatPlan(data)
        self.assertEqual(seat_plan.nearest_seats((3, 3)), [])


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