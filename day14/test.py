import os
import unittest

import day14
import emulation_v1 as v1
import emulation_v2 as v2

class TestDay12(unittest.TestCase):

    def test_bitmask_v1(self):
        mask = v1.Bitmask("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X")
        self.assertEqual(mask.apply(11), 73)

        mask = v1.Bitmask("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X")
        self.assertEqual(mask.apply(101), 101)

        mask = v1.Bitmask("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X")
        self.assertEqual(mask.apply(0), 64)


    def test_bitmask_v2(self):
        mask = v2.Bitmask("000000000000000000000000000000X1001X")
        self.assertCountEqual(mask.apply(42), [26, 27, 58, 59])

        mask = v2.Bitmask("00000000000000000000000000000000X0XX")
        self.assertCountEqual(mask.apply(26), [16, 17, 18, 19, 24, 25, 26, 27])


    def test_part01(self):
        input = [
            "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
            "mem[8] = 11",
            "mem[7] = 101",
            "mem[8] = 0"
        ]

        self.assertEqual(day14.part01(input), 165)


    # def test_part02(self):
    #     input = [
    #         "mask = 000000000000000000000000000000X1001X",
    #         "mem[42] = 100",
    #         "mask = 00000000000000000000000000000000X0XX",
    #         "mem[26] = 1"
    #     ]

    #     self.assertEqual(day14.part02(input), 208)


if __name__ == '__main__':
    unittest.main()