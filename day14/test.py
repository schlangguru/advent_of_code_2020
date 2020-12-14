import os
import unittest

import day14
from emulation import Bitmask

class TestDay12(unittest.TestCase):

    def test_bitmask(self):
        mask = Bitmask("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X")
        self.assertEqual(mask.apply(11), 73)

        mask = Bitmask("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X")
        self.assertEqual(mask.apply(101), 101)

        mask = Bitmask("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X")
        self.assertEqual(mask.apply(0), 64)


    def test_part01(self):
        input = [
            "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
            "mem[8] = 11",
            "mem[7] = 101",
            "mem[8] = 0"
        ]

        self.assertEqual(day14.part01(input), 165)


if __name__ == '__main__':
    unittest.main()