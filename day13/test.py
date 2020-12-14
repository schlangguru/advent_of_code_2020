import os
import unittest

import day13

class TestDay13(unittest.TestCase):

    def test_part01(self):
        input = (939, [7,13,59,31,19])
        self.assertEqual(day13.part01(*input), 295)

    def test_part02_1(self):
        input = ['7','13','x','x','59','x','31','19']
        self.assertEqual(day13.part02(input), 1068781)

    def test_part02_2(self):
        input = ['67','7','59','61']
        self.assertEqual(day13.part02(input), 754018)

    def test_part02_3(self):
        input = ['67','7','x','59','61']
        self.assertEqual(day13.part02(input), 1261476)

    def test_part02_4(self):
        input = ['1789','37','47','1889']
        self.assertEqual(day13.part02(input), 1202161486)


if __name__ == '__main__':
    unittest.main()