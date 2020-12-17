import os
import unittest

import day17
from pocket_dimension import PocketDimension

class TestPocketDimension(unittest.TestCase):

    def test_neighbours(self):
        dimension = PocketDimension("")

        expected = [(-1, -1, -1), (-1, -1, 0), (-1, -1, 1), (-1, 0, -1), (-1, 0, 0), (-1, 0, 1), (-1, 1, -1), (-1, 1, 0), (-1, 1, 1), (0, -1, -1), (0, -1, 0), (0, -1, 1), (0, 0, -1), (0, 0, 1), (0, 1, -1), (0, 1, 0), (0, 1, 1), (1, -1, -1), (1, -1, 0), (1, -1, 1), (1, 0, -1), (1, 0, 0), (1, 0, 1), (1, 1, -1), (1, 1, 0), (1, 1, 1)]
        actual = dimension.neighbours((0, 0, 0))

        self.assertCountEqual(actual, expected)


class TestDay17(unittest.TestCase):

    def test_part01(self):
        state = """
            .#.
            ..#
            ###
        """

        self.assertEqual(day17.part01(state), 112)



    def test_part02(self):
        pass


if __name__ == '__main__':
    unittest.main()