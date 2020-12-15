import os
import unittest

import day15

class TestDay15(unittest.TestCase):

    def test_part01(self):
        self.assertEqual(day15.part01([0, 3, 6], turns=10), 0)
        self.assertEqual(day15.part01([1, 3, 2]), 1)
        self.assertEqual(day15.part01([2, 1, 3]), 10)
        self.assertEqual(day15.part01([1, 2, 3]), 27)
        self.assertEqual(day15.part01([2, 3, 1]), 78)
        self.assertEqual(day15.part01([3, 2, 1]), 438)
        self.assertEqual(day15.part01([3, 1, 2]), 1836)


    def test_part02(self):
        self.assertEqual(day15.part02([0, 3, 6], turns=10), 0)
        # self.assertEqual(day15.part02([1, 3, 2], turns=2020), 1)
        # self.assertEqual(day15.part02([2, 1, 3], turns=2020), 10)
        # self.assertEqual(day15.part02([1, 2, 3], turns=2020), 27)
        # self.assertEqual(day15.part02([2, 3, 1], turns=2020), 78)
        # self.assertEqual(day15.part02([3, 2, 1], turns=2020), 438)
        # self.assertEqual(day15.part02([3, 1, 2], turns=2020), 1836)


if __name__ == '__main__':
    unittest.main()